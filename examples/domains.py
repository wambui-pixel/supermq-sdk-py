# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    domains_url=default_url + ":9003",
)

token = "<token>"
domain_id = "<domainId>"
role_id = "<roleId>"
user_id = "<userId>"

resp = mgsdk.domains.create(
    domain={"name": "<domainName>", "route": "<domainRoute>"}, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.get(domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.list(query_params={"offset": 0, "limit": 10}, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.update(
    domain={"id": domain_id, "name": "<newName>"}, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.enable(domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.disable(domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.freeze(domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.send_invitation(
    invitation={"invitee_user_id": user_id, "domain_id": domain_id, "role_id": role_id},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.get_invitation(user_id=user_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.list_invitations(query_params={"offset": 0, "limit": 10}, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.accept_invitation(domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.reject_invitation(domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.delete_invitation(user_id=user_id, domain_id=domain_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.list_available_actions(token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.create_role(domain_id=domain_id, role_name="<roleName>", token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.list_roles(
    domain_id=domain_id, query_params={"offset": 0, "limit": 10}, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.get_role(domain_id=domain_id, role_id=role_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.delete_role(domain_id=domain_id, role_id=role_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.add_role_actions(
    domain_id=domain_id, role_id=role_id, actions=["read", "write"], token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.domains.add_role_members(
    domain_id=domain_id, role_id=role_id, members=[user_id], token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)
