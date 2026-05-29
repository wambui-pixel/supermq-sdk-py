# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    clients_url=default_url + ":9006",
)

token = "<token>"
domain_id = "<domainId>"
channel_id = "<channelId>"
client_id = "<clientId>"

resp = mgsdk.channels.create(
    channel={"name": "<channelName>"}, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.create_bulk(
    channels=[{"name": "<channelName>"}, {"name": "<channelName2>"}],
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.get(channel_id=channel_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.get_all(
    query_params={"offset": 0, "limit": 10}, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.get_by_thing(
    client_id=client_id,
    query_params={"offset": 0, "limit": 10},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.update(
    channel_id=channel_id,
    channel={"name": "<newName>"},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.update_tags(
    channel_id=channel_id,
    channel={"tags": ["tag1", "tag2"]},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.enable(channel_id=channel_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.disable(channel_id=channel_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.delete(channel_id=channel_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.connect_client(
    client_id=client_id, channel_id=channel_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.disconnect_client(
    client_id=client_id, channel_id=channel_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.set_parent_group(
    channel_id=channel_id, group_id="<groupId>", domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.delete_parent_group(
    channel_id=channel_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.channels.identify_thing(client_key="<clientSecret>")
print(resp.value if resp.error.status == 0 else resp.error.message)
