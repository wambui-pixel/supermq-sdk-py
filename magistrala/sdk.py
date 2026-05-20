from magistrala import users
from magistrala import clients
from magistrala import messages
from magistrala import channels
from magistrala import groups
from magistrala import boostrap
from magistrala import certs

import requests

default_url = "http://localhost"


class SDK:
    def __init__(
        self,
        users_url=default_url,
        clients_url=default_url,
        reader_url=default_url,
        http_adapter_url=default_url,
        certs_url=default_url,
        bootstrap_url=default_url,
        groups_url=default_url,
    ):
        self.users = users.Users(users_url)
        self.clients = clients.Clients(clients_url)
        self.messages = messages.Messages(
            adapter_url=http_adapter_url, reader_url=reader_url
        )
        self.channels = channels.Channels(clients_url)
        self.groups = groups.Groups(groups_url)
        self.bootstrap = boostrap.Bootstrap(bootstrap_url)
        self.certs = certs.Certs(certs_url)
        self.version_url = clients_url

    def version(self):
        response = requests.get(self.version_url + "/version")
        return response.json()
