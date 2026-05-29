# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    http_adapter_url=default_url,
    reader_url=default_url + ":9011",
)

token = "<token>"
channel_id = "<channelId>"

resp = mgsdk.messages.send(
    channel_id=channel_id,
    msg='[{"bn":"home/","bt":1.276020076001e+09,"bu":"A","bver":5,"n":"voltage","u":"V","v":120.1}]',
    client_key="<clientSecret>",
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.messages.read(
    channel_id=channel_id,
    token=token,
    query_params={"offset": 0, "limit": 10},
)
print(resp.value if resp.error.status == 0 else resp.error.message)
