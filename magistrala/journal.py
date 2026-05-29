import requests

from magistrala import response
from magistrala import errors
from magistrala import utils


class Journal:
    """Journal API client.

    Retrieves audit/activity logs for entities and users, and client telemetry.
    """

    JOURNAL_ENDPOINT = "journal"

    def __init__(self, url: str):
        self.URL = url

    def list_by_entity(
        self,
        entity_type: str,
        entity_id: str,
        domain_id: str,
        query_params: dict,
        token: str,
    ):
        """Retrieves journal entries for a domain entity (client, channel, group).

        params:
            entity_type: str - e.g. "client", "channel", "group"
            entity_id: str - unique entity ID
            domain_id: str - domain the entity belongs to
            query_params: dict - pagination/filter params
            token: str - authorization token

        returns:
            mf_resp: response.Response - response object with JournalsPage
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.JOURNAL_ENDPOINT
            + "/"
            + entity_type
            + "/"
            + entity_id,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.journal["list_by_entity"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list_by_user(self, user_id: str, query_params: dict, token: str):
        """Retrieves journal entries for a user.

        params:
            user_id: str - unique user ID
            query_params: dict - pagination/filter params
            token: str - authorization token

        returns:
            mf_resp: response.Response - response object with JournalsPage
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.JOURNAL_ENDPOINT + "/user/" + user_id,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.journal["list_by_user"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def client_telemetry(self, client_id: str, domain_id: str, token: str):
        """Retrieves telemetry data for a client.

        params:
            client_id: str - unique client ID
            domain_id: str - domain the client belongs to
            token: str - authorization token

        returns:
            mf_resp: response.Response - response object with ClientTelemetry
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.JOURNAL_ENDPOINT
            + "/client/"
            + client_id
            + "/telemetry",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.journal["client_telemetry"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
