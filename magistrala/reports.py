import requests

from magistrala import response
from magistrala import errors
from magistrala import utils
from magistrala.roles import Roles


class Reports:
    """Reports API client.

    Handles on-demand report generation and scheduled report configuration.
    """

    REPORTS_ENDPOINT = "reports"
    CONFIGS_ENDPOINT = "reports/configs"

    def __init__(self, url: str):
        self.URL = url
        self.__roles = Roles()

    def generate(self, domain_id: str, report_config: dict, token: str):
        """Generates a report on demand.

        params:
            domain_id: str - domain ID
            report_config: dict - report request with metrics, time range,
                aggregation, and optional file_format
            token: str - authorization token

        returns:
            mf_resp: response.Response - response object with ReportPage
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + domain_id + "/" + self.REPORTS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            json=report_config,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["generate"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    # Report Configs

    def add_config(self, domain_id: str, config: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + domain_id + "/" + self.CONFIGS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            json=config,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["add_config"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_config(self, domain_id: str, config_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + domain_id + "/" + self.CONFIGS_ENDPOINT + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["get_config"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list_configs(self, domain_id: str, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + domain_id + "/" + self.CONFIGS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["list_configs"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_config(self, domain_id: str, config: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.put(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config["id"],
            headers=utils.construct_header(token, utils.CTJSON),
            json=config,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["update_config"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_schedule(
        self, domain_id: str, config_id: str, schedule: dict, token: str
    ):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config_id
            + "/schedule",
            headers=utils.construct_header(token, utils.CTJSON),
            json=schedule,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["update_schedule"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete_config(self, domain_id: str, config_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL + "/" + domain_id + "/" + self.CONFIGS_ENDPOINT + "/" + config_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["delete_config"], http_resp.status_code
            )
        else:
            mf_resp.value = "Report config deleted successfully"
        return mf_resp

    def enable_config(self, domain_id: str, config_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config_id
            + "/enable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["enable_config"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable_config(self, domain_id: str, config_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config_id
            + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["disable_config"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_template(self, domain_id: str, config_id: str, template: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.put(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config_id
            + "/template",
            headers=utils.construct_header(token, utils.CTJSON),
            json=template,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["update_template"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_template(self, domain_id: str, config_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config_id
            + "/template",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["get_template"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete_template(self, domain_id: str, config_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CONFIGS_ENDPOINT
            + "/"
            + config_id
            + "/template",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.reports["delete_template"], http_resp.status_code
            )
        else:
            mf_resp.value = "Report template deleted successfully"
        return mf_resp

    # Role management

    def list_available_actions(self, domain_id: str, token: str):
        return self.__roles.list_available_actions(
            self.URL + "/" + domain_id, self.CONFIGS_ENDPOINT, token
        )

    def create_role(
        self,
        domain_id: str,
        config_id: str,
        role_name: str,
        token: str,
        optional_actions: list = None,
        optional_members: list = None,
    ):
        return self.__roles.create_role(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_name,
            token,
            optional_actions,
            optional_members,
        )

    def list_roles(
        self, domain_id: str, config_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_roles(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            query_params,
            token,
        )

    def get_role(self, domain_id: str, config_id: str, role_id: str, token: str):
        return self.__roles.get_role(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            token,
        )

    def update_role(
        self, domain_id: str, config_id: str, role_id: str, role: dict, token: str
    ):
        return self.__roles.update_role(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            role,
            token,
        )

    def delete_role(self, domain_id: str, config_id: str, role_id: str, token: str):
        return self.__roles.delete_role(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            token,
        )

    def add_role_actions(
        self, domain_id: str, config_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.add_role_actions(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            actions,
            token,
        )

    def list_role_actions(
        self, domain_id: str, config_id: str, role_id: str, token: str
    ):
        return self.__roles.list_role_actions(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            token,
        )

    def delete_role_actions(
        self, domain_id: str, config_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.delete_role_actions(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            actions,
            token,
        )

    def delete_all_role_actions(
        self, domain_id: str, config_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_actions(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            token,
        )

    def add_role_members(
        self, domain_id: str, config_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.add_role_members(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            members,
            token,
        )

    def list_role_members(
        self, domain_id: str, config_id: str, role_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_role_members(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            query_params,
            token,
        )

    def delete_role_members(
        self, domain_id: str, config_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.delete_role_members(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            members,
            token,
        )

    def delete_all_role_members(
        self, domain_id: str, config_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_members(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            role_id,
            token,
        )

    def list_members(
        self, domain_id: str, config_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_entity_members(
            self.URL + "/" + domain_id,
            self.CONFIGS_ENDPOINT,
            config_id,
            query_params,
            token,
        )
