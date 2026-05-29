# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    clients_url=default_url + ":9006",
)

token = "<token>"
domain_id = "<domainId>"
client_id = "<clientId>"
client_id2 = "<clientId2>"
channel_id = "<channelId>"
channel_id2 = "<channelId2>"

resp = mgsdk.clients.create(
    client={"name": "<clientName>"}, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.create_bulk(
    clients=[{"name": "<clientName>"}, {"name": "<clientName2>"}],
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.get(client_id=client_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.get_all(
    query_params={"offset": 0, "limit": 10}, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.get_by_channel(
    channel_id=channel_id,
    query_params={"offset": 0, "limit": 10},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.update(
    client_id=client_id,
    client={"name": "<newName>"},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.update_client_secret(
    client_id=client_id,
    client={"credentials": {"secret": "<newSecret>"}},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.update_client_tags(
    client_id=client_id,
    client={"tags": ["tag1", "tag2"]},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.enable(client_id=client_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.disable(client_id=client_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.delete(client_id=client_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.connect(
    client_id=client_id, channel_id=channel_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.disconnect(
    client_id=client_id, channel_id=channel_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.connects(
    client_ids=[client_id, client_id2],
    channel_ids=[channel_id, channel_id2],
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.disconnects(
    client_ids=[client_id, client_id2],
    channel_ids=[channel_id, channel_id2],
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.set_parent_group(
    client_id=client_id, group_id="<groupId>", domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.clients.delete_parent_group(
    client_id=client_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)
