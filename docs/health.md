<!-- markdownlint-disable -->

# <kbd>module</kbd> `health`






---

## <kbd>class</kbd> `Health`
Health check API client. 

Checks the health of individual Magistrala services. Each service URL is optional; only provided services can be checked. 

### <kbd>method</kbd> `__init__`

```python
__init__(
    users_url: str = '',
    clients_url: str = '',
    channels_url: str = '',
    groups_url: str = '',
    bootstrap_url: str = '',
    certs_url: str = '',
    reader_url: str = '',
    http_adapter_url: str = '',
    journal_url: str = '',
    domains_url: str = '',
    auth_url: str = ''
)
```








---

### <kbd>method</kbd> `check`

```python
check(service: str)
```

Checks the health of the given service. 

params:  service: str - one of: users, clients, channels, groups,  bootstrap, certs, reader, http-adapter, journal, domains, auth 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with HealthInfo dict 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
