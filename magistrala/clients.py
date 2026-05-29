import requests
from magistrala import response
from magistrala import errors
from magistrala import utils
from magistrala.roles import Roles


class Clients:
    """Clients API client.
    
    Clients API is used for creating and managing clients.
    It is used for creating new clients, creating multiple clients
    getting client information, updating client information, disabling 
    and enabling clients ,and connecting and disconnecting clients.
    
    Attributes:
        URL: str - URL of the Clients API
        CLIENTS_ENDPOINT: str - Clients API endpoint
    """
    CLIENTS_ENDPOINT = "clients"

    def __init__(self, url: str):
        self.URL = url
        self.__roles = Roles()
    """Initializes Clients API client.
        
        params:
            url: str - URL of the Clients API
        
        returns:
            Thigs: Clients - Clients API client
            
        raises:
            None
    """
    def create(self, client: dict, token: str):
        """Creates client entity in the database.
                
        Creates a new client with provided client information.
        If token is provided, it will be used to create a new client

        params:
            client: dict - client information for example:
            {
                "name": "client1"
            }
            token: str - token used for creating a new client
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client = {
            ...     "name": "client1",
            ...  }
            >>> mf_resp = mfsdk.clients.create(client)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.CLIENTS_ENDPOINT,
            json=client,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["create"], http_resp.status_code
            )
        else:
             mf_resp.value = http_resp.json()
        return mf_resp

    def create_bulk(self, clients: list, token: str):
        """Creates multiple clients in bulk.
                
        Creates multiple new clients with provided clients information.
        If a token is provided, it will be used to create the new clients.

        params:
            clients: list - a list of clients with theri information for example:
                [
                    {"name": "client2"}, 
                    {"name": "client3"}, 
                    {"name": "client4"}
                ]
            token: str - token used for creating the new clients.
            
        returns:
            mf_resp: response.Response - response object

        Usage::
            
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> clients = [
            ...     {"name": "client2"}, 
            ...     {"name": "client3"}, 
            ...     {"name": "client4"}
            ... ]
            >>> mf_resp = mfsdk.clients.create_bulk(clients)
            >>> mf_resp            
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/bulk",
            json=clients,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["create_bulk"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, client_id: str, token: str):
        """Gets a client entity.
        
        Provides information about a client with provided client ID and token.
        Information about a client is provided in a JSON format and includes the name
        its owner, secret,tags and status.
        
        params:
            client_id: str - ID of the client
            token: str - token used for getting client information
        
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> mf_resp = mfsdk.clients.get(client_id)
            >>> mf_resp        
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/" + client_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, query_params: dict, token: str):
        """Gets all clients from database.
        
        Provides information about all clients in a JSON format. It is controlled
        by a set of query parameters and a valid token.
        
        params:
            query_params: dict - query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
                where offset is the number of clients to skip and limit is the maximum
            token: str - token used for getting all clients information
        
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                    
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10
            ... }
            >>> mf_resp = mfsdk.clients.get_all(query_params)
            >>> mf_resp        
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/" + self.CLIENTS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_by_channel(self, channel_id: str, query_params: dict, token: str):
        """Gets all clients to which a specific client is connected to.
        
        Provides a list of all clients that are connected to a specific channel when
        given a channel ID and valid token.
        
        params:
            channel_id: str - ID of the channel
            query_params: dict - query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
                where offset is the number of clients to skip and limit is the maximum
            token: str - token used for getting all clients information
        
        returns:    
            mf_resp: response.Response - response object.
            
        Usage::
                        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> query_params = {
            ...     "offset": 0,
            ...     "limit": 10
            ... }
            >>> mf_resp = mfsdk.clients.get_by_channel(channel_id, query_params)
            >>> mf_resp        
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.URL + "/channels/" + channel_id + "/" + self.CLIENTS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["get_by_channel"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, client_id: str, client: dict, token: str):
        """Updates client entity.
        
        Allows a logged in user to make changes and update a client's
        information with provided client ID and valid token. Information 
        such as the metadata and name can be updated. 
        
        params:
            client_id: str - ID of the client
            client: dict - client information for example:
                {
                    "name": "client1"
                }
            token: str - token used for updating client information 
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                                
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> client = {
            ...     "name": "client2",
            ...  }
            >>> mf_resp = mfsdk.clients.update(client_id, client)
            >>> mf_resp            
        """
        http_resp = requests.patch(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/" + client_id,
            json=client,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def update_client_secret(self, client_id: str, client: dict, token: str):
        """Updates client secret.
        
        Allows a logged in user to make changes and update a client's
        information with provided client ID and valid token. The client's 
        secret can be updated.
        
        params:
            client_id: str - ID of the client
            client: dict - client information for example:
                {
                    "key": "client1"
                }
            token: str - token used for updating client information
            
        returns:
            mf_resp: response.Response - response object.
        
        Usage::

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> client = {
            ...     "key": "client2",
            ...  }
            >>> mf_resp = mfsdk.clients.update_client_secret(client_id, client)
            >>> mf_resp
        """
        http_resp = requests.patch(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/" + client_id + "/secret",
            json=client,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["update_client_secret"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def update_client_tags(self, client_id: str, client: dict, token: str):
        """Updates client tags.
        
        Allows a logged in user to make changes and update a client's
        information with provided client ID and valid token. The client's
        tags can be updated.
        
        params:
            client_id: str - ID of the client
            client: dict - client information for example:
                {
                    "tags": ["tag1", "tag2"]
                }
            token: str - token used for updating client information
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
        
            >>> from magistrala import sdk   
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> client = {
            ...     "tags": ["tag1", "tag2"]
            ...  }
            >>> mf_resp = mfsdk.clients.update_client_tags(client_id, client)
            >>> mf_resp
        """
        http_resp = requests.patch(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/" + client_id + "/tags",
            json=client,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["update_client_tags"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def update_client_owner(self, client_id: str, client: dict, token: str):
        """Updates client owner.
        
        Allows a logged in user to make changes and update a client's
            information with provided client ID and valid token. The client
            owner can be updated.
        
        params:
            client_id: str - ID of the client
            client: dict - client information for example:
                {
                    "owner": "user1"
                }
            token: str - token used for updating client information
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> client = {
            ...     "owner": "user1"
            ...  }
            >>> mf_resp = mfsdk.clients.update_client_owner(client_id, client)
            >>> mf_resp
        """
        http_resp = requests.patch(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/" + client_id + "/owner",
            json=client,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["update_client_owner"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, client_id: str, token: str):
        """Deletes a client entity from the database.
        
        Deletes a client with provided client ID and valid token.
        
        params:
            client_id: str - ID of the client
            token: str - token used for deleting client
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
                        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> mf_resp = mfsdk.clients.disable(client_id)
            >>> mf_resp        
        """
        http_resp = requests.post(
            self.URL + "/" + self.CLIENTS_ENDPOINT + "/" + client_id + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["delete"], http_resp.status_code
            )
        return mf_resp

    def connects(self, client_ids: list, channel_ids: list, actions: list, token: str):
        """Connects clients and channels. 
        
        Connects multiple clients and channels with provided client IDs 
        as the subjects, channel IDs as the objects, actions that the 
        client can partake in and a valid token.
        
        params:
            client_ids: list - list of client IDs
            channel_ids: list - list of channel IDs
            actions: list - list of actions for example: 
                ["m_write", "m_read"]
            token: str - token used for connecting clients and channels
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> actions = ["m_write", "m_read"]
            >>> mf_resp = mfsdk.clients.connects(client_ids, channel_ids, actions)
            >>> mf_resp            
        """
        payload = {"subjects": client_ids, "objects": channel_ids, "actions": actions}
        http_resp = requests.post(
            self.URL + "/connect",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["connect"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disconnects(self, client_ids: list, channel_ids: list, token: str):
        """Disconnect clients and channels.
        
        Disconnects multiple clients and channels with provided client IDs 
        as the subjects, channel IDs as the objects and a valid token.
        
        params:
            client_ids: list - list of client IDs
            channel_ids: list - list of channel IDs
            token: str - token used for disconnecting clients and channels
        
        returns:
            mf_resp: response.Response - response object.
            
        Usage::
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_ids = ["fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> channel_ids = ["567f7da5-b7bf-49b7-bf2f-99995e78afd9"]
            >>> mf_resp = mfsdk.clients.disconnects(client_ids, channel_ids)
            >>> mf_resp
        """
        payload = {"subjects": client_ids, "objects": channel_ids}
        http_resp = requests.post(
            self.URL + "/disconnect",
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["disconnect"], http_resp.status_code
            )
        return mf_resp

    def connect(self, client_id: str, channel_id: str, action: str, token: str):
        """Connects client and channel.
        
        Connects a client and channel with provided client ID as the subject,
        channel ID as the object, action that the client can partake in and a
        valid token.
        
        params:
            client_id: str - ID of the client
            channel_id: str - ID of the channel
            action: str - action for example: "m_write"
            token: str - token used for connecting client and channel
            
        returns:
            mf_resp: "connected"
            
        Usage::
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> action = "m_write"
            >>> mf_resp = mfsdk.clients.connect(client_id, channel_id, action)
            >>> mf_resp
        """
        payload= {"subject": client_id, "object": channel_id, "action": action}
        http_resp = requests.post(
            self.URL + "/policies",
            headers=utils.construct_header(token, utils.CTJSON),
            json= payload, 
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["connect"], http_resp.status_code
            )
        else:
            mf_resp.value = "connected"
        return mf_resp

    def disconnect(self, client_id: str, channel_id: str, token: str):
        """Disconnects client and channel.
        
        Disconnects a client and channel with provided client ID as the subject,  
        channel ID as the object and a valid token.
        
        params:
            client_id: str - ID of the client
            channel_id: str - ID of the channel
            token: str - token used for disconnecting client and channel
            
        returns:
            mf_resp: response.Response - response object.
            
        Usage::

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> client_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> mf_resp = mfsdk.clients.disconnect(client_id, channel_id)
            >>> mf_resp
        """
        payload = {"subject": client_id, "object": channel_id}
        http_resp = requests.delete(
            self.URL + "/policies" + "/" + client_id + "/" + channel_id,
            headers=utils.construct_header(token, utils.CTJSON),
            json=payload,
        )
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["disconnect"], http_resp.status_code
            )
        else:
            mf_resp.value = "Disconnected"
        return mf_resp
    
    def share_thing(self, user_id: str, channel_id: str, actions: list, token: str):
        """Shares client.
        
        Allows a logged in user to create new policies for a client over a channel
        provided with a user ID, channel ID, actions that the client can partake in
        and a valid token.
        
        params:
            user_id: str - ID of the user
            channel_id: str - ID of the channel
            actions: list - list of actions for example: 
                ["m_write", "m_read"]
            token: str - token used for sharing client
            
        returns:
            mf_resp: "OK"
            
        Usage::
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> user_id = "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> channel_id = "567f7da5-b7bf-49b7-bf2f-99995e78afd9"
            >>> actions = ["m_write", "m_read"]
            >>> mf_resp = mfsdk.clients.share_thing(user_id, channel_id, actions)
            >>> mf_resp
        """
        payload = {"object": channel_id, "subject": user_id, "actions": actions, "external": True}
        http_resp = requests.post(
            self.URL + "/policies",
            headers=utils.construct_header(token, utils.CTJSON),
            data=payload
        )
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["share_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = "OK"
        return mf_resp
    
    def authorise_thing(self,access_request: dict, token: str):
        """Authorises client.
        
        Creates policies for a client as a subject over a channel which is the object. 
        It authorizes the client to perform some actions over the channel.
        
        params:
        
            access_request: dict - access request information for example:
                {
                    "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",
                    "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",
                    "actions": "m_write"
                    "entity_type": "group"
                }
            token: str - token used for authorising client
            
        returns:
            mf_resp: "True"
            
        Usage::
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(clients_url="http://localhost:9000")
            >>> access_request = {
            ...     "subject": "fd4f7da5-b7bf-49b7-bf2f-99995e78afd9",
            ...     "object": "567f7da5-b7bf-49b7-bf2f-99995e78afd9",
            ...     "actions": "m_write"
            ...     "entity_type": "group"
            ... }
            >>> mf_resp = mfsdk.clients.authorise_thing(access_request)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp= requests.post(
            self.URL +"/channels/object/access",
            headers=utils.construct_header(token, utils.CTJSON),
            json= access_request
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["authorise_thing"], http_resp.status_code
            )
        else:
            mf_resp.value = "True"
        return mf_resp

    def enable(self, client_id: str, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CLIENTS_ENDPOINT
            + "/"
            + client_id
            + "/enable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["enable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete(self, client_id: str, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CLIENTS_ENDPOINT
            + "/"
            + client_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["delete"], http_resp.status_code
            )
        else:
            mf_resp.value = "Client deleted successfully"
        return mf_resp

    def set_parent_group(
        self, domain_id: str, client_id: str, parent_group_id: str, token: str
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CLIENTS_ENDPOINT
            + "/"
            + client_id
            + "/parent",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"parent_group_id": parent_group_id},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["set_parent_group"], http_resp.status_code
            )
        else:
            mf_resp.value = "Parent group set successfully"
        return mf_resp

    def delete_parent_group(self, domain_id: str, client_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.URL
            + "/"
            + domain_id
            + "/"
            + self.CLIENTS_ENDPOINT
            + "/"
            + client_id
            + "/parent",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.clients["delete_parent_group"], http_resp.status_code
            )
        else:
            mf_resp.value = "Parent group removed successfully"
        return mf_resp

    # Role management

    def list_available_actions(self, domain_id: str, token: str):
        return self.__roles.list_available_actions(
            self.URL + "/" + domain_id, self.CLIENTS_ENDPOINT, token
        )

    def create_role(
        self,
        domain_id: str,
        client_id: str,
        role_name: str,
        token: str,
        optional_actions: list = None,
        optional_members: list = None,
    ):
        return self.__roles.create_role(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_name,
            token,
            optional_actions,
            optional_members,
        )

    def list_roles(self, domain_id: str, client_id: str, query_params: dict, token: str):
        return self.__roles.list_roles(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            query_params,
            token,
        )

    def get_role(self, domain_id: str, client_id: str, role_id: str, token: str):
        return self.__roles.get_role(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            token,
        )

    def update_role(
        self, domain_id: str, client_id: str, role_id: str, role: dict, token: str
    ):
        return self.__roles.update_role(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            role,
            token,
        )

    def delete_role(self, domain_id: str, client_id: str, role_id: str, token: str):
        return self.__roles.delete_role(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            token,
        )

    def add_role_actions(
        self, domain_id: str, client_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.add_role_actions(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            actions,
            token,
        )

    def list_role_actions(
        self, domain_id: str, client_id: str, role_id: str, token: str
    ):
        return self.__roles.list_role_actions(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            token,
        )

    def delete_role_actions(
        self, domain_id: str, client_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.delete_role_actions(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            actions,
            token,
        )

    def delete_all_role_actions(
        self, domain_id: str, client_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_actions(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            token,
        )

    def add_role_members(
        self, domain_id: str, client_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.add_role_members(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            members,
            token,
        )

    def list_role_members(
        self, domain_id: str, client_id: str, role_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_role_members(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            query_params,
            token,
        )

    def delete_role_members(
        self, domain_id: str, client_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.delete_role_members(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            members,
            token,
        )

    def delete_all_role_members(
        self, domain_id: str, client_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_members(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            role_id,
            token,
        )

    def list_members(
        self, domain_id: str, client_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_entity_members(
            self.URL + "/" + domain_id,
            self.CLIENTS_ENDPOINT,
            client_id,
            query_params,
            token,
        )
