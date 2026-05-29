<!-- markdownlint-disable -->

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `roles`






---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Roles`
Shared role management helper used by Clients, Channels, Groups, Domains, and Rules. 




---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L148"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_role_actions`

```python
add_role_actions(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    actions: List,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_role_members`

```python
add_role_members(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    members: List,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_role`

```python
create_role(
    url: str,
    endpoint: str,
    entity_id: str,
    role_name: str,
    token: str,
    optional_actions: List = None,
    optional_members: List = None
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L333"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role`

```python
delete_role(url: str, endpoint: str, entity_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role_actions`

```python
delete_role_actions(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    actions: List,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L302"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role_members`

```python
delete_role_members(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    members: List,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_role`

```python
get_role(url: str, endpoint: str, entity_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(url: str, endpoint: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L362"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_entity_members`

```python
list_entity_members(
    url: str,
    endpoint: str,
    entity_id: str,
    query_params: dict,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L278"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_role_members`

```python
list_role_members(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    query_params: dict,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_roles`

```python
list_roles(
    url: str,
    endpoint: str,
    entity_id: str,
    query_params: dict,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/roles.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_role`

```python
update_role(
    url: str,
    endpoint: str,
    entity_id: str,
    role_id: str,
    role: dict,
    token: str
)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
