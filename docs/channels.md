<!-- markdownlint-disable -->

# <kbd>module</kbd> `channels`






---

## <kbd>class</kbd> `Channels`
Channels class provides the abstraction of the Magistrala Channels API. 

Channels are used to connect clients and users. They are used to send messages to clients and  receive messages from clients. Channels API provides the following functionalities: 
    - create channel 
    - create multiple channels in a bulk 
    - get channel 
    - get all channels 
    - get all channels to which a specific client is connected to 
    - update channel 
    - delete channel 
    - identify client  



**Attributes:**
 
 - <b>`CHANNELS_ENDPOINT`</b> (str):  Channels API endpoint 
 - <b>`CLIENTS_ENDPOINT`</b> (str):  Clients API endpoint 
 - <b>`IDENTIFY_ENDPOINT`</b> (str):  Identify API endpoint 



### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```

Initializes Channels class with the provided url 



**Args:**
 
 - <b>`url`</b> (str):  Magistrala Channels API URL 



**returns:**
 
 - <b>`Channels`</b>:  Channels object initialized with the provided url. 



**raises:**
 None 




---

### <kbd>method</kbd> `add_role_actions`

```python
add_role_actions(
    domain_id: str,
    channel_id: str,
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
    channel_id: str,
    role_id: str,
    members: list,
    token: str
)
```





---

### <kbd>method</kbd> `connect_client`

```python
connect_client(
    client_ids: list,
    channel_id: str,
    connection_types: list,
    domain_id: str,
    token: str
)
```

Connects clients to a single channel. 

---

### <kbd>method</kbd> `create`

```python
create(channel: dict, token: str)
```

Creates channel entity in the database 

Creates a new channel in the database when provided with a valid token. 

params:  channel (dict): Channel entity to be created for example:  {  "name": "channel_name",  "metadata": {  "description": "channel_description"  }  }  token (str): User's token  



**returns:**
 
 - <b>`Response`</b>:  Response object containing the response from the server 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> channel = {

 - <b>`    ...    "name"`</b>:  "channel_name"
    ... }
    >>> mf_resp = mfsdk.channels.create(channel, token)
    >>> mf_resp


---

### <kbd>method</kbd> `create_bulk`

```python
create_bulk(channels: list, token: str)
```

Creates multiple channels in bulk 

Creates multiple new channels when provided with channels information and a valid token. 

params:  channels: list- Channel entities to be created for example:  [  {  "name": "channel_name",  "metadata": {  "description": "channel_description"  }  },  {  "name": "channel_name",  "metadata": {  "description": "channel_description"  }  }  ]  

 token (str): User's token 



**returns:**
 
 - <b>`Response`</b>:  Response object containing the response from the server 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> channels = [
    ...    {

 - <b>`    ...        "name"`</b>:  "channel_name"
    ...    },
    ...    {

 - <b>`    ...        "name"`</b>:  "channel_name"
    ...    }
    ... ]
    >>> mf_resp = mfsdk.channels.create_bulk(channels, token)
    >>> mf_resp


---

### <kbd>method</kbd> `create_role`

```python
create_role(
    domain_id: str,
    channel_id: str,
    role_name: str,
    token: str,
    optional_actions: list = None,
    optional_members: list = None
)
```





---

### <kbd>method</kbd> `delete`

```python
delete(channel_id: str, domain_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_all_role_actions`

```python
delete_all_role_actions(
    domain_id: str,
    channel_id: str,
    role_id: str,
    token: str
)
```





---

### <kbd>method</kbd> `delete_all_role_members`

```python
delete_all_role_members(
    domain_id: str,
    channel_id: str,
    role_id: str,
    token: str
)
```





---

### <kbd>method</kbd> `delete_parent_group`

```python
delete_parent_group(domain_id: str, channel_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role`

```python
delete_role(domain_id: str, channel_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `delete_role_actions`

```python
delete_role_actions(
    domain_id: str,
    channel_id: str,
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
    channel_id: str,
    role_id: str,
    members: list,
    token: str
)
```





---

### <kbd>method</kbd> `disable`

```python
disable(channel_id: str, token: str)
```

Deletes a channel entity from database. 

Deletes a channel entity from database when provided with a valid channel ID and token. The channel is not deleted from the database but is marked as disabled. 

params: 

 channel_id (str): Channel ID  token (str): User's token  



**returns:**
 


 - <b>`mf_resp`</b>:  response.Response -response object 

Usage: 

``` from magistrala import sdk```

 - <b>`        >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
        >>> channel_id = "channel_id"
        >>> mf_resp = mfsdk.channels.disable(channel_id, token)
        >>> mf_resp


