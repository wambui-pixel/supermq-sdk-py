<!-- markdownlint-disable -->

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `reports`






---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Reports`
Reports API client. 

Handles on-demand report generation and scheduled report configuration. 

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_config`

```python
add_config(domain_id: str, config: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L338"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_role_actions`

```python
add_role_actions(
    domain_id: str,
    config_id: str,
    role_id: str,
    actions: list,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L384"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_role_members`

```python
add_role_members(
    domain_id: str,
    config_id: str,
    role_id: str,
    members: list,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L278"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_role`

```python
create_role(
    domain_id: str,
    config_id: str,
    role_name: str,
    token: str,
    optional_actions: list = None,
    optional_members: list = None
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L373"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(
    domain_id: str,
    config_id: str,
    role_id: str,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L420"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(
    domain_id: str,
    config_id: str,
    role_id: str,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_config`

```python
delete_config(domain_id: str, config_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role`

```python
delete_role(domain_id: str, config_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L361"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role_actions`

```python
delete_role_actions(
    domain_id: str,
    config_id: str,
    role_id: str,
    actions: list,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L408"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_role_members`

```python
delete_role_members(
    domain_id: str,
    config_id: str,
    role_id: str,
    members: list,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_template`

```python
delete_template(domain_id: str, config_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable_config`

```python
disable_config(domain_id: str, config_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable_config`

```python
enable_config(domain_id: str, config_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `generate`

```python
generate(domain_id: str, report_config: dict, token: str)
```

Generates a report on demand. 

params:  domain_id: str - domain ID  report_config: dict - report request with metrics, time range,  aggregation, and optional file_format  token: str - authorization token 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object with ReportPage 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L67"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_config`

```python
get_config(domain_id: str, config_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L308"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_role`

```python
get_role(domain_id: str, config_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L227"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_template`

```python
get_template(domain_id: str, config_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(domain_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_configs`

```python
list_configs(domain_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L431"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_members`

```python
list_members(domain_id: str, config_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L350"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(domain_id: str, config_id: str, role_id: str, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L396"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_role_members`

```python
list_role_members(
    domain_id: str,
    config_id: str,
    role_id: str,
    query_params: dict,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `list_roles`

```python
list_roles(domain_id: str, config_id: str, query_params: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_config`

```python
update_config(domain_id: str, config: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L317"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_role`

```python
update_role(
    domain_id: str,
    config_id: str,
    role_id: str,
    role: dict,
    token: str
)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_schedule`

```python
update_schedule(domain_id: str, config_id: str, schedule: dict, token: str)
```





---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/reports.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_template`

```python
update_template(domain_id: str, config_id: str, template: dict, token: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
