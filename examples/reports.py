# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    reports_url=default_url + ":9012",
)

token = "<token>"
domain_id = "<domainId>"
config_id = "<configId>"

report_config = {
    "name": "<configName>",
    "metrics": [{"channel_id": "<channelId>", "name": "<metricName>"}],
}

resp = mgsdk.reports.generate(
    domain_id=domain_id, report_config=report_config, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.add_config(
    domain_id=domain_id, config=report_config, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.get_config(
    domain_id=domain_id, config_id=config_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.list_configs(
    domain_id=domain_id, query_params={"offset": 0, "limit": 10}, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.update_config(
    domain_id=domain_id,
    config={"id": config_id, "name": "<newName>"},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.enable_config(
    domain_id=domain_id, config_id=config_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.disable_config(
    domain_id=domain_id, config_id=config_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.reports.delete_config(
    domain_id=domain_id, config_id=config_id, token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)
