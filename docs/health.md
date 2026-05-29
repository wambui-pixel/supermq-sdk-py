<!-- markdownlint-disable -->

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/health.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `health`






---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/health.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Health`
Health check API client. 

Checks the health of individual Magistrala services. Each service URL is optional; only provided services can be checked. 

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/health.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/health.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
