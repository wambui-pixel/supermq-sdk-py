<!-- markdownlint-disable -->

# <kbd>module</kbd> `clients`






---

## <kbd>class</kbd> `Clients`
Clients API client. 

Clients API is used for creating and managing clients. It is used for creating new clients, creating multiple clients getting client information, updating client information, disabling  and enabling clients ,and connecting and disconnecting clients. 



**Attributes:**
 
 - <b>`URL`</b>:  str - URL of the Clients API 
 - <b>`CLIENTS_ENDPOINT`</b>:  str - Clients API endpoint 

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

### <kbd>method</kbd> `add_role_actions`

```python
add_role_actions(
    domain_id: str,
    client_id: str,
    role_id: str,
    actions: list,
    token: str
)
```





---

### <kbd>method</kbd> `add_role_members`

```python
add_role_members(
    domain_id: str,
    client_id: str,
    role_id: str,
    members: list,
    token: str
)
```





---

### <kbd>method</kbd> `authorise_thing`

```python
authorise_thing(access_request: dict, token: str)
```

Authorises client. 

Creates policies for a client as a subject over a channel which is the object.  It authorizes the client to perform some actions over the channel. 

params: 

 access_request: dict - access request information for example:  {  "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",  "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",  "actions": "m_write"  "entity_type": "group"  }  token: str - token used for authorising client  



**returns:**
 
 - <b>`mf_resp`</b>:  "True" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> access_request = {     ...     "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",     ...     "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",     ...     "actions": "m_write"     ...     "entity_type": "group"     ... }     >>> mf_resp = mfsdk.clients.authorise_thing(access_request)     >>> mf_resp 

---

### <kbd>method</kbd> `connect`

```python
connect(client_id: str, channel_id: str, action: str, token: str)
```

Connects client and channel. 

Connects a client and channel with provided client ID as the subject, channel ID as the object, action that the client can partake in and a valid token. 

params:  client_id: str - ID of the client  channel_id: str - ID of the channel  action: str - action for example: "m_write"  token: str - token used for connecting client and channel  



**returns:**
 
 - <b>`mf_resp`</b>:  "connected" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> action = "m_write"     >>> mf_resp = mfsdk.clients.connect(client_id, channel_id, action)     >>> mf_resp 

---

### <kbd>method</kbd> `connects`

```python
connects(client_ids: list, channel_ids: list, actions: list, token: str)
```

Connects clients and channels.  

Connects multiple clients and channels with provided client IDs  as the subjects, channel IDs as the objects, actions that the  client can partake in and a valid token. 

params:  client_ids: list - list of client IDs  channel_ids: list - list of channel IDs  actions: list - list of actions for example:   ["m_write", "m_read"]  token: str - token used for connecting clients and channels  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> actions = ["m_write", "m_read"]     >>> mf_resp = mfsdk.clients.connects(client_ids, channel_ids, actions)     >>> mf_resp             

---

### <kbd>method</kbd> `create`

```python
create(client: dict, token: str)
```

Creates client entity in the database.  

Creates a new client with provided client information. If token is provided, it will be used to create a new client 

params:  client: dict - client information for example:  {  "name": "client1"  }  token: str - token used for creating a new client  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client = {     ...     "name": "client1",     ...  }     >>> mf_resp = mfsdk.clients.create(client)     >>> mf_resp             

---

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(clients: list, token: str)
```

Creates multiple clients in bulk.  

Creates multiple new clients with provided clients information. If a token is provided, it will be used to create the new clients. 

params:  clients: list - a list of clients with theri information for example:  [  {"name": "client2"},   {"name": "client3"},   {"name": "client4"}  ]  token: str - token used for creating the new clients.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> clients = [     ...     {"name": "client2"},      ...     {"name": "client3"},      ...     {"name": "client4"}     ... ]     >>> mf_resp = mfsdk.clients.create_bulk(clients)     >>> mf_resp             

---

### <kbd>method</kbd> `create_role`

```python
create_role(
    domain_id: str,
    client_id: str,
    role_name: str,
    token: str,
    optional_actions: list = None,
    optional_members: list = None
)
```





---

### <kbd>method</kbd> `delete`

```python
delete(client_id: str, domain_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(
    domain_id: str,
    client_id: str,
    role_id: str,
    token: str
)
```





---

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(
    domain_id: str,
    client_id: str,
    role_id: str,
    token: str
)
```





---

### <kbd>method</kbd> `delete_parent_group`

```python
delete_parent_group(domain_id: str, client_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role`

```python
delete_role(domain_id: str, client_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role_actions`

```python
delete_role_actions(
    domain_id: str,
    client_id: str,
    role_id: str,
    actions: list,
    token: str
)
```





---

### <kbd>method</kbd> `delete_role_members`

```python
delete_role_members(
    domain_id: str,
    client_id: str,
    role_id: str,
    members: list,
    token: str
)
```





---

### <kbd>method</kbd> `disable`

```python
disable(client_id: str, token: str)
```

Deletes a client entity from the database. 

Deletes a client with provided client ID and valid token. 

params:  client_id: str - ID of the client  token: str - token used for deleting client  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```                       >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> mf_resp = mfsdk.clients.disable(client_id)     >>> mf_resp         

---

### <kbd>method</kbd> `disconnect`

```python
disconnect(client_id: str, channel_id: str, token: str)
```

Disconnects client and channel. 

Disconnects a client and channel with provided client ID as the subject,   channel ID as the object and a valid token. 

params:  client_id: str - ID of the client  channel_id: str - ID of the channel  token: str - token used for disconnecting client and channel  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> mf_resp = mfsdk.clients.disconnect(client_id, channel_id)     >>> mf_resp 

---

### <kbd>method</kbd> `disconnects`

```python
disconnects(client_ids: list, channel_ids: list, token: str)
```

Disconnect clients and channels. 

Disconnects multiple clients and channels with provided client IDs  as the subjects, channel IDs as the objects and a valid token. 

params:  client_ids: list - list of client IDs  channel_ids: list - list of channel IDs  token: str - token used for disconnecting clients and channels 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> mf_resp = mfsdk.clients.disconnects(client_ids, channel_ids)     >>> mf_resp 

---

### <kbd>method</kbd> `enable`

```python
enable(client_id: str, domain_id: str, token: str)
```





---

### <kbd>method</kbd> `get`

```python
get(client_id: str, token: str)
```

Gets a client entity. 

Provides information about a client with provided client ID and token. Information about a client is provided in a JSON format and includes the name its owner, secret,tags and status. 

params:  client_id: str - ID of the client  token: str - token used for getting client information 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```               >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> mf_resp = mfsdk.clients.get(client_id)     >>> mf_resp         

---

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all clients from database. 

Provides information about all clients in a JSON format. It is controlled by a set of query parameters and a valid token. 

params:  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10  }  where offset is the number of clients to skip and limit is the maximum  token: str - token used for getting all clients information 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```                   >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> query_params = {     ...     "offset": 0,     ...     "limit": 10     ... }     >>> mf_resp = mfsdk.clients.get_all(query_params)     >>> mf_resp         

---

### <kbd>method</kbd> `get_by_channel`

```python
get_by_channel(channel_id: str, query_params: dict, token: str)
```

Gets all clients to which a specific client is connected to. 

Provides a list of all clients that are connected to a specific channel when given a channel ID and valid token. 

params:  channel_id: str - ID of the channel  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10  }  where offset is the number of clients to skip and limit is the maximum  token: str - token used for getting all clients information 

returns:      mf_resp: response.Response - response object.  

Usage:
```                        >>> from magistrala import sdk      >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")      >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"      >>> query_params = {      ...     "offset": 0,      ...     "limit": 10      ... }      >>> mf_resp = mfsdk.clients.get_by_channel(channel_id, query_params)      >>> mf_resp         

