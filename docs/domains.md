<!-- markdownlint-disable -->

# <kbd>module</kbd> `domains`






---

## <kbd>class</kbd> `Domains`
Domains API client. 

Handles domain lifecycle and membership via invitations. Role management is available through the shared Roles helper. 

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

### <kbd>method</kbd> `accept_invitation`

```python
accept_invitation(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `add_role_actions`

```python
add_role_actions(domain_id: str, role_id: str, actions: List, token: str)
```





---

### <kbd>method</kbd> `add_role_members`

```python
add_role_members(domain_id: str, role_id: str, members: List, token: str)
```





---

### <kbd>method</kbd> `create`

```python
create(domain: dict, token: str)
```





---

### <kbd>method</kbd> `create_role`

```python
create_role(
    domain_id: str,
    role_name: str,
    token: str,
    optional_actions: List = None,
    optional_members: List = None
)
```





---

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(domain_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(domain_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_invitation`

```python
delete_invitation(user_id: str, domain_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role`

```python
delete_role(domain_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role_actions`

```python
delete_role_actions(domain_id: str, role_id: str, actions: List, token: str)
```





---

### <kbd>method</kbd> `delete_role_members`

```python
delete_role_members(domain_id: str, role_id: str, members: List, token: str)
```





---

### <kbd>method</kbd> `disable`

```python
disable(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `enable`

```python
enable(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `freeze`

```python
freeze(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `get`

```python
get(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `get_invitation`

```python
get_invitation(user_id: str, domain_id: str, token: str)
```





---

### <kbd>method</kbd> `get_role`

```python
get_role(domain_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list`

```python
list(query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(token: str)
```





---

### <kbd>method</kbd> `list_by_user`

```python
list_by_user(user_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_invitations`

```python
list_invitations(query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_members`

```python
list_members(domain_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(domain_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list_role_members`

```python
list_role_members(domain_id: str, role_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_roles`

```python
list_roles(domain_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_user_invitations`

```python
list_user_invitations(query_params: dict, token: str)
```





---

### <kbd>method</kbd> `reject_invitation`

```python
reject_invitation(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `send_invitation`

```python
send_invitation(invitation: dict, token: str)
```





---

### <kbd>method</kbd> `update`

```python
update(domain: dict, token: str)
```





---

### <kbd>method</kbd> `update_role`

```python
update_role(domain_id: str, role_id: str, role: dict, token: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
