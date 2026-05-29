<!-- markdownlint-disable -->

# <kbd>module</kbd> `journal`






---

## <kbd>class</kbd> `Journal`
Journal API client. 

Retrieves audit/activity logs for entities and users, and client telemetry. 

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

### <kbd>method</kbd> `client_telemetry`

```python
client_telemetry(client_id: str, domain_id: str, token: str)
```

Retrieves telemetry data for a client. 

params:  client_id: str - unique client ID  domain_id: str - domain the client belongs to  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with ClientTelemetry 

---

### <kbd>method</kbd> `list_by_entity`

```python
list_by_entity(
    entity_type: str,
    entity_id: str,
    domain_id: str,
    query_params: dict,
    token: str
)
```

Retrieves journal entries for a domain entity (client, channel, group). 

params:  entity_type: str - e.g. "client", "channel", "group"  entity_id: str - unique entity ID  domain_id: str - domain the entity belongs to  query_params: dict - pagination/filter params  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with JournalsPage 

---

### <kbd>method</kbd> `list_by_user`

```python
list_by_user(user_id: str, query_params: dict, token: str)
```

Retrieves journal entries for a user. 

params:  user_id: str - unique user ID  query_params: dict - pagination/filter params  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with JournalsPage 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
