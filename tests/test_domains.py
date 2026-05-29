from magistrala import sdk

import requests_mock

s = sdk.SDK(domains_url="http://localhost")

domain = {
    "id": "domain-id-1",
    "name": "test-domain",
    "tags": ["tag1"],
    "metadata": {"type": "test"},
    "status": "enabled",
}

invitation = {
    "invitee_user_id": "user-id-1",
    "domain_id": "domain-id-1",
    "role_id": "role-id-1",
}

role = {
    "id": "role-id-1",
    "name": "viewer",
    "entity_id": "domain-id-1",
}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
url = "http://localhost"
domain_id = "domain-id-1"
role_id = "role-id-1"
user_id = "user-id-1"


def test_create_domain(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/domains", json=domain, status_code=201
    )
    r = s.domains.create(domain=domain, token=token)
    assert r.error.status == 0
    assert r.value == domain


def test_create_domain_conflict(requests_mock):
    requests_mock.register_uri("POST", url + "/domains", status_code=409)
    r = s.domains.create(domain=domain, token=token)
    assert r.error.status == 1
    assert "existing domain name" in r.error.message


def test_get_domain(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/domains/" + domain_id, json=domain, status_code=200
    )
    r = s.domains.get(domain_id=domain_id, token=token)
    assert r.error.status == 0
    assert r.value == domain


def test_get_domain_not_found(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/domains/" + domain_id, status_code=404
    )
    r = s.domains.get(domain_id=domain_id, token=token)
    assert r.error.status == 1
    assert "does not exist" in r.error.message


def test_list_domains(requests_mock):
    page = {"domains": [domain], "total": 1, "offset": 0, "limit": 10}
    requests_mock.register_uri("GET", url + "/domains", json=page, status_code=200)
    r = s.domains.list(query_params={"offset": 0, "limit": 10}, token=token)
    assert r.error.status == 0
    assert r.value == page


def test_update_domain(requests_mock):
    requests_mock.register_uri(
        "PATCH", url + "/domains/" + domain_id, json=domain, status_code=200
    )
    r = s.domains.update(domain=domain, token=token)
    assert r.error.status == 0


def test_enable_domain(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/domains/" + domain_id + "/enable", json=domain, status_code=200
    )
    r = s.domains.enable(domain_id=domain_id, token=token)
    assert r.error.status == 0


def test_disable_domain(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/domains/" + domain_id + "/disable",
        json=domain,
        status_code=200,
    )
    r = s.domains.disable(domain_id=domain_id, token=token)
    assert r.error.status == 0


def test_send_invitation(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/invitations", status_code=201
    )
    r = s.domains.send_invitation(invitation=invitation, token=token)
    assert r.error.status == 0


def test_send_invitation_bad_request(requests_mock):
    requests_mock.register_uri("POST", url + "/invitations", status_code=400)
    r = s.domains.send_invitation(invitation=invitation, token=token)
    assert r.error.status == 1
    assert "malformed" in r.error.message


def test_get_invitation(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/invitations/" + user_id + "/" + domain_id,
        json=invitation,
        status_code=200,
    )
    r = s.domains.get_invitation(user_id=user_id, domain_id=domain_id, token=token)
    assert r.error.status == 0


def test_list_invitations(requests_mock):
    page = {"invitations": [invitation], "total": 1, "offset": 0, "limit": 10}
    requests_mock.register_uri(
        "GET", url + "/invitations", json=page, status_code=200
    )
    r = s.domains.list_invitations(query_params={}, token=token)
    assert r.error.status == 0


def test_accept_invitation(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/invitations/" + domain_id + "/accept", status_code=200
    )
    r = s.domains.accept_invitation(domain_id=domain_id, token=token)
    assert r.error.status == 0


def test_reject_invitation(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/invitations/" + domain_id + "/reject", status_code=200
    )
    r = s.domains.reject_invitation(domain_id=domain_id, token=token)
    assert r.error.status == 0


def test_delete_invitation(requests_mock):
    requests_mock.register_uri(
        "DELETE",
        url + "/invitations/" + user_id + "/" + domain_id,
        status_code=204,
    )
    r = s.domains.delete_invitation(
        user_id=user_id, domain_id=domain_id, token=token
    )
    assert r.error.status == 0


def test_list_available_actions(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/domains/roles/available-actions",
        json={"available_actions": ["read", "write"]},
        status_code=200,
    )
    r = s.domains.list_available_actions(token=token)
    assert r.error.status == 0
    assert "read" in r.value


def test_create_role(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/domains/" + domain_id + "/roles",
        json=role,
        status_code=201,
    )
    r = s.domains.create_role(
        domain_id=domain_id, role_name="viewer", token=token
    )
    assert r.error.status == 0


def test_list_roles(requests_mock):
    page = {"roles": [role], "total": 1, "offset": 0, "limit": 10}
    requests_mock.register_uri(
        "GET",
        url + "/domains/" + domain_id + "/roles",
        json=page,
        status_code=200,
    )
    r = s.domains.list_roles(
        domain_id=domain_id, query_params={}, token=token
    )
    assert r.error.status == 0


def test_get_role(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/domains/" + domain_id + "/roles/" + role_id,
        json=role,
        status_code=200,
    )
    r = s.domains.get_role(domain_id=domain_id, role_id=role_id, token=token)
    assert r.error.status == 0


def test_delete_role(requests_mock):
    requests_mock.register_uri(
        "DELETE",
        url + "/domains/" + domain_id + "/roles/" + role_id,
        status_code=204,
    )
    r = s.domains.delete_role(domain_id=domain_id, role_id=role_id, token=token)
    assert r.error.status == 0


def test_add_role_actions(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/domains/" + domain_id + "/roles/" + role_id + "/actions",
        json={"actions": ["read"]},
        status_code=200,
    )
    r = s.domains.add_role_actions(
        domain_id=domain_id, role_id=role_id, actions=["read"], token=token
    )
    assert r.error.status == 0


def test_add_role_members(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/domains/" + domain_id + "/roles/" + role_id + "/members",
        json={"members": [user_id]},
        status_code=200,
    )
    r = s.domains.add_role_members(
        domain_id=domain_id, role_id=role_id, members=[user_id], token=token
    )
    assert r.error.status == 0
