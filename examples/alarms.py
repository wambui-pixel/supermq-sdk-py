# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    alarms_url=default_url + ":8050",
)

token = "<token>"
domain_id = "<domainId>"
alarm_id = "<alarmId>"

resp = mgsdk.alarms.list(
    domain_id=domain_id,
    query_params={"offset": 0, "limit": 10},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.alarms.view(domain_id=domain_id, alarm_id=alarm_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.alarms.update(
    domain_id=domain_id,
    alarm={"id": alarm_id, "status": "cleared"},
    token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.alarms.delete(domain_id=domain_id, alarm_id=alarm_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)
