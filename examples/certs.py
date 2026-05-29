# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    certs_url=default_url + ":9019",
)

token = "<token>"
client_id = "<clientId>"

resp = mgsdk.certs.issue(client_id=client_id, valid="8760h", token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.certs.view_by_thing(client_id=client_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.certs.view_by_serial(cert_id="<certSerial>", token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.certs.revoke(client_id=client_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)
