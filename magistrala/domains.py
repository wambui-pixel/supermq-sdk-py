import requests
from typing import List

from magistrala import response
from magistrala import errors
from magistrala import utils
from magistrala.roles import Roles


class Domains:
    """Domains API client.

    Handles domain lifecycle and membership via invitations.
    Role management is available through the shared Roles helper.
    """

    DOMAINS_ENDPOINT = "domains"
    INVITATIONS_ENDPOINT = "invitations"

    def __init__(self, url: str):
        self.URL = url
        self.__roles = Roles()

    def create(self, domain: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.DOMAINS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            json=domain,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.DOMAINS_ENDPOINT + "/" + domain_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list(self, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.DOMAINS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["list"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list_by_user(self, user_id: str, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/users/" + user_id + "/" + self.DOMAINS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["list"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, domain: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.DOMAINS_ENDPOINT + "/" + domain["id"],
            headers=utils.construct_header(token, utils.CTJSON),
            json=domain,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def enable(self, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.DOMAINS_ENDPOINT + "/" + domain_id + "/enable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["enable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.DOMAINS_ENDPOINT + "/" + domain_id + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["disable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def freeze(self, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.DOMAINS_ENDPOINT + "/" + domain_id + "/freeze",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["freeze"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    # Invitations

    def send_invitation(self, invitation: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.INVITATIONS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            json=invitation,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["send_invitation"], http_resp.status_code
            )
        else:
            mf_resp.value = "Invitation sent successfully"
        return mf_resp

    def get_invitation(self, user_id: str, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL
            + "/"
            + self.INVITATIONS_ENDPOINT
            + "/"
            + user_id
            + "/"
            + domain_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["get_invitation"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list_invitations(self, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.INVITATIONS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["list_invitations"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list_user_invitations(self, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.INVITATIONS_ENDPOINT + "/me",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["list_invitations"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def accept_invitation(self, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + self.INVITATIONS_ENDPOINT
            + "/"
            + domain_id
            + "/accept",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["accept_invitation"], http_resp.status_code
            )
        else:
            mf_resp.value = "Invitation accepted successfully"
        return mf_resp

    def reject_invitation(self, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + self.INVITATIONS_ENDPOINT
            + "/"
            + domain_id
            + "/reject",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["reject_invitation"], http_resp.status_code
            )
        else:
            mf_resp.value = "Invitation rejected successfully"
        return mf_resp

    def delete_invitation(self, user_id: str, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL
            + "/"
            + self.INVITATIONS_ENDPOINT
            + "/"
            + user_id
            + "/"
            + domain_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.domains["delete_invitation"], http_resp.status_code
            )
        else:
            mf_resp.value = "Invitation deleted successfully"
        return mf_resp

    # Role management

    def list_available_actions(self, token: str):
        return self.__roles.list_available_actions(
            self.URL, self.DOMAINS_ENDPOINT, token
        )

    def create_role(
        self,
        domain_id: str,
        role_name: str,
        token: str,
        optional_actions: List = None,
        optional_members: List = None,
    ):
        return self.__roles.create_role(
            self.URL,
            self.DOMAINS_ENDPOINT,
            domain_id,
            role_name,
            token,
            optional_actions,
            optional_members,
        )

    def list_roles(self, domain_id: str, query_params: dict, token: str):
        return self.__roles.list_roles(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, query_params, token
        )

    def get_role(self, domain_id: str, role_id: str, token: str):
        return self.__roles.get_role(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, token
        )

    def update_role(self, domain_id: str, role_id: str, role: dict, token: str):
        return self.__roles.update_role(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, role, token
        )

    def delete_role(self, domain_id: str, role_id: str, token: str):
        return self.__roles.delete_role(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, token
        )

    def add_role_actions(
        self, domain_id: str, role_id: str, actions: List, token: str
    ):
        return self.__roles.add_role_actions(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, actions, token
        )

    def list_role_actions(self, domain_id: str, role_id: str, token: str):
        return self.__roles.list_role_actions(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, token
        )

    def delete_role_actions(
        self, domain_id: str, role_id: str, actions: List, token: str
    ):
        return self.__roles.delete_role_actions(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, actions, token
        )

    def delete_all_role_actions(self, domain_id: str, role_id: str, token: str):
        return self.__roles.delete_all_role_actions(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, token
        )

    def add_role_members(
        self, domain_id: str, role_id: str, members: List, token: str
    ):
        return self.__roles.add_role_members(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, members, token
        )

    def list_role_members(
        self, domain_id: str, role_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_role_members(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, query_params, token
        )

    def delete_role_members(
        self, domain_id: str, role_id: str, members: List, token: str
    ):
        return self.__roles.delete_role_members(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, members, token
        )

    def delete_all_role_members(self, domain_id: str, role_id: str, token: str):
        return self.__roles.delete_all_role_members(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, role_id, token
        )

    def list_members(self, domain_id: str, query_params: dict, token: str):
        return self.__roles.list_entity_members(
            self.URL, self.DOMAINS_ENDPOINT, domain_id, query_params, token
        )
