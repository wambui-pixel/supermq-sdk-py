import requests

from magistrala import response
from magistrala import errors
from magistrala import utils
from magistrala.roles import Roles


class Rules:
    """Rules Engine API client.

    Manages rules that process incoming messages and trigger outputs
    such as channel forwards, alarms, and email notifications.
    """

    RULES_ENDPOINT = "rules"

    def __init__(self, url: str):
        self.URL = url
        self.__roles = Roles()

    def create(self, domain_id: str, rule: dict, token: str):
        """Creates a new rule.

        params:
            domain_id: str - domain the rule belongs to
            rule: dict - rule definition with name, input_channel,
                input_topic, logic, outputs, schedule fields
            token: str - authorization token

        returns:
            mf_resp: response.Response - response object with Rule
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + domain_id + "/" + self.RULES_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            json=rule,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def view(self, domain_id: str, rule_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + domain_id + "/" + self.RULES_ENDPOINT + "/" + rule_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["view"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list(self, domain_id: str, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + domain_id + "/" + self.RULES_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["list"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, domain_id: str, rule: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.put(
            self.URL + "/" + domain_id + "/" + self.RULES_ENDPOINT + "/" + rule["id"],
            headers=utils.construct_header(token, utils.CTJSON),
            json=rule,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_tags(self, domain_id: str, rule: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.RULES_ENDPOINT
            + "/"
            + rule["id"]
            + "/tags",
            headers=utils.construct_header(token, utils.CTJSON),
            json=rule,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["update_tags"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_schedule(self, domain_id: str, rule_id: str, schedule: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.RULES_ENDPOINT
            + "/"
            + rule_id
            + "/schedule",
            headers=utils.construct_header(token, utils.CTJSON),
            json=schedule,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["update_schedule"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def enable(self, domain_id: str, rule_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.RULES_ENDPOINT
            + "/"
            + rule_id
            + "/enable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["enable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, domain_id: str, rule_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.RULES_ENDPOINT
            + "/"
            + rule_id
            + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["disable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete(self, domain_id: str, rule_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL + "/" + domain_id + "/" + self.RULES_ENDPOINT + "/" + rule_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.rules["delete"], http_resp.status_code
            )
        else:
            mf_resp.value = "Rule deleted successfully"
        return mf_resp

    # Role management

    def list_available_actions(self, domain_id: str, token: str):
        return self.__roles.list_available_actions(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, token
        )

    def create_role(
        self,
        domain_id: str,
        rule_id: str,
        role_name: str,
        token: str,
        optional_actions: list = None,
        optional_members: list = None,
    ):
        return self.__roles.create_role(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_name,
            token,
            optional_actions,
            optional_members,
        )

    def list_roles(self, domain_id: str, rule_id: str, query_params: dict, token: str):
        return self.__roles.list_roles(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, query_params, token
        )

    def get_role(self, domain_id: str, rule_id: str, role_id: str, token: str):
        return self.__roles.get_role(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, role_id, token
        )

    def update_role(
        self, domain_id: str, rule_id: str, role_id: str, role: dict, token: str
    ):
        return self.__roles.update_role(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_id,
            role,
            token,
        )

    def delete_role(self, domain_id: str, rule_id: str, role_id: str, token: str):
        return self.__roles.delete_role(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, role_id, token
        )

    def add_role_actions(
        self, domain_id: str, rule_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.add_role_actions(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_id,
            actions,
            token,
        )

    def list_role_actions(
        self, domain_id: str, rule_id: str, role_id: str, token: str
    ):
        return self.__roles.list_role_actions(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, role_id, token
        )

    def delete_role_actions(
        self, domain_id: str, rule_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.delete_role_actions(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_id,
            actions,
            token,
        )

    def delete_all_role_actions(
        self, domain_id: str, rule_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_actions(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, role_id, token
        )

    def add_role_members(
        self, domain_id: str, rule_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.add_role_members(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_id,
            members,
            token,
        )

    def list_role_members(
        self, domain_id: str, rule_id: str, role_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_role_members(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_id,
            query_params,
            token,
        )

    def delete_role_members(
        self, domain_id: str, rule_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.delete_role_members(
            self.URL + "/" + domain_id,
            self.RULES_ENDPOINT,
            rule_id,
            role_id,
            members,
            token,
        )

    def delete_all_role_members(
        self, domain_id: str, rule_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_members(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, role_id, token
        )

    def list_members(
        self, domain_id: str, rule_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_entity_members(
            self.URL + "/" + domain_id, self.RULES_ENDPOINT, rule_id, query_params, token
        )
