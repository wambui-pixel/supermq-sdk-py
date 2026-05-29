from magistrala import users
from magistrala import clients
from magistrala import messages
from magistrala import channels
from magistrala import groups
from magistrala import boostrap
from magistrala import certs
from magistrala import domains
from magistrala import health
from magistrala import journal
from magistrala import pats
from magistrala import alarms
from magistrala import re
from magistrala import reports

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
        domains_url=default_url,
        journal_url=default_url,
        rules_url=default_url,
        reports_url=default_url,
        auth_url=default_url,
        alarms_url=default_url,
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
        self.domains = domains.Domains(domains_url)
        self.journal = journal.Journal(journal_url)
        self.pats = pats.PATs(auth_url)
        self.alarms = alarms.Alarms(alarms_url)
        self.rules = re.Rules(rules_url)
        self.reports = reports.Reports(reports_url)
        self.health = health.Health(
            users_url=users_url,
            clients_url=clients_url,
            channels_url=clients_url,
            groups_url=groups_url,
            bootstrap_url=bootstrap_url,
            certs_url=certs_url,
            reader_url=reader_url,
            http_adapter_url=http_adapter_url,
            journal_url=journal_url,
            domains_url=domains_url,
            auth_url=auth_url,
        )
        self.version_url = clients_url

    def version(self):
        response = requests.get(self.version_url + "/version")
        return response.json()
