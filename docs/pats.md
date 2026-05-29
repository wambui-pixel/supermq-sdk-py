<!-- markdownlint-disable -->

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `pats`






---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PATs`
Personal Access Tokens (PATs) API client. 

Handles creating, retrieving, updating, revoking, and managing scopes for personal access tokens. 

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_scope`

```python
add_scope(pat_id: str, scopes: List, token: str)
```

Adds scopes to a PAT. 

params:  pat_id: str - PAT ID  scopes: List - list of scope dicts, each with entity_type,  domain_id, operation, entity_id fields  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(name: str, duration: str, token: str, description: str = '')
```

Creates a new Personal Access Token. 

params:  name: str - name of the PAT  duration: str - validity duration e.g. "24h"  token: str - authorization token  description: str - optional description 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with PAT 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete`

```python
delete(pat_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all`

```python
delete_all(token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L234"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_scopes`

```python
delete_all_scopes(pat_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_scopes`

```python
delete_scopes(pat_id: str, scope_ids: List, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(pat_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list`

```python
list(query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L202"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_scopes`

```python
list_scopes(pat_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset_secret`

```python
reset_secret(pat_id: str, duration: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `revoke`

```python
revoke(pat_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_description`

```python
update_description(pat_id: str, description: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/pats.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_name`

```python
update_name(pat_id: str, name: str, token: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
