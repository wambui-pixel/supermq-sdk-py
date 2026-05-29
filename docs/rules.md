<!-- markdownlint-disable -->

# <kbd>module</kbd> `rules`






---

## <kbd>class</kbd> `Rules`
Rules Engine API client. 

Manages rules that process incoming messages and trigger outputs such as channel forwards, alarms, and email notifications. 

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

### <kbd>method</kbd> `add_role_actions`

```python
add_role_actions(
    domain_id: str,
    rule_id: str,
    role_id: str,
    actions: List,
    token: str
)
```





---

### <kbd>method</kbd> `add_role_members`

```python
add_role_members(
    domain_id: str,
    rule_id: str,
    role_id: str,
    members: List,
    token: str
)
```





---

### <kbd>method</kbd> `create`

```python
create(domain_id: str, rule: dict, token: str)
```

Creates a new rule. 

params:  domain_id: str - domain the rule belongs to  rule: dict - rule definition with name, input_channel,  input_topic, logic, outputs, schedule fields  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with Rule 

---

### <kbd>method</kbd> `create_role`

```python
create_role(
    domain_id: str,
    rule_id: str,
    role_name: str,
    token: str,
    optional_actions: List = None,
    optional_members: List = None
)
```





---

### <kbd>method</kbd> `delete`

```python
delete(domain_id: str, rule_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role`

```python
delete_role(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role_actions`

```python
delete_role_actions(
    domain_id: str,
    rule_id: str,
    role_id: str,
    actions: List,
    token: str
)
```





---

### <kbd>method</kbd> `delete_role_members`

```python
delete_role_members(
    domain_id: str,
    rule_id: str,
    role_id: str,
    members: List,
    token: str
)
```





---

### <kbd>method</kbd> `disable`

```python
disable(domain_id: str, rule_id: str, token: str)
```





---

### <kbd>method</kbd> `enable`

```python
enable(domain_id: str, rule_id: str, token: str)
```





---

### <kbd>method</kbd> `get_role`

```python
get_role(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list`

```python
list(domain_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `list_members`

```python
list_members(domain_id: str, rule_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list_role_members`

```python
list_role_members(
    domain_id: str,
    rule_id: str,
    role_id: str,
    query_params: dict,
    token: str
)
```





---

### <kbd>method</kbd> `list_roles`

```python
list_roles(domain_id: str, rule_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `update`

```python
update(domain_id: str, rule: dict, token: str)
```





---

### <kbd>method</kbd> `update_role`

```python
update_role(domain_id: str, rule_id: str, role_id: str, role: dict, token: str)
```





---

### <kbd>method</kbd> `update_schedule`

```python
update_schedule(domain_id: str, rule_id: str, schedule: dict, token: str)
```





---

### <kbd>method</kbd> `update_tags`

```python
update_tags(domain_id: str, rule: dict, token: str)
```





---

### <kbd>method</kbd> `view`

```python
view(domain_id: str, rule_id: str, token: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
