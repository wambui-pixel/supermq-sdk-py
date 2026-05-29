from magistrala import sdk

import requests_mock

url = "http://localhost"
s = sdk.SDK(reports_url=url)

report_config = {
    "id": "config-id-1",
    "name": "daily-report",
    "domain_id": "domain-id-1",
    "status": "enabled",
    "metrics": [{"channel_id": "channel-id-1", "name": "temperature"}],
}

report_page = {
    "total": 1,
    "reports": [{"metric": {"channel_id": "channel-id-1"}, "messages": []}],
}

configs_page = {
    "report_configs": [report_config],
    "total": 1,
    "offset": 0,
    "limit": 10,
}

role = {"id": "role-id-1", "name": "viewer"}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
domain_id = "domain-id-1"
config_id = "config-id-1"
role_id = "role-id-1"


def test_generate_report(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/reports",
        json=report_page,
        status_code=200,
    )
    r = s.reports.generate(
        domain_id=domain_id, report_config=report_config, token=token
    )
    assert r.error.status == 0
    assert r.value == report_page


def test_generate_report_bad_request(requests_mock):
    requests_mock.register_uri(
        "POST", url + "/" + domain_id + "/reports", status_code=400
    )
    r = s.reports.generate(
        domain_id=domain_id, report_config=report_config, token=token
    )
    assert r.error.status == 1


def test_add_config(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/reports/configs",
        json=report_config,
        status_code=201,
    )
    r = s.reports.add_config(
        domain_id=domain_id, config=report_config, token=token
    )
    assert r.error.status == 0
    assert r.value == report_config


def test_get_config(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/reports/configs/" + config_id,
        json=report_config,
        status_code=200,
    )
    r = s.reports.get_config(
        domain_id=domain_id, config_id=config_id, token=token
    )
    assert r.error.status == 0
    assert r.value == report_config


def test_get_config_not_found(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/reports/configs/" + config_id,
        status_code=404,
    )
    r = s.reports.get_config(
        domain_id=domain_id, config_id=config_id, token=token
    )
    assert r.error.status == 1


def test_list_configs(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/reports/configs",
        json=configs_page,
        status_code=200,
    )
    r = s.reports.list_configs(
        domain_id=domain_id, query_params={}, token=token
    )
    assert r.error.status == 0
    assert r.value == configs_page


def test_update_config(requests_mock):
    requests_mock.register_uri(
        "PUT",
        url + "/" + domain_id + "/reports/configs/" + config_id,
        json=report_config,
        status_code=200,
    )
    r = s.reports.update_config(
        domain_id=domain_id, config=report_config, token=token
    )
    assert r.error.status == 0


def test_enable_config(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/reports/configs/" + config_id + "/enable",
        json=report_config,
        status_code=200,
    )
    r = s.reports.enable_config(
        domain_id=domain_id, config_id=config_id, token=token
    )
    assert r.error.status == 0


def test_disable_config(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/reports/configs/" + config_id + "/disable",
        json=report_config,
        status_code=200,
    )
    r = s.reports.disable_config(
        domain_id=domain_id, config_id=config_id, token=token
    )
    assert r.error.status == 0


def test_delete_config(requests_mock):
    requests_mock.register_uri(
        "DELETE",
        url + "/" + domain_id + "/reports/configs/" + config_id,
        status_code=204,
    )
    r = s.reports.delete_config(
        domain_id=domain_id, config_id=config_id, token=token
    )
    assert r.error.status == 0


def test_create_role(requests_mock):
    requests_mock.register_uri(
        "POST",
        url + "/" + domain_id + "/reports/configs/" + config_id + "/roles",
        json=role,
        status_code=201,
    )
    r = s.reports.create_role(
        domain_id=domain_id,
        config_id=config_id,
        role_name="viewer",
        token=token,
    )
    assert r.error.status == 0


def test_list_roles(requests_mock):
    page = {"roles": [role], "total": 1, "offset": 0, "limit": 10}
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/reports/configs/" + config_id + "/roles",
        json=page,
        status_code=200,
    )
    r = s.reports.list_roles(
        domain_id=domain_id, config_id=config_id, query_params={}, token=token
    )
    assert r.error.status == 0