---

### <kbd>method</kbd> `get_role`

```python
get_role(domain_id: str, client_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `list_members`

```python
list_members(domain_id: str, client_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(domain_id: str, client_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list_role_members`

```python
list_role_members(
    domain_id: str,
    client_id: str,
    role_id: str,
    query_params: dict,
    token: str
)
```





---

### <kbd>method</kbd> `list_roles`

```python
list_roles(domain_id: str, client_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `set_parent_group`

```python
set_parent_group(
    domain_id: str,
    client_id: str,
    parent_group_id: str,
    token: str
)
```





---

### <kbd>method</kbd> `share_thing`

```python
share_thing(user_id: str, channel_id: str, actions: list, token: str)
```

Shares client. 

Allows a logged in user to create new policies for a client over a channel provided with a user ID, channel ID, actions that the client can partake in and a valid token. 

params:  user_id: str - ID of the user  channel_id: str - ID of the channel  actions: list - list of actions for example:   ["m_write", "m_read"]  token: str - token used for sharing client  



**returns:**
 
 - <b>`mf_resp`</b>:  "OK" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> user_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> actions = ["m_write", "m_read"]     >>> mf_resp = mfsdk.clients.share_thing(user_id, channel_id, actions)     >>> mf_resp 

---

### <kbd>method</kbd> `update`

```python
update(client_id: str, client: dict, token: str)
```

Updates client entity. 

Allows a logged in user to make changes and update a client's information with provided client ID and valid token. Information  such as the metadata and name can be updated.  

params:  client_id: str - ID of the client  client: dict - client information for example:  {  "name": "client1"  }  token: str - token used for updating client information   



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```                               >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> client = {     ...     "name": "client2",     ...  }     >>> mf_resp = mfsdk.clients.update(client_id, client)     >>> mf_resp             

---

### <kbd>method</kbd> `update_client_owner`

```python
update_client_owner(client_id: str, client: dict, token: str)
```

Updates client owner. 

Allows a logged in user to make changes and update a client's  information with provided client ID and valid token. The client  owner can be updated. 

params:  client_id: str - ID of the client  client: dict - client information for example:  {  "owner": "user1"  }  token: str - token used for updating client information  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> client = {     ...     "owner": "user1"     ...  }     >>> mf_resp = mfsdk.clients.update_client_owner(client_id, client)     >>> mf_resp 

---

### <kbd>method</kbd> `update_client_secret`

```python
update_client_secret(client_id: str, client: dict, token: str)
```

Updates client secret. 

Allows a logged in user to make changes and update a client's information with provided client ID and valid token. The client's  secret can be updated. 

params:  client_id: str - ID of the client  client: dict - client information for example:  {  "key": "client1"  }  token: str - token used for updating client information  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> client = {     ...     "key": "client2",     ...  }     >>> mf_resp = mfsdk.clients.update_client_secret(client_id, client)     >>> mf_resp 

---

### <kbd>method</kbd> `update_client_tags`

```python
update_client_tags(client_id: str, client: dict, token: str)
```

Updates client tags. 

Allows a logged in user to make changes and update a client's information with provided client ID and valid token. The client's tags can be updated. 

params:  client_id: str - ID of the client  client: dict - client information for example:  {  "tags": ["tag1", "tag2"]  }  token: str - token used for updating client information  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk        >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> client = {     ...     "tags": ["tag1", "tag2"]     ...  }     >>> mf_resp = mfsdk.clients.update_client_tags(client_id, client)     >>> mf_resp 

---

### <kbd>method</kbd> `update_role`

```python
update_role(
    domain_id: str,
    client_id: str,
    role_id: str,
    role: dict,
    token: str
)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
