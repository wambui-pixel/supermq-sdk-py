from magistrala import sdk

import requests_mock

url = "http://localhost"
s = sdk.SDK(auth_url=url)

pat = {
    "id": "pat-id-1",
    "name": "my-token",
    "description": "test token",
    "duration": "24h",
    "status": "active",
}

pats_page = {
    "pats": [pat],
    "total": 1,
    "offset": 0,
    "limit": 10,
}

scope = {
    "entity_type": "clients",
    "domain_id": "domain-id-1",
    "operation": "read",
    "entity_id": "client-id-1",
}

scopes_page = {
    "scopes": [scope],
    "total": 1,
    "offset": 0,
    "limit": 10,
}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
pat_id = "pat-id-1"


def test_create_pat(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/pats", json=pat, status_code=201
    )
    r = s.pats.create(name="my-token", duration="24h", token=token)
    assert r.error.status == 0
    assert r.value == pat


def test_create_pat_bad_request(requests_mock):
    requests_mock.register_uri("POST", url + "/pats", status_code=400)
    r = s.pats.create(name="my-token", duration="24h", token=token)
    assert r.error.status == 1
    assert "malformed" in r.error.message


def test_get_pat(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/pats/" + pat_id, json=pat, status_code=200
    )
    r = s.pats.get(pat_id=pat_id, token=token)
    assert r.error.status == 0
    assert r.value == pat


def test_get_pat_not_found(requests_mock):
    requests_mock.register_uri("GET", url + "/pats/" + pat_id, status_code=404)
    r = s.pats.get(pat_id=pat_id, token=token)
    assert r.error.status == 1
    assert "does not exist" in r.error.message


def test_list_pats(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/pats", json=pats_page, status_code=200
    )
    r = s.pats.list(query_params={"offset": 0, "limit": 10}, token=token)
    assert r.error.status == 0
    assert r.value == pats_page


def test_update_pat_name(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/pats/" + pat_id + "/name", json=pat, status_code=200
    )
    r = s.pats.update_name(pat_id=pat_id, name="new-name", token=token)
    assert r.error.status == 0


def test_update_pat_description(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/pats/" + pat_id + "/description", json=pat, status_code=200
    )
    r = s.pats.update_description(
        pat_id=pat_id, description="new description", token=token
    )
    assert r.error.status == 0


def test_delete_pat(requests_mock):
    requests_mock.register_uri("DELETE", url + "/pats/" + pat_id, status_code=204)
    r = s.pats.delete(pat_id=pat_id, token=token)
    assert r.error.status == 0


def test_delete_all_pats(requests_mock):
    requests_mock.register_uri("DELETE", url + "/pats", status_code=204)
    r = s.pats.delete_all(token=token)
    assert r.error.status == 0


def test_reset_secret(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/pats/" + pat_id + "/secret/reset", json=pat, status_code=200
    )
    r = s.pats.reset_secret(pat_id=pat_id, duration="48h", token=token)
    assert r.error.status == 0


def test_revoke_pat(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/pats/" + pat_id + "/secret/revoke", status_code=200
    )
    r = s.pats.revoke(pat_id=pat_id, token=token)
    assert r.error.status == 0


def test_add_scope(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/pats/" + pat_id + "/scope/add", status_code=200
    )
    r = s.pats.add_scope(pat_id=pat_id, scopes=[scope], token=token)
    assert r.error.status == 0


def test_list_scopes(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/pats/" + pat_id + "/scope", json=scopes_page, status_code=200
    )
    r = s.pats.list_scopes(pat_id=pat_id, query_params={}, token=token)
    assert r.error.status == 0
    assert r.value == scopes_page


def test_delete_scopes(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/pats/" + pat_id + "/scope/remove", status_code=204
    )
    r = s.pats.delete_scopes(pat_id=pat_id, scope_ids=["scope-1"], token=token)
    assert r.error.status == 0


def test_delete_all_scopes(requests_mock):
    requests_mock.register_uri(
        "DELETE", url + "/pats/" + pat_id + "/scope", status_code=204
    )
    r = s.pats.delete_all_scopes(pat_id=pat_id, token=token)
    assert r.error.status == 0
