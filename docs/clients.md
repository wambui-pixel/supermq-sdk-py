<!-- markdownlint-disable -->

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `clients`






---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Clients`
Clients API client. 

Clients API is used for creating and managing clients. It is used for creating new clients, creating multiple clients getting thing information, updating thing information, disabling  and enabling clients ,and connecting and disconnecting clients. 



**Attributes:**
 
 - <b>`URL`</b>:  str - URL of the Clients API 
 - <b>`CLIENTS_ENDPOINT`</b>:  str - Clients API endpoint 

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L658"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `authorise_thing`

```python
authorise_thing(access_request: dict, token: str)
```

Authorises thing. 

Creates policies for a thing as a subject over a channel which is the object.  It authorizes the thing to perform some actions over the channel. 

params: 

 access_request: dict - access request information for example:  {  "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",  "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",  "actions": "m_write"  "entity_type": "group"  }  token: str - token used for authorising thing  



**returns:**
 
 - <b>`mf_resp`</b>:  "True" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> access_request = {     ...     "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",     ...     "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",     ...     "actions": "m_write"     ...     "entity_type": "group"     ... }     >>> mf_resp = mfsdk.clients.authorise_thing(access_request)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L534"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect(thing_id: str, channel_id: str, action: str, token: str)
```

Connects thing and channel. 

Connects a thing and channel with provided thing ID as the subject, channel ID as the object, action that the thing can partake in and a valid token. 

params:  thing_id: str - ID of the thing  channel_id: str - ID of the channel  action: str - action for example: "m_write"  token: str - token used for connecting thing and channel  



**returns:**
 
 - <b>`mf_resp`</b>:  "connected" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> action = "m_write"     >>> mf_resp = mfsdk.clients.connect(thing_id, channel_id, action)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connects`

```python
connects(thing_ids: list, channel_ids: list, actions: list, token: str)
```

Connects clients and channels.  

Connects multiple clients and channels with provided thing IDs  as the subjects, channel IDs as the objects, actions that the  thing can partake in and a valid token. 

params:  thing_ids: list - list of thing IDs  channel_ids: list - list of channel IDs  actions: list - list of actions for example:   ["m_write", "m_read"]  token: str - token used for connecting clients and channels  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> actions = ["m_write", "m_read"]     >>> mf_resp = mfsdk.clients.connects(thing_ids, channel_ids, actions)     >>> mf_resp             

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(thing: dict, token: str)
```

Creates thing entity in the database.  

Creates a new thing with provided thing information. If token is provided, it will be used to create a new thing 

params:  thing: dict - thing information for example:  {  "name": "thing1"  }  token: str - token used for creating a new thing  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing = {     ...     "name": "thing1",     ...  }     >>> mf_resp = mfsdk.clients.create(thing)     >>> mf_resp             

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(clients: list, token: str)
```

Creates multiple clients in bulk.  

Creates multiple new clients with provided clients information. If a token is provided, it will be used to create the new clients. 

params:  clients: list - a list of clients with theri information for example:  [  {"name": "thing2"},   {"name": "thing3"},   {"name": "thing4"}  ]  token: str - token used for creating the new clients.  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object 

Usage:
```          >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> clients = [     ...     {"name": "thing2"},      ...     {"name": "thing3"},      ...     {"name": "thing4"}     ... ]     >>> mf_resp = mfsdk.clients.create_bulk(clients)     >>> mf_resp             

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L422"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(thing_id: str, token: str)
```

Deletes a thing entity from the database. 

Deletes a thing with provided thing ID and valid token. 

params:  thing_id: str - ID of the thing  token: str - token used for deleting thing  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```                       >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> mf_resp = mfsdk.clients.disable(thing_id)     >>> mf_resp         

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L576"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect(thing_id: str, channel_id: str, token: str)
```

Disconnects thing and channel. 

Disconnects a thing and channel with provided thing ID as the subject,   channel ID as the object and a valid token. 

params:  thing_id: str - ID of the thing  channel_id: str - ID of the channel  token: str - token used for disconnecting thing and channel  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> mf_resp = mfsdk.clients.disconnect(thing_id, channel_id)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L497"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnects`

```python
disconnects(thing_ids: list, channel_ids: list, token: str)
```

Disconnect clients and channels. 

