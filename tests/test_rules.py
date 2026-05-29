from magistrala import sdk

import requests_mock

url = "http://localhost"
s = sdk.SDK(rules_url=url)

rule = {
    "id": "rule-id-1",
    "name": "temperature-alert",
    "input_channel": "channel-id-1",
    "input_topic": "temperature",
    "logic": {"type": 0, "value": "if value > 100 then alarm end"},
    "status": "enabled",
}

rules_page = {
    "rules": [rule],
    "total": 1,
    "offset": 0,
    "limit": 10,
}

role = {"id": "role-id-1", "name": "viewer"}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
domain_id = "domain-id-1"
rule_id = "rule-id-1"
role_id = "role-id-1"


def test_create_rule(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/rules",
        json=rule,
        status_code=201,
    )
    r = s.rules.create(domain_id=domain_id, rule=rule, token=token)
    assert r.error.status == 0
    assert r.value == rule


def test_create_rule_bad_request(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/" + domain_id + "/rules", status_code=400
    )
    r = s.rules.create(domain_id=domain_id, rule=rule, token=token)
    assert r.error.status == 1


def test_view_rule(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/rules/" + rule_id,
        json=rule,
        status_code=200,
    )
    r = s.rules.view(domain_id=domain_id, rule_id=rule_id, token=token)
    assert r.error.status == 0
    assert r.value == rule


def test_view_rule_not_found(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/" + domain_id + "/rules/" + rule_id, status_code=404
    )
    r = s.rules.view(domain_id=domain_id, rule_id=rule_id, token=token)
    assert r.error.status == 1
    assert "does not exist" in r.error.message


def test_list_rules(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/rules",
        json=rules_page,
        status_code=200,
    )
    r = s.rules.list(domain_id=domain_id, query_params={}, token=token)
    assert r.error.status == 0
    assert r.value == rules_page


def test_update_rule(requests_mock):
    requests_mock.register_uri(
        "PUT",
        url + "/" + domain_id + "/rules/" + rule_id,
        json=rule,
        status_code=200,
    )
    r = s.rules.update(domain_id=domain_id, rule=rule, token=token)
    assert r.error.status == 0


def test_enable_rule(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/rules/" + rule_id + "/enable",
        json=rule,
        status_code=200,
    )
    r = s.rules.enable(domain_id=domain_id, rule_id=rule_id, token=token)
    assert r.error.status == 0


def test_disable_rule(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/rules/" + rule_id + "/disable",
        json=rule,
        status_code=200,
    )
    r = s.rules.disable(domain_id=domain_id, rule_id=rule_id, token=token)
    assert r.error.status == 0


def test_delete_rule(requests_mock):
    requests_mock.register_uri(
        "DELETE",
        url + "/" + domain_id + "/rules/" + rule_id,
        status_code=204,
    )
    r = s.rules.delete(domain_id=domain_id, rule_id=rule_id, token=token)
    assert r.error.status == 0


def test_create_role(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/rules/" + rule_id + "/roles",
        json=role,
        status_code=201,
    )
    r = s.rules.create_role(
        domain_id=domain_id,
        rule_id=rule_id,
        role_name="viewer",
        token=token,
    )
    assert r.error.status == 0


def test_list_roles(requests_mock):
    page = {"roles": [role], "total": 1, "offset": 0, "limit": 10}
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/rules/" + rule_id + "/roles",
        json=page,
        status_code=200,
    )
    r = s.rules.list_roles(
        domain_id=domain_id, rule_id=rule_id, query_params={}, token=token
    )
    assert r.error.status == 0
