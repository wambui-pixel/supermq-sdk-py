# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    journal_url=default_url + ":9021",
)

token = "<token>"
domain_id = "<domainId>"
client_id = "<clientId>"
user_id = "<userId>"

resp = mgsdk.journal.list_by_entity(
    entity_type="client",
    entity_id=client_id,
    domain_id=domain_id,
    query_params={"offset": 0, "limit": 10},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.journal.list_by_user(
    user_id=user_id,
    query_params={"offset": 0, "limit": 10},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.journal.client_telemetry(
    client_id=client_id, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)
