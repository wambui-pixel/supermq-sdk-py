from magistrala import sdk

import requests_mock

url = "http://localhost"
s = sdk.SDK(journal_url=url)

journal_entry = {
    "id": "journal-id-1",
    "operation": "create",
    "occurred_at": "2024-01-01T00:00:00Z",
}

journals_page = {
    "journals": [journal_entry],
    "total": 1,
    "offset": 0,
    "limit": 10,
}

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
domain_id = "domain-id-1"
entity_id = "client-id-1"
user_id = "user-id-1"

telemetry = {
    "client_id": entity_id,
    "domain_id": domain_id,
    "subscriptions": 2,
    "inbound_messages": 100,
    "outbound_messages": 50,
    "first_seen": "2024-01-01T00:00:00Z",
    "last_seen": "2024-01-02T00:00:00Z",
}


def test_list_by_entity(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/journal/client/" + entity_id,
        json=journals_page,
        status_code=200,
    )
    r = s.journal.list_by_entity(
        entity_type="client",
        entity_id=entity_id,
        domain_id=domain_id,
        query_params={},
        token=token,
    )
    assert r.error.status == 0
    assert r.value == journals_page


def test_list_by_entity_not_found(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/journal/client/" + entity_id,
        status_code=404,
    )
    r = s.journal.list_by_entity(
        entity_type="client",
        entity_id=entity_id,
        domain_id=domain_id,
        query_params={},
        token=token,
    )
    assert r.error.status == 1


def test_list_by_user(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/journal/user/" + user_id,
        json=journals_page,
        status_code=200,
    )
    r = s.journal.list_by_user(
        user_id=user_id, query_params={}, token=token
    )
    assert r.error.status == 0
    assert r.value == journals_page


def test_list_by_user_not_found(requests_mock):
    requests_mock.register_uri(
        "GET", url + "/journal/user/" + user_id, status_code=404
    )
    r = s.journal.list_by_user(
        user_id=user_id, query_params={}, token=token
    )
    assert r.error.status == 1


def test_client_telemetry(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/journal/client/" + entity_id + "/telemetry",
        json=telemetry,
        status_code=200,
    )
    r = s.journal.client_telemetry(
        client_id=entity_id, domain_id=domain_id, token=token
    )
    assert r.error.status == 0
    assert r.value == telemetry


def test_client_telemetry_not_found(requests_mock):
    requests_mock.register_uri(
        "GET",
        url + "/" + domain_id + "/journal/client/" + entity_id + "/telemetry",
        status_code=404,
    )
    r = s.journal.client_telemetry(
        client_id=entity_id, domain_id=domain_id, token=token
    )
    assert r.error.status == 1
