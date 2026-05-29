import requests

from magistrala import response
from magistrala import errors
from magistrala import utils
from magistrala.roles import Roles


class Channels:
    """Channels class provides the abstraction of the Magistrala Channels API.
    
    Channels are used to connect clients and users. They are used to send messages to clients and 
    receive messages from clients. Channels API provides the following functionalities:
        - create channel
        - create multiple channels in a bulk
        - get channel
        - get all channels
        - get all channels to which a specific client is connected to
        - update channel
        - delete channel
        - identify client
        
    Attributes: 
        CHANNELS_ENDPOINT (str): Channels API endpoint
        CLIENTS_ENDPOINT (str): Clients API endpoint
        IDENTIFY_ENDPOINT (str): Identify API endpoint
        
    """
    CHANNELS_ENDPOINT = "channels"
    CLIENTS_ENDPOINT = "clients"
    IDENTIFY_ENDPOINT = "identify"

    def __init__(self, url: str):
        """Initializes Channels class with the provided url

            Args:
                url (str): Magistrala Channels API URL
                
            returns:
                Channels: Channels object initialized with the provided url.
                
            raises:
                None
        """
        self.url = url
        self.__roles = Roles()

    def create(self, channel: dict, token: str):
        """Creates channel entity in the database
        
        Creates a new channel in the database when provided with a valid token.
        
        params:
            channel (dict): Channel entity to be created for example:
                {
                    "name": "channel_name",
                    "metadata": {
                        "description": "channel_description"
                    }
                }
            token (str): User's token
            
        returns:
            Response: Response object containing the response from the server
            
        Usage:
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channel = {
            ...    "name": "channel_name"
            ... }
            >>> mf_resp = mfsdk.channels.create(channel, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.CHANNELS_ENDPOINT,
            json=channel,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["create"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def create_bulk(self, channels: list, token: str):
        """Creates multiple channels in bulk
        
        Creates multiple new channels when provided with channels information
        and a valid token.
        
        params:
            channels: list- Channel entities to be created for example:
                [
                    {
                        "name": "channel_name",
                        "metadata": {
                            "description": "channel_description"
                        }
                    },
                    {
                        "name": "channel_name",
                        "metadata": {
                            "description": "channel_description"
                        }
                    }
                ]
                
            token (str): User's token
        
        returns:
            Response: Response object containing the response from the server
            
        Usage:
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channels = [
            ...    {
            ...        "name": "channel_name"
            ...    },
            ...    {
            ...        "name": "channel_name"
            ...    }
            ... ]
            >>> mf_resp = mfsdk.channels.create_bulk(channels, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/bulk",
            json=channels,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["create_bulk"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get(self, channel_id: str, token: str):
        """Gets a channel entity for a logged-in user
        
        Provides a channel entity when provided with a valid channel ID and token.
        
        params: 
            channel_id (str): Channel ID
            token (str): User's token
            
        returns:
            Response: Response object
            
        Usage:

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channel_id = "channel_id"
            >>> mf_resp = mfsdk.channels.get(channel_id, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/" + channel_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, query_params: dict, token: str):
        """Gets all channels from database
        
        Gets all channels from database when provided with a valid token..
        
        params:
            query_params (dict): Query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
            token (str): User's token
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> query_params = {
            ...    "offset": 0,
            ...    "limit": 10
            ... }
            >>> mf_resp = mfsdk.channels.get_all(query_params, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.CHANNELS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get_all"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_by_client(self, client_id: str, query_params: dict, token: str):
        """Gets all channels to which a specific client is connected to.
        
        Provides a list of all the channels a client is connected to when provided with a valid
        token and client ID.
        
        params:
            client_id (str): Client ID
            query_params (dict): Query parameters for example:
                {
                    "offset": 0,
                    "limit": 10
                }
            token (str): User's token
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> client_id = "client_id"
            >>> query_params = {
            ...    "offset": 0,
            ...    "limit": 10
            ... }
            >>> mf_resp = mfsdk.channels.get_by_client(client_id, query_params, token)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.CLIENTS_ENDPOINT + "/" + client_id + "/" + self.CHANNELS_ENDPOINT,
            headers=utils.construct_header(token, utils.CTJSON),
            params=query_params,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["get_by_client"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, channel_id: str, channel: dict, token: str):
        """Updates channel entity
        
        Updates a channel entity when provided with a valid channel ID, channel entity and token.
        The information that can be updated are channel's name and metadata.
        
        params:
            channel_id (str): Channel ID
            channel (dict): Channel entity to be updated for example:
                {
                    "name": "channel_name",
                    "metadata": {
                        "description": "channel_description"
                    }
                }
            token (str): User's token
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> channel_id = "channel_id"
            >>> channel = {
            ...    "name": "channel_name"
            ... }
            >>> mf_resp = mfsdk.channels.update(channel_id, channel, token)
            >>> mf_resp
        """
        http_resp = requests.put(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/" + channel_id,
            json=channel,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def disable(self, channel_id: str, token: str):
        """Deletes a channel entity from database.
        
        Deletes a channel entity from database when provided with a valid channel ID and token.
        The channel is not deleted from the database but is marked as disabled.
        
        params:

            channel_id (str): Channel ID
            token (str): User's token
            
        returns:

            mf_resp: response.Response -response object
            
        Usage:
            
                >>> from magistrala import sdk
                >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
                >>> channel_id = "channel_id"
                >>> mf_resp = mfsdk.channels.disable(channel_id, token)
                >>> mf_resp
        """
        http_resp = requests.post(
            self.url + "/" + self.CHANNELS_ENDPOINT + "/" + channel_id + "/disable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["delete"], http_resp.status_code
            )
        return mf_resp

    def identify_client(self, client_key: str):
        """Validates client's key and returns it's ID if key is valid
        
        Uses a client_key or secret to validate a client and provide its information.
        
        params:
            client_key (str): Client's key
            
        returns:
            mf_resp: response.Response -response object
            
        Usage:
        
            >>> from magistrala import sdk    
            >>> mfsdk = sdk.SDK(channels_url="http://localhost:9000")
            >>> client_key = "client_key"
            >>> mf_resp = mfsdk.channels.identify_client(client_key)
            >>> mf_resp
        """
        http_resp = requests.post(
            self.url + "/" + self.IDENTIFY_ENDPOINT,
            headers=utils.construct_header(utils.ClientPrefix + client_key, utils.CTJSON),
        )
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["identify_client"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def enable(self, channel_id: str, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id
            + "/enable",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["enable"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete(self, channel_id: str, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["delete"], http_resp.status_code
            )
        else:
            mf_resp.value = "Channel deleted successfully"
        return mf_resp

    def update_tags(self, channel_id: str, channel: dict, domain_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.patch(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id
            + "/tags",
            headers=utils.construct_header(token, utils.CTJSON),
            json=channel,
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["update"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def connect_client(
        self,
        client_ids: list,
        channel_id: str,
        connection_types: list,
        domain_id: str,
        token: str,
    ):
        """Connects clients to a single channel."""
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id
            + "/connect",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"client_ids": client_ids, "types": connection_types},
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["connect"], http_resp.status_code
            )
        else:
            mf_resp.value = "connected"
        return mf_resp

    def disconnect_client(
        self,
        client_ids: list,
        channel_id: str,
        connection_types: list,
        domain_id: str,
        token: str,
    ):
        """Disconnects clients from a single channel."""
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id
            + "/disconnect",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"client_ids": client_ids, "types": connection_types},
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["disconnect"], http_resp.status_code
            )
        else:
            mf_resp.value = "Disconnected"
        return mf_resp

    def set_parent_group(
        self, domain_id: str, channel_id: str, parent_group_id: str, token: str
    ):
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id
            + "/parent",
            headers=utils.construct_header(token, utils.CTJSON),
            json={"parent_group_id": parent_group_id},
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["set_parent_group"], http_resp.status_code
            )
        else:
            mf_resp.value = "Parent group set successfully"
        return mf_resp

    def delete_parent_group(self, domain_id: str, channel_id: str, token: str):
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url
            + "/"
            + domain_id
            + "/"
            + self.CHANNELS_ENDPOINT
            + "/"
            + channel_id
            + "/parent",
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.channels["delete_parent_group"], http_resp.status_code
            )
        else:
            mf_resp.value = "Parent group removed successfully"
        return mf_resp

    # Role management

    def list_available_actions(self, domain_id: str, token: str):
        return self.__roles.list_available_actions(
            self.url + "/" + domain_id, self.CHANNELS_ENDPOINT, token
        )

    def create_role(
        self,
        domain_id: str,
        channel_id: str,
        role_name: str,
        token: str,
        optional_actions: list = None,
        optional_members: list = None,
    ):
        return self.__roles.create_role(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_name,
            token,
            optional_actions,
            optional_members,
        )

    def list_roles(
        self, domain_id: str, channel_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_roles(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            query_params,
            token,
        )

    def get_role(self, domain_id: str, channel_id: str, role_id: str, token: str):
        return self.__roles.get_role(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            token,
        )

    def update_role(
        self, domain_id: str, channel_id: str, role_id: str, role: dict, token: str
    ):
        return self.__roles.update_role(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            role,
            token,
        )

    def delete_role(self, domain_id: str, channel_id: str, role_id: str, token: str):
        return self.__roles.delete_role(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            token,
        )

    def add_role_actions(
        self, domain_id: str, channel_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.add_role_actions(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            actions,
            token,
        )

    def list_role_actions(
        self, domain_id: str, channel_id: str, role_id: str, token: str
    ):
        return self.__roles.list_role_actions(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            token,
        )

    def delete_role_actions(
        self, domain_id: str, channel_id: str, role_id: str, actions: list, token: str
    ):
        return self.__roles.delete_role_actions(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            actions,
            token,
        )

    def delete_all_role_actions(
        self, domain_id: str, channel_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_actions(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            token,
        )

    def add_role_members(
        self, domain_id: str, channel_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.add_role_members(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            members,
            token,
        )

    def list_role_members(
        self,
        domain_id: str,
        channel_id: str,
        role_id: str,
        query_params: dict,
        token: str,
    ):
        return self.__roles.list_role_members(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            query_params,
            token,
        )

    def delete_role_members(
        self, domain_id: str, channel_id: str, role_id: str, members: list, token: str
    ):
        return self.__roles.delete_role_members(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            members,
            token,
        )

    def delete_all_role_members(
        self, domain_id: str, channel_id: str, role_id: str, token: str
    ):
        return self.__roles.delete_all_role_members(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            role_id,
            token,
        )

    def list_members(
        self, domain_id: str, channel_id: str, query_params: dict, token: str
    ):
        return self.__roles.list_entity_members(
            self.url + "/" + domain_id,
            self.CHANNELS_ENDPOINT,
            channel_id,
            query_params,
            token,
        )
