import requests

from magistrala import response
from magistrala import errors


_SERVICE_URLS = [
    "users",
    "clients",
    "channels",
    "groups",
    "bootstrap",
    "certs",
    "reader",
    "http_adapter",
    "journal",
    "domains",
    "auth",
]


class Health:
    """Health check API client.

    Checks the health of individual Magistrala services.
    Each service URL is optional; only provided services can be checked.
    """

    HEALTH_ENDPOINT = "health"

    def __init__(
        self,
        users_url: str = "",
        clients_url: str = "",
        channels_url: str = "",
        groups_url: str = "",
        bootstrap_url: str = "",
        certs_url: str = "",
        reader_url: str = "",
        http_adapter_url: str = "",
        journal_url: str = "",
        domains_url: str = "",
        auth_url: str = "",
    ):
        self._urls = {
            "users": users_url,
            "clients": clients_url,
            "channels": channels_url,
            "groups": groups_url,
            "bootstrap": bootstrap_url,
            "certs": certs_url,
            "reader": reader_url,
            "http-adapter": http_adapter_url,
            "journal": journal_url,
            "domains": domains_url,
            "auth": auth_url,
        }

    def check(self, service: str):
        """Checks the health of the given service.

        params:
            service: str - one of: users, clients, channels, groups,
                bootstrap, certs, reader, http-adapter, journal, domains, auth

        returns:
            mf_resp: response.Response - response object with HealthInfo dict
        """
        mf_resp = response.Response()
        base_url = self._urls.get(service, "")
        if not base_url:
            mf_resp.error.status = 1
            mf_resp.error.message = (
                "Unknown or unconfigured service: " + service
            )
            return mf_resp
        try:
            http_resp = requests.get(base_url + "/" + self.HEALTH_ENDPOINT)
        except Exception as e:
            mf_resp.error.status = 1
            mf_resp.error.message = str(e)
            return mf_resp
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.health["check"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
