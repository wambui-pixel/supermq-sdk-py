<!-- markdownlint-disable -->

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `things`






---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L7"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Things`
Things API client. 

Things API is used for creating and managing things. It is used for creating new things, creating multiple things getting thing information, updating thing information, disabling  and enabling things ,and connecting and disconnecting things. 



**Attributes:**
 
 - <b>`URL`</b>:  str - URL of the Things API 
 - <b>`THINGS_ENDPOINT`</b>:  str - Things API endpoint 

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```








---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L658"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `authorise_thing`

```python
authorise_thing(access_request: dict, token: str)
```

Authorises thing. 

Creates policies for a thing as a subject over a channel which is the object.  It authorizes the thing to perform some actions over the channel. 

params: 

 access_request: dict - access request information for example:  {  "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",  "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",  "actions": "m_write"  "entity_type": "group"  }  token: str - token used for authorising thing  



**returns:**
 
 - <b>`resp`</b>:  "True" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> access_request = {     ...     "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",     ...     "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",     ...     "actions": "m_write"     ...     "entity_type": "group"     ... }     >>> resp = mgsdk.things.authorise_thing(access_request)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L534"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connect`

```python
connect(client_id: str, channel_id: str, action: str, token: str)
```

Connects thing and channel. 

Connects a thing and channel with provided thing ID as the subject, channel ID as the object, action that the thing can partake in and a valid token. 

params:  client_id: str - ID of the thing  channel_id: str - ID of the channel  action: str - action for example: "m_write"  token: str - token used for connecting thing and channel  



**returns:**
 
 - <b>`resp`</b>:  "connected" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> action = "m_write"     >>> resp = mgsdk.things.connect(client_id, channel_id, action)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `connects`

```python
connects(client_ids: list, channel_ids: list, actions: list, token: str)
```

Connects things and channels.  

Connects multiple things and channels with provided thing IDs  as the subjects, channel IDs as the objects, actions that the  thing can partake in and a valid token. 

params:  client_ids: list - list of thing IDs  channel_ids: list - list of channel IDs  actions: list - list of actions for example:   ["m_write", "m_read"]  token: str - token used for connecting things and channels  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> actions = ["m_write", "m_read"]     >>> resp = mgsdk.things.connects(client_ids, channel_ids, actions)     >>> resp             

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create`

```python
create(thing: dict, token: str)
```

Creates thing entity in the database.  

Creates a new thing with provided thing information. If token is provided, it will be used to create a new thing 

params:  thing: dict - thing information for example:  {  "name": "thing1"  }  token: str - token used for creating a new thing  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object 

Usage:
```          >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> thing = {     ...     "name": "thing1",     ...  }     >>> resp = mgsdk.things.create(thing)     >>> resp             

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(things: list, token: str)
```

Creates multiple things in bulk.  

Creates multiple new things with provided things information. If a token is provided, it will be used to create the new things. 

params:  things: list - a list of things with theri information for example:  [  {"name": "thing2"},   {"name": "thing3"},   {"name": "thing4"}  ]  token: str - token used for creating the new things.  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object 

Usage:
```          >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> things = [     ...     {"name": "thing2"},      ...     {"name": "thing3"},      ...     {"name": "thing4"}     ... ]     >>> resp = mgsdk.things.create_bulk(things)     >>> resp             

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L422"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable(client_id: str, token: str)
```

Deletes a thing entity from the database. 

Deletes a thing with provided thing ID and valid token. 

params:  client_id: str - ID of the thing  token: str - token used for deleting thing  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
```                       >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> resp = mgsdk.things.disable(client_id)     >>> resp         

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L576"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnect`

```python
disconnect(client_id: str, channel_id: str, token: str)
```

Disconnects thing and channel. 

Disconnects a thing and channel with provided thing ID as the subject,   channel ID as the object and a valid token. 

params:  client_id: str - ID of the thing  channel_id: str - ID of the channel  token: str - token used for disconnecting thing and channel  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> resp = mgsdk.things.disconnect(client_id, channel_id)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L497"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disconnects`

```python
disconnects(client_ids: list, channel_ids: list, token: str)
```

Disconnect things and channels. 

Disconnects multiple things and channels with provided thing IDs  as the subjects, channel IDs as the objects and a valid token. 

