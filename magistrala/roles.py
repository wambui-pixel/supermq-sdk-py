import requests
from typing import List

from magistrala import response
from magistrala import errors
from magistrala import utils


class Roles:
    """Shared role management helper used by Clients, Channels, Groups, Domains, and Rules."""

    def list_available_actions(self, url: str, endpoint: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            url + "/" + endpoint + "/roles/available-actions",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["list_available_actions"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json().get("available_actions", [])
        return mf_resp

    def create_role(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_name: str,
        token: str,
        optional_actions: List = None,
        optional_members: List = None,
    ):
        payload = {"role_name": role_name}
        if optional_actions:
            payload["optional_actions"] = optional_actions
        if optional_members:
            payload["optional_members"] = optional_members
        mf_resp = response.Response()
        http_resp = requests.post(
            url + "/" + endpoint + "/" + entity_id + "/roles",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["create_role"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list_roles(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        query_params: dict,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.get(
            url + "/" + endpoint + "/" + entity_id + "/roles",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["list_roles"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_role(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.get(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["get_role"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_role(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        role: dict,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.put(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id,
            headers=utils.construct_header(token, utils.CTJSON),
            json=role,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["update_role"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete_role(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.delete(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["delete_role"], http_resp.status_code
            )
        else:
            mf_resp.value = "Role deleted successfully"
        return mf_resp

    def add_role_actions(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        actions: List,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id + "/actions",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"actions": actions},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["add_role_actions"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json().get("actions", [])
        return mf_resp

    def list_role_actions(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.get(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id + "/actions",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["list_role_actions"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json().get("actions", [])
        return mf_resp

    def delete_role_actions(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        actions: List,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            url
            + "/"
            + endpoint
            + "/"
            + entity_id
            + "/roles/"
            + role_id
            + "/actions/delete",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"actions": actions},
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["delete_role_actions"], http_resp.status_code
            )
        else:
            mf_resp.value = "Role actions deleted successfully"
        return mf_resp

    def delete_all_role_actions(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            url
            + "/"
            + endpoint
            + "/"
            + entity_id
            + "/roles/"
            + role_id
            + "/actions/delete-all",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["delete_all_role_actions"], http_resp.status_code
            )
        else:
            mf_resp.value = "All role actions deleted successfully"
        return mf_resp

    def add_role_members(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        members: List,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id + "/members",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"members": members},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["add_role_members"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json().get("members", [])
        return mf_resp

    def list_role_members(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        query_params: dict,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.get(
            url + "/" + endpoint + "/" + entity_id + "/roles/" + role_id + "/members",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["list_role_members"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete_role_members(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        members: List,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            url
            + "/"
            + endpoint
            + "/"
            + entity_id
            + "/roles/"
            + role_id
            + "/members/delete",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"members": members},
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["delete_role_members"], http_resp.status_code
            )
        else:
            mf_resp.value = "Role members deleted successfully"
        return mf_resp

    def delete_all_role_members(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        role_id: str,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            url
            + "/"
            + endpoint
            + "/"
            + entity_id
            + "/roles/"
            + role_id
            + "/members/delete-all",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["delete_all_role_members"], http_resp.status_code
            )
        else:
            mf_resp.value = "All role members deleted successfully"
        return mf_resp

    def list_entity_members(
        self,
        url: str,
        endpoint: str,
        entity_id: str,
        query_params: dict,
        token: str,
    ):
        mf_resp = response.Response()
        http_resp = requests.get(
            url + "/" + endpoint + "/" + entity_id + "/roles/members",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.roles["list_entity_members"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
