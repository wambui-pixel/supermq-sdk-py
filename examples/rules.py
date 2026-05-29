# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    rules_url=default_url + ":9008",
)

token = "<token>"
domain_id = "<domainId>"
rule_id = "<ruleId>"

resp = mgsdk.rules.create(
    domain_id=domain_id,
    rule={
        "name": "<ruleName>",
        "input_channel": "<channelId>",
        "logic": {"type": "mpl", "value": "<script>"},
        "output_channel": "<channelId>",
    },
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.view(domain_id=domain_id, rule_id=rule_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.list(
    domain_id=domain_id, query_params={"offset": 0, "limit": 10}, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.update(
    domain_id=domain_id,
    rule={"id": rule_id, "name": "<newName>"},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.update_tags(
    domain_id=domain_id,
    rule={"id": rule_id, "tags": ["tag1", "tag2"]},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.enable(domain_id=domain_id, rule_id=rule_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.disable(domain_id=domain_id, rule_id=rule_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.rules.delete(domain_id=domain_id, rule_id=rule_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)