Disconnects multiple clients and channels with provided thing IDs  as the subjects, channel IDs as the objects and a valid token. 

params:  thing_ids: list - list of thing IDs  channel_ids: list - list of channel IDs  token: str - token used for disconnecting clients and channels 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> mf_resp = mfsdk.clients.disconnects(thing_ids, channel_ids)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(thing_id: str, token: str)
```

Gets a thing entity. 

Provides information about a thing with provided thing ID and token. Information about a thing is provided in a JSON format and includes the name its owner, secret,tags and status. 

params:  thing_id: str - ID of the thing  token: str - token used for getting thing information 



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```               >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> mf_resp = mfsdk.clients.get(thing_id)     >>> mf_resp         

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_channel`

```python
get_by_channel(channel_id: str, query_params: dict, token: str)
```

Gets all clients to which a specific thing is connected to. 

Provides a list of all clients that are connected to a specific channel when given a channel ID and valid token. 

params:  channel_id: str - ID of the channel  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10  }  where offset is the number of clients to skip and limit is the maximum  token: str - token used for getting all clients information 

returns:      mf_resp: response.Response - response object.  

Usage:
```                        >>> from magistrala import sdk      >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")      >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"      >>> query_params = {      ...     "offset": 0,      ...     "limit": 10      ... }      >>> mf_resp = mfsdk.clients.get_by_channel(channel_id, query_params)      >>> mf_resp         

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L615"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `share_thing`

```python
share_thing(user_id: str, channel_id: str, actions: list, token: str)
```

Shares thing. 

Allows a logged in user to create new policies for a thing over a channel provided with a user ID, channel ID, actions that the thing can partake in and a valid token. 

params:  user_id: str - ID of the user  channel_id: str - ID of the channel  actions: list - list of actions for example:   ["m_write", "m_read"]  token: str - token used for sharing thing  



**returns:**
 
 - <b>`mf_resp`</b>:  "OK" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> user_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> actions = ["m_write", "m_read"]     >>> mf_resp = mfsdk.clients.share_thing(user_id, channel_id, actions)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L246"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(thing_id: str, thing: dict, token: str)
```

Updates thing entity. 

Allows a logged in user to make changes and update a thing's information with provided thing ID and valid token. Information  such as the metadata and name can be updated.  

params:  thing_id: str - ID of the thing  thing: dict - thing information for example:  {  "name": "thing1"  }  token: str - token used for updating thing information   



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
```                               >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "name": "thing2",     ...  }     >>> mf_resp = mfsdk.clients.update(thing_id, thing)     >>> mf_resp             

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L378"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_owner`

```python
update_thing_owner(thing_id: str, thing: dict, token: str)
```

Updates thing owner. 

Allows a logged in user to make changes and update a thing's  information with provided thing ID and valid token. The thing  owner can be updated. 

params:  thing_id: str - ID of the thing  thing: dict - thing information for example:  {  "owner": "user1"  }  token: str - token used for updating thing information  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "owner": "user1"     ...  }     >>> mf_resp = mfsdk.clients.update_thing_owner(thing_id, thing)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L290"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_secret`

```python
update_thing_secret(thing_id: str, thing: dict, token: str)
```

Updates thing secret. 

Allows a logged in user to make changes and update a thing's information with provided thing ID and valid token. The thing's  secret can be updated. 

params:  thing_id: str - ID of the thing  thing: dict - thing information for example:  {  "key": "thing1"  }  token: str - token used for updating thing information  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "key": "thing2",     ...  }     >>> mf_resp = mfsdk.clients.update_thing_secret(thing_id, thing)     >>> mf_resp 

---

<a href="https://github.com/magistrala/sdk-py/blob/main/magistrala/clients.py#L334"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_tags`

```python
update_thing_tags(thing_id: str, thing: dict, token: str)
```

Updates thing tags. 

Allows a logged in user to make changes and update a thing's information with provided thing ID and valid token. The thing's tags can be updated. 

params:  thing_id: str - ID of the thing  thing: dict - thing information for example:  {  "tags": ["tag1", "tag2"]  }  token: str - token used for updating thing information  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk        >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")     >>> thing_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "tags": ["tag1", "tag2"]     ...  }     >>> mf_resp = mfsdk.clients.update_thing_tags(thing_id, thing)     >>> mf_resp 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