---

### <kbd>method</kbd> `disconnect_client`

```python
disconnect_client(
    client_ids: list,
    channel_id: str,
    connection_types: list,
    domain_id: str,
    token: str
)
```

Disconnects clients from a single channel. 

---

### <kbd>method</kbd> `enable`

```python
enable(channel_id: str, domain_id: str, token: str)
```





---

### <kbd>method</kbd> `get`

```python
get(channel_id: str, token: str)
```

Gets a channel entity for a logged-in user 

Provides a channel entity when provided with a valid channel ID and token. 

params:   channel_id (str): Channel ID  token (str): User's token  



**returns:**
 
 - <b>`Response`</b>:  Response object 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> channel_id = "channel_id"
    >>> mf_resp = mfsdk.channels.get(channel_id, token)
    >>> mf_resp


---

### <kbd>method</kbd> `get_all`

```python
get_all(query_params: dict, token: str)
```

Gets all channels from database 

Gets all channels from database when provided with a valid token.. 

params:  query_params (dict): Query parameters for example:  {  "offset": 0,  "limit": 10  }  token (str): User's token  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response -response object 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> query_params = {

 - <b>`    ...    "offset"`</b>:  0,

 - <b>`    ...    "limit"`</b>:  10
    ... }
    >>> mf_resp = mfsdk.channels.get_all(query_params, token)
    >>> mf_resp


---

### <kbd>method</kbd> `get_by_client`

```python
get_by_client(client_id: str, query_params: dict, token: str)
```

Gets all channels to which a specific client is connected to. 

Provides a list of all the channels a client is connected to when provided with a valid token and client ID. 

params:  client_id (str): Client ID  query_params (dict): Query parameters for example:  {  "offset": 0,  "limit": 10  }  token (str): User's token  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response -response object 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> client_id = "client_id"
    >>> query_params = {

 - <b>`    ...    "offset"`</b>:  0,

 - <b>`    ...    "limit"`</b>:  10
    ... }
    >>> mf_resp = mfsdk.channels.get_by_client(client_id, query_params, token)
    >>> mf_resp


---

### <kbd>method</kbd> `get_role`

```python
get_role(domain_id: str, channel_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `identify_client`

```python
identify_client(client_key: str)
```

Validates client's key and returns it's ID if key is valid 

Uses a client_key or secret to validate a client and provide its information. 

params:  client_key (str): Client's key  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response -response object 

Usage: 

``` from magistrala import sdk    ```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> client_key = "client_key"
    >>> mf_resp = mfsdk.channels.identify_client(client_key)
    >>> mf_resp


---

### <kbd>method</kbd> `list_available_actions`

```python
list_available_actions(domain_id: str, token: str)
```





---

### <kbd>method</kbd> `list_members`

```python
list_members(domain_id: str, channel_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `list_role_actions`

```python
list_role_actions(domain_id: str, channel_id: str, role_id: str, token: str)
```





---

### <kbd>method</kbd> `list_role_members`

```python
list_role_members(
    domain_id: str,
    channel_id: str,
    role_id: str,
    query_params: dict,
    token: str
)
```





---

### <kbd>method</kbd> `list_roles`

```python
list_roles(domain_id: str, channel_id: str, query_params: dict, token: str)
```





---

### <kbd>method</kbd> `set_parent_group`

```python
set_parent_group(
    domain_id: str,
    channel_id: str,
    parent_group_id: str,
    token: str
)
```





---

### <kbd>method</kbd> `update`

```python
update(channel_id: str, channel: dict, token: str)
```

Updates channel entity 

Updates a channel entity when provided with a valid channel ID, channel entity and token. The information that can be updated are channel's name and metadata. 

params:  channel_id (str): Channel ID  channel (dict): Channel entity to be updated for example:  {  "name": "channel_name",  "metadata": {  "description": "channel_description"  }  }  token (str): User's token  



**returns:**
 
 - <b>`mf_resp`</b>:  response.Response -response object 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(channels_url="http`</b>: //localhost:9000")
    >>> channel_id = "channel_id"
    >>> channel = {

 - <b>`    ...    "name"`</b>:  "channel_name"
    ... }
    >>> mf_resp = mfsdk.channels.update(channel_id, channel, token)
    >>> mf_resp


---

### <kbd>method</kbd> `update_role`

```python
update_role(
    domain_id: str,
    channel_id: str,
    role_id: str,
    role: dict,
    token: str
)
```





---

### <kbd>method</kbd> `update_tags`

```python
update_tags(channel_id: str, channel: dict, domain_id: str, token: str)
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
