# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    groups_url=default_url + ":9004",
)

token = "<token>"
domain_id = "<domainId>"
group_id = "<groupId>"

resp = mgsdk.groups.create(
    group={"name": "<groupName>"}, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.get(group_id=group_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.get_all(
    query_params={"offset": 0, "limit": 10}, domain_id=domain_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.parents(
    group_id=group_id,
    query_params={"offset": 0, "limit": 10},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.children(
    group_id=group_id,
    query_params={"offset": 0, "limit": 10},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.update(
    group_id=group_id,
    group={"name": "<newName>", "metadata": {"foo": "bar"}},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.members(
    group_id=group_id,
    query_params={"offset": 0, "limit": 10},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.memberships(
    member_id="<memberId>",
    query_params={"offset": 0, "limit": 10},
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.assign(
    group_id=group_id,
    member_id="<memberId>",
    member_type=["<memberType>"],
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.unassign(
    group_id=group_id,
    members_ids="<memberId>",
    domain_id=domain_id,
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.enable(group_id=group_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.disable(group_id=group_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.groups.delete(group_id=group_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)
