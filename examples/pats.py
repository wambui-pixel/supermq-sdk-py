# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    auth_url=default_url + ":9002",
)

token = "<token>"
pat_id = "<patId>"

resp = mgsdk.pats.create(
    name="<patName>",
    duration=3600,
    token=token,
    description="<description>",
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.get(pat_id=pat_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.list(query_params={"offset": 0, "limit": 10}, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.update_name(pat_id=pat_id, name="<newName>", token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.update_description(
    pat_id=pat_id, description="<newDescription>", token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.reset_secret(pat_id=pat_id, duration=7200, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.revoke(pat_id=pat_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.add_scope(
    pat_id=pat_id,
    scopes=[{"optional_domain_id": "<domainId>", "entity_type": "client", "operation": "read"}],
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.list_scopes(pat_id=pat_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.delete_scopes(
    pat_id=pat_id, scope_ids=["<scopeId>"], token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.delete_all_scopes(pat_id=pat_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.delete(pat_id=pat_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.pats.delete_all(token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)
