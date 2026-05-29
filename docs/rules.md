<!-- markdownlint-disable -->

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rules`






---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Rules`
Rules Engine API client. 

Manages rules that process incoming messages and trigger outputs such as channel forwards, alarms, and email notifications. 

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(domain_id: str, rule: dict, token: str)
```

Creates a new rule. 

params:  domain_id: str - domain the rule belongs to  rule: dict - rule definition with name, input_channel,  input_topic, logic, outputs, schedule fields  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with Rule 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(domain_id: str, rule_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L286"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L250"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role`

```python
delete_role(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L274"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(domain_id: str, rule_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable(domain_id: str, rule_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_role`

```python
get_role(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list`

```python
list(domain_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(domain_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L336"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_members`

```python
list_members(domain_id: str, rule_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L267"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(domain_id: str, rule_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L305"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L228"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_roles`

```python
list_roles(domain_id: str, rule_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(domain_id: str, rule: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_role`

```python
update_role(domain_id: str, rule_id: str, role_id: str, role: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_schedule`

```python
update_schedule(domain_id: str, rule_id: str, schedule: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_tags`

```python
update_tags(domain_id: str, rule: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/rules.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `view`

```python
view(domain_id: str, rule_id: str, token: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