params:  client_ids: list - list of thing IDs  channel_ids: list - list of channel IDs  token: str - token used for disconnecting things and channels 



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]     >>> resp = mgsdk.things.disconnects(client_ids, channel_ids)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get`

```python
get(client_id: str, token: str)
```

Gets a thing entity. 

Provides information about a thing with provided thing ID and token. Information about a thing is provided in a JSON format and includes the name its owner, secret,tags and status. 

params:  client_id: str - ID of the thing  token: str - token used for getting thing information 



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
```               >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> resp = mgsdk.things.get(client_id)     >>> resp         

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all things from database. 

Provides information about all things in a JSON format. It is controlled by a set of query parameters and a valid token. 

params:  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10  }  where offset is the number of things to skip and limit is the maximum  token: str - token used for getting all things information 



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
```                   >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> query_params = {     ...     "offset": 0,     ...     "limit": 10     ... }     >>> resp = mgsdk.things.get_all(query_params)     >>> resp         

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_by_channel`

```python
get_by_channel(channel_id: str, query_params: dict, token: str)
```

Gets all things to which a specific thing is connected to. 

Provides a list of all things that are connected to a specific channel when given a channel ID and valid token. 

params:  channel_id: str - ID of the channel  query_params: dict - query parameters for example:  {  "offset": 0,  "limit": 10  }  where offset is the number of things to skip and limit is the maximum  token: str - token used for getting all things information 

returns:      resp: response.Response - response object.  

Usage:
```                        >>> from magistrala import sdk      >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")      >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"      >>> query_params = {      ...     "offset": 0,      ...     "limit": 10      ... }      >>> resp = mgsdk.things.get_by_channel(channel_id, query_params)      >>> resp         

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L615"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `share_thing`

```python
share_thing(user_id: str, channel_id: str, actions: list, token: str)
```

Shares thing. 

Allows a logged in user to create new policies for a thing over a channel provided with a user ID, channel ID, actions that the thing can partake in and a valid token. 

params:  user_id: str - ID of the user  channel_id: str - ID of the channel  actions: list - list of actions for example:   ["m_write", "m_read"]  token: str - token used for sharing thing  



**returns:**
 
 - <b>`resp`</b>:  "OK" 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> user_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> actions = ["m_write", "m_read"]     >>> resp = mgsdk.things.share_thing(user_id, channel_id, actions)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L246"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update`

```python
update(client_id: str, thing: dict, token: str)
```

Updates thing entity. 

Allows a logged in user to make changes and update a thing's information with provided thing ID and valid token. Information  such as the metadata and name can be updated.  

params:  client_id: str - ID of the thing  thing: dict - thing information for example:  {  "name": "thing1"  }  token: str - token used for updating thing information   



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
```                               >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "name": "thing2",     ...  }     >>> resp = mgsdk.things.update(client_id, thing)     >>> resp             

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L378"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_owner`

```python
update_thing_owner(client_id: str, thing: dict, token: str)
```

Updates thing owner. 

Allows a logged in user to make changes and update a thing's  information with provided thing ID and valid token. The thing  owner can be updated. 

params:  client_id: str - ID of the thing  thing: dict - thing information for example:  {  "owner": "user1"  }  token: str - token used for updating thing information  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "owner": "user1"     ...  }     >>> resp = mgsdk.things.update_thing_owner(client_id, thing)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L290"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_secret`

```python
update_thing_secret(client_id: str, thing: dict, token: str)
```

Updates thing secret. 

Allows a logged in user to make changes and update a thing's information with provided thing ID and valid token. The thing's  secret can be updated. 

params:  client_id: str - ID of the thing  thing: dict - thing information for example:  {  "key": "thing1"  }  token: str - token used for updating thing information  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk     >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "key": "thing2",     ...  }     >>> resp = mgsdk.things.update_thing_secret(client_id, thing)     >>> resp 

---

<a href="https://github.com/absmach/supermq-sdk-py/blob/main/magistrala/things.py#L334"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `update_thing_tags`

```python
update_thing_tags(client_id: str, thing: dict, token: str)
```

Updates thing tags. 

Allows a logged in user to make changes and update a thing's information with provided thing ID and valid token. The thing's tags can be updated. 

params:  client_id: str - ID of the thing  thing: dict - thing information for example:  {  "tags": ["tag1", "tag2"]  }  token: str - token used for updating thing information  



**returns:**
 
 - <b>`resp`</b>:  response.Response - response object. 

Usage:
``` 

    >>> from magistrala import sdk        >>> mgsdk = sdk.SDK(things_url="http://localhost:9000")     >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"     >>> thing = {     ...     "tags": ["tag1", "tag2"]     ...  }     >>> resp = mgsdk.things.update_thing_tags(client_id, thing)     >>> resp 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
