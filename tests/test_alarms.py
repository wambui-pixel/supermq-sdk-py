from magistrala import sdk

import requests_mock

url = "http://localhost"
s = sdk.SDK(alarms_url=url)

alarm = {
    "id": "alarm-id-1",
    "rule_id": "rule-id-1",
    "domain_id": "domain-id-1",
    "status": "active",
    "severity": 1,
    "measurement": "temperature",
    "value": "100",
}

alarms_page = {
    "alarms": [alarm],
    "total": 1,
    "offset": 0,
    "limit": 10,
}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
domain_id = "domain-id-1"
alarm_id = "alarm-id-1"


def test_list_alarms(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/alarms",
        json=alarms_page,
        status_code=200,
    )
    r = s.alarms.list(domain_id=domain_id, query_params={}, token=token)
    assert r.error.status == 0
    assert r.value == alarms_page


def test_list_alarms_bad_request(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/" + domain_id + "/alarms", status_code=400
    )
    r = s.alarms.list(domain_id=domain_id, query_params={}, token=token)
    assert r.error.status == 1
    assert "malformed" in r.error.message


def test_view_alarm(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/alarms/" + alarm_id,
        json=alarm,
        status_code=200,
    )
    r = s.alarms.view(domain_id=domain_id, alarm_id=alarm_id, token=token)
    assert r.error.status == 0
    assert r.value == alarm


def test_view_alarm_not_found(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/" + domain_id + "/alarms/" + alarm_id, status_code=404
    )
    r = s.alarms.view(domain_id=domain_id, alarm_id=alarm_id, token=token)
    assert r.error.status == 1
    assert "does not exist" in r.error.message


def test_update_alarm(requests_mock):
    requests_mock.register_uri(
        "PUT",
        url + "/" + domain_id + "/alarms/" + alarm_id,
        json=alarm,
        status_code=200,
    )
    r = s.alarms.update(domain_id=domain_id, alarm=alarm, token=token)
    assert r.error.status == 0
    assert r.value == alarm


def test_update_alarm_not_found(requests_mock):
    requests_mock.register_uri(
        "PUT", url + "/" + domain_id + "/alarms/" + alarm_id, status_code=404
    )
    r = s.alarms.update(domain_id=domain_id, alarm=alarm, token=token)
    assert r.error.status == 1


def test_delete_alarm(requests_mock):
    requests_mock.register_uri(
        "DELETE",
        url + "/" + domain_id + "/alarms/" + alarm_id,
        status_code=204,
    )
    r = s.alarms.delete(domain_id=domain_id, alarm_id=alarm_id, token=token)
    assert r.error.status == 0


def test_delete_alarm_not_found(requests_mock):
    requests_mock.register_uri(
        "DELETE", url + "/" + domain_id + "/alarms/" + alarm_id, status_code=404
    )
    r = s.alarms.delete(domain_id=domain_id, alarm_id=alarm_id, token=token)
    assert r.error.status == 1
