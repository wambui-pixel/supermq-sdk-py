# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    bootstrap_url=default_url + ":9013",
)

token = "<token>"
client_id = "<clientId>"

config = {
    "external_id": "<externalId>",
    "external_key": "<externalKey>",
    "client_id": client_id,
    "name": "<configName>",
}

resp = mgsdk.bootstrap.add(config=config, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.bootstrap.view(client_id=client_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.bootstrap.update(config=config, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.bootstrap.whitelist(config=config, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.bootstrap.bootstrap(
    external_id="<externalId>", external_key="<externalKey>"
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.bootstrap.remove(config_id=client_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)
