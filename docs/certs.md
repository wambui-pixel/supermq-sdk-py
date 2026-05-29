<!-- markdownlint-disable -->

# <kbd>module</kbd> `certs`






---

## <kbd>class</kbd> `Certs`
Magistrala Certificates API 

Certs is used to issue, view, and revoke certificates. It is used to issue certificates for clients.  



**Args:**
 
 - <b>`url`</b> (str):  Magistrala Certificates API URL. 
 - <b>`CERTS_ENDPOINT`</b> (str):  Certificates API endpoint. 

### <kbd>method</kbd> `__init__`

```python
__init__(url: str)
```

Initializes Certs with the provided URL. 



**Args:**
 
 - <b>`url`</b> (str):  Magistrala Certificates API URL. 



**Returns:**
 
 - <b>`Certs`</b>:  Certs object. 




---

### <kbd>method</kbd> `issue`

```python
issue(client_id: str, valid: str, token: str)
```

Issues a certificate for a given client ID. 



**Args:**
 
 - <b>`client_id`</b> (str):  Client ID. 
 - <b>`valid`</b> (str):  Certificate validity period. 
 - <b>`token`</b> (str):  Authorization token. 



**Returns:**
 
 - <b>`Response`</b>:  Magistrala response. 

Usage: ``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> client_id = "client_id"
    >>> valid = "1h"
    >>> mf_resp = mfsdk.certs.issue(client_id, valid)
    >>> mf_resp


---

### <kbd>method</kbd> `revoke`

```python
revoke(client_id: str, token: str)
```

Revokes a certificate for a given client ID. 

Deletes a certificate for a given client ID and valid token. 

params:  client_id (str): client id  token (str): valid authorization token used to delete the certificate 



**Returns:**
 
 - <b>`mf_resp `</b>:  response.Response - response object. 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> client_id = "client_id"
    >>> mf_resp = mfsdk.certs.revoke(client_id)
    >>> mf_resp


---

### <kbd>method</kbd> `view_by_client`

```python
view_by_client(client_id: str, token: str)
```

Retrieves a list of certificates' serial IDs for a given client ID. 

Provides a list of certificates' serial IDs for a given client ID. 

Params:  client_id (str): Client ID.  token (str): Authorization token.  



**Returns:**
 
 - <b>`mf_resp `</b>:  response.Response - response object. 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> client_id = "client_id"
    >>> mf_resp = mfsdk.certs.view_by_client(client_id)
    >>> mf_resp


---

### <kbd>method</kbd> `view_by_serial`

```python
view_by_serial(cert_id: str, token: str)
```

Retrieves a certificate for a given cert ID. 

Provides a certificate for a given cert ID. 

Params: 

 cert_id (str): Certificate ID.  token (str): Authorization token.  



**Returns:**
 
 - <b>`mf_resp `</b>:  response.Response - response object. 

Usage: 

``` from magistrala import sdk```

 - <b>`    >>> mfsdk = sdk.SDK(certs_url="http`</b>: //localhost:9019")
    >>> cert_id = "cert_id"
    >>> mf_resp = mfsdk.certs.view_by_serial(cert_id)
    >>> mf_resp





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
