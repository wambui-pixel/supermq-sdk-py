import requests
from typing import List

from magistrala import response
from magistrala import errors
from magistrala import utils


class PATs:
    """Personal Access Tokens (PATs) API client.

    Handles creating, retrieving, updating, revoking, and managing
    scopes for personal access tokens.
    """

    PATS_ENDPOINT = "pats"

    def __init__(self, url: str):
        self.URL = url

    def create(self, name: str, duration: str, token: str, description: str = ""):
        """Creates a new Personal Access Token.

        params:
            name: str - name of the PAT
            duration: str - validity duration e.g. "24h"
            token: str - authorization token
            description: str - optional description

        returns:
            mf_resp: response.Response - response object with PAT
        """
        payload = {"name": name, "duration": duration}
        if description:
            payload["description"] = description
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.PATS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, pat_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def list(self, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.PATS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["list"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_name(self, pat_id: str, name: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/name",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"name": name},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["update_name"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update_description(self, pat_id: str, description: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/description",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"description": description},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["update_description"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete(self, pat_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["delete"], http_resp.status_code
            )
        else:
            mf_resp.value = "PAT deleted successfully"
        return mf_resp

    def delete_all(self, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL + "/" + self.PATS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["delete_all"], http_resp.status_code
            )
        else:
            mf_resp.value = "PATs deleted successfully"
        return mf_resp

    def reset_secret(self, pat_id: str, duration: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/secret/reset",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"duration": duration},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["reset_secret"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def revoke(self, pat_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/secret/revoke",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["revoke"], http_resp.status_code
            )
        else:
            mf_resp.value = "PAT revoked successfully"
        return mf_resp

    def add_scope(self, pat_id: str, scopes: List, token: str):
        """Adds scopes to a PAT.

        params:
            pat_id: str - PAT ID
            scopes: List - list of scope dicts, each with entity_type,
                domain_id, operation, entity_id fields
            token: str - authorization token

        returns:
            mf_resp: response.Response
        """
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/scope/add",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"scopes": scopes},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["add_scope"], http_resp.status_code
            )
        else:
            mf_resp.value = "Scope added successfully"
        return mf_resp

    def list_scopes(self, pat_id: str, query_params: dict, token: str):
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/scope",
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["list_scopes"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete_scopes(self, pat_id: str, scope_ids: List, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/scope/remove",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"scopes_id": scope_ids},
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["delete_scopes"], http_resp.status_code
            )
        else:
            mf_resp.value = "Scopes removed successfully"
        return mf_resp

    def delete_all_scopes(self, pat_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL + "/" + self.PATS_ENDPOINT + "/" + pat_id + "/scope",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.pats["delete_all_scopes"], http_resp.status_code
            )
        else:
            mf_resp.value = "All scopes deleted successfully"
        return mf_resp
