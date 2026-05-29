from magistrala import sdk

import requests_mock

url = "http://localhost"

health_info = {
    "status": "pass",
    "version": "0.14.0",
    "commit": "abc123",
    "description": "clients service",
    "build_time": "2024-01-01T00:00:00Z",
    "instance_id": "inst-1",
}

s = sdk.SDK(
    users_url=url,
    clients_url=url,
    reader_url=url,
    http_adapter_url=url,
    certs_url=url,
    bootstrap_url=url,
    groups_url=url,
    domains_url=url,
    journal_url=url,
    auth_url=url,
    alarms_url=url,
)


def test_health_check_users(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/health", json=health_info, status_code=200
    )
    r = s.health.check("users")
    assert r.error.status == 0
    assert r.value["status"] == "pass"


def test_health_check_clients(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/health", json=health_info, status_code=200
    )
    r = s.health.check("clients")
    assert r.error.status == 0


def test_health_check_unknown_service():
    r = s.health.check("unknown-service")
    assert r.error.status == 1
    assert "Unknown or unconfigured service" in r.error.message


def test_health_check_service_down(requests_mock):
    requests_mock.register_uri("GET", url + "/health", status_code=500)
    r = s.health.check("users")
    assert r.error.status == 1
