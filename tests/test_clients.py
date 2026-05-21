from magistrala import sdk

import requests_mock

s = sdk.SDK()

client = {
  "id": "35ad0272-94bb-4701-9785-ff32334327a0",
  "name": "client",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "edc876eb-27e2-4bc9-8599-4faf21d2a12f",
  "credentials": {
    "identity": "clientidentity",
    "secret": "f002d93b-fa40-435e-b9d9-37f991e47e9f"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled"
}
clients = [{
  "id": "4e5532c0-cf92-4ef3-ab7b-65ee30151c99",
  "name": "client1",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "edc876eb-27e2-4bc9-8599-4faf21d2a12f",
  "credentials": {
    "identity": "clientidentity",
    "secret": "47749f5e-1e32-4834-9a1d-2d38871d4e1e"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled"
}, {
  "id": "53ed347d-f277-4e2b-9ee1-442389ad1a9a",
  "name": "client2",
  "tags": [
    "tag1",
    "tag2"
  ],
  "owner": "edc876eb-27e2-4bc9-8599-4faf21d2a12f",
  "credentials": {
    "identity": "clientidentity",
    "secret": "566eff24-0b55-4033-9ab1-b4df0d9a3266"
  },
  "metadata": {
    "domain": "example.com"
  },
  "status": "enabled"
}]
client_id = "123-456-789"
client_id1 = "123-223-333"
channel_id = "654-654-654"
channel_id1 = "654-654-654"
user_id= "123-679-773"
action= "m_read"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
url = "http://localhost"
params = None
access_request= {
    "subject": "123-456-789",
    "object": "654-654-654",
    "action": "m_read",
    "entity_type": "group"
}
policies= {
  "policies": [
    {
      "owner_id": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
      "subject": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
      "object": "bb7edb32-2eac-4aad-aebe-ed96fe073879",
      "actions": [
        "m_write",
        "g_add"
      ],
      "created_at": "2019-11-26 13:31:52",
      "updated_at": "2019-11-26 13:31:52"
    }
  ],
  "total": 1,
  "offset": 0,
  "limit": 10
}

def test_create_client(requests_mock):
    requests_mock.register_uri("POST", url + "/clients", headers={"location": "/clients/" + client["id"]}, json=client, status_code=201)
    r = s.clients.create(client=client, token=token)
    assert r.error.status == 0
    assert client == r.value

def test_create_existing_client(requests_mock):
    requests_mock.register_uri("POST", url + "/clients", headers={"location": "/clients/" + client_id}, status_code=409)
    r = s.clients.create(client=client, token=token)
    assert r.error.status == 1
    assert r.error.message == "Entity already exist."

def test_create_bulk_clients(requests_mock):
    requests_mock.register_uri("POST", url + "/clients/bulk", json=clients, status_code=200)
    r = s.clients.create_bulk(clients=clients, token=token)
    assert r.error.status == 0
    assert clients == r.value

def test_create_bulk_clients_missing_token(requests_mock):
    requests_mock.register_uri("POST", url + "/clients/bulk", json=[client_id, client_id1], headers={"location": "/clients/" + client_id}, status_code=401)
    r = s.clients.create_bulk(clients=clients, token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_get_client(requests_mock):
    requests_mock.register_uri("GET", url + "/clients/" + client_id, json=client, status_code=200)
    r = s.clients.get(client_id=client_id, token=token)
    assert r.error.status == 0
    assert client == r.value

def test_get_client_malformed_query(requests_mock):
    requests_mock.register_uri("GET", url + "/clients/" + client_id, json=client, status_code=400)
    r = s.clients.get(client_id=client_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed query parameters."

def test_get_all_clients(requests_mock):
    requests_mock.register_uri("GET", url + "/clients", json=[client_id, client_id1], status_code=200)
    r = s.clients.get_all(token=token, query_params=params)
    assert r.error.status == 0
    assert [client_id, client_id1] == r.value

def test_get_all_client_does_not_exist(requests_mock):
    requests_mock.register_uri("GET", url + "/clients", json=[client_id, client_id1], status_code=404)
    r = s.clients.get_all(token=token, query_params=params)
    assert r.error.status == 1
    assert r.error.message == "Client does not exist."

def test_get_by_channel(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id + "/clients", json=channel_id, headers={"Authorization": "/channels/" + channel_id + "/clients"}, status_code=200)
    r = s.clients.get_by_channel(channel_id=channel_id, query_params=params, token=token)
    assert r.error.status == 0
    assert channel_id == r.value

def test_get_by_channel_missing_token(requests_mock):
    requests_mock.register_uri("GET", url + "/channels/" + channel_id + "/clients", json=channel_id, headers={"Authorization": "/channels/" + channel_id + "/clients"}, status_code=401)
    r = s.clients.get_by_channel(channel_id=channel_id, query_params=params, token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_client(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"], json=client, status_code=200)
    r = s.clients.update(client_id=client["id"], token=token, client=client)
    assert r.error.status == 0
    assert client== r.value

def test_update_client_bad_json(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"], json=client, status_code=404)
    r = s.clients.update(client_id=client["id"], token=token, client=client)
    assert r.error.status == 1
    assert r.error.message == "Client does not exist."

def test_update_client_secret(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"] + "/secret", json=client, status_code=200)
    r = s.clients.update_client_secret(client_id=client["id"], token=token, client=client)
    assert r.error.status == 0
    assert client== r.value

def test_update_client_secret_bad_token(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"] + "/secret", json=client, status_code=401)
    r = s.clients.update_client_secret(client_id=client["id"], token=token, client=client)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_client_tags(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"] + "/tags", json=client, status_code=200)
    r = s.clients.update_client_tags(client_id=client["id"], token=token, client=client)
    assert r.error.status == 0
    assert client== r.value

def test_update_client_tags_bad_token(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"] + "/tags", json=client, status_code=401)
    r = s.clients.update_client_tags(client_id=client["id"], token=token, client=client)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_update_client_owner(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"] + "/owner", json=client, status_code=200)
    r = s.clients.update_client_owner(client_id=client["id"], token=token, client=client)
    assert r.error.status == 0
    assert client== r.value

def test_update_client_owner_bad_token(requests_mock):
    requests_mock.register_uri("PATCH", url + "/clients/" + client["id"] + "/owner", json=client, status_code=401)
    r = s.clients.update_client_owner(client_id=client["id"], token=token, client=client)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_disable_client(requests_mock):
    requests_mock.register_uri("POST", url + "/clients/" + client["id"] + "/disable", status_code=200)
    r = s.clients.disable(client_id=client["id"], token=token)
    assert r.error.status == 0

def test_disable_bad_client_id(requests_mock):
    requests_mock.register_uri("POST", url + "/clients/" + client["id"] + "/disable", status_code=400)
    r = s.clients.disable(client_id=client["id"], token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed due to malformed client's ID."

def test_connect_client(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=201)
    r = s.clients.connect(channel_id=channel_id, client_id=client_id, token=token, action=["m_read"])
    assert r.error.status == 0
    assert r.value == "connected"

def test_connects_clients(requests_mock):
    requests_mock.register_uri("POST", url + "/connect", json=policies, status_code=201)
    r = s.clients.connects(channel_ids=[channel_id], client_ids=[client_id, client_id1], token=token, actions=["m_read"])
    assert r.error.status == 0    
    
def test_connects_clients_non_existing_entity(requests_mock):
    requests_mock.register_uri("POST", url + "/connect", status_code=400)
    r = s.clients.connects(channel_ids=[channel_id], client_ids=[client_id, client_id1], token=token, actions=["m_read"])
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."

def test_connect_non_existing_entity(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=404)
    r = s.clients.connect(channel_id=channel_id, client_id=client_id, token=token, action="m_read")
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."

def test_disconnect_client(requests_mock):
    requests_mock.register_uri("DELETE", url + "/policies" + "/" + client_id + "/" + channel_id, status_code=204)
    r = s.clients.disconnect(channel_id=channel_id, client_id=client_id, token=token)
    assert r.error.status == 0
    
def test_disconnect_client_or_channel_does_not_exist(requests_mock):
    requests_mock.register_uri("DELETE", url + "/policies" + "/" + client_id + "/" + channel_id, status_code=404)
    r = s.clients.disconnect(channel_id=channel_id, client_id=client_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Channel or client does not exist."

def test_disconnects(requests_mock):
    requests_mock.register_uri("POST", url + "/disconnect", status_code=204)
    r = s.clients.disconnects(channel_ids=[channel_id], client_ids=[client_id, client_id1], token=token)
    assert r.error.status == 0

def test_disconnects_bad_json(requests_mock):
    requests_mock.register_uri("POST", url + "/disconnect", status_code=404)
    r = s.clients.disconnects(channel_ids=[channel_id], client_ids=[client_id, client_id1], token=token)
    assert r.error.status == 1
    assert r.error.message == "Channel or client does not exist."

def test_share_client(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=201)
    r = s.clients.share_client(channel_id=channel_id, user_id=user_id, actions= action, token=token)
    assert r.error.status == 0

def test_share_client_bad_token(requests_mock):
    requests_mock.register_uri("POST", url + "/policies", status_code=400)
    r = s.clients.share_client(channel_id=channel_id, user_id=user_id, actions= action, token=token)
    assert r.error.status == 1
    assert r.error.message == "A non-existent entity request."
    
def test_authorise_client(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/object/access", status_code=200)
    r = s.clients.authorise_client(access_request=access_request , token=token)
    assert r.error.status == 0

def test_authorise_client_bad_token(requests_mock):
    requests_mock.register_uri("POST", url + "/channels/object/access", status_code=403)
    r = s.clients.authorise_client(access_request=access_request , token=token)
    assert r.error.status == 1
    assert r.error.message == "False"
