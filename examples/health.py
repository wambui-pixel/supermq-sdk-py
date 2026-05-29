# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    users_url=default_url + ":9002",
    clients_url=default_url + ":9006",
    reader_url=default_url + ":9011",
    http_adapter_url=default_url,
    certs_url=default_url + ":9019",
    bootstrap_url=default_url + ":9013",
    groups_url=default_url + ":9004",
    domains_url=default_url + ":9003",
    journal_url=default_url + ":9021",
    auth_url=default_url + ":9002",
    alarms_url=default_url + ":8050",
)

for service in ["users", "clients", "reader", "http-adapter", "certs", "bootstrap",
                "groups", "domains", "journal", "auth", "alarms"]:
    resp = mgsdk.health.check(service)
    if resp.error.status == 0:
        print(f"{service}: {resp.value}")
    else:
        print(f"{service}: {resp.error.message}")
