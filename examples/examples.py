from magistrala import sdk
import json

default_url = "http://localhost"

mfsdk = sdk.SDK(
    users_url=default_url,
    clients_url=default_url + ":9000",
    reader_url=default_url + ":9011",
    http_adapter_url=default_url,
    certs_url=default_url + ":9019",
    bootstrap_url=default_url + ":9013"
)

"""Repetitive values that can be easily fed into the example code"""

email = "<email>",
password = "<password>",
user_id =  "<user_id>",
token =  "<access_token>",
refresh_token = "<refresh_token>",
client_id = "<client_id>",
client_id2 = "<client_id2>",
channel_id = "<channel_id>",
channel_id2 = "<channel_id2>",
group_id = "<group_id>",

"""To start working with the Magistrala system,
you need to create a user account"""
mf_resp = mfsdk.users.create(
    user={"credentials": {"identity": "<user_identity>", "secret": password}},
    token= token,
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To log in to the Magistrala system, you need to create a user token"""
mf_resp = mfsdk.users.login(
    user={ "identity" : "<user_identity>", "secret": password}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Refreshes Access and Refresh Token used for authenticating into the system."""

mf_resp = mfsdk.users.refresh_token(
    refresh_token= refresh_token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can always check the user entity that is logged in
by entering the user ID and token"""
mf_resp = mfsdk.users.get(user_id= user_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user entities in the database"""
user = {
    "id":  user_id,
    "name": "<user_name>",
    "metadata": {
        "foo": "bar"
    }
}
mf_resp = mfsdk.users.update(user_token= token, user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user identity in the database"""
user = {
  "credentials": {
    "identity": "<new_user_identity>",
  },
  "id":  user_id
}
mf_resp = mfsdk.users.update_user_identity(user_token= token, user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user tags in the database"""
user = {
  "id":  user_id,
  "name": "<user_name>",
  "tags": [
    "yellow",
    "orange"
  ]
}
mf_resp = mfsdk.users.update_user_tags(user_token= token, user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates user owner in the database"""
user = {
  "credentials": {
    "identity": "<user_identity>",
    "secret": password,
  },
  "id":  user_id,
  "owner": "<owner_id>"
}
mf_resp = mfsdk.users.update_user_owner(user_token= token, user=user)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""User Password reset request"""
mf_resp = mfsdk.users.reset_password_request(email= email, url= "http://localhost/reset-request")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""User Password reset with the reset_request token"""
mf_resp = mfsdk.users.reset_password(password="<password>", confirm_password="<confirm_password>", token=  token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all users in the database by calling the get_all () function"""
mf_resp = mfsdk.users.get_all(
    query_params={"offset": 0, "limit": 5},
    user_token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
  
"""Disables user"""
mf_resp = mfsdk.users.disable(user_id= user_id, user_token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Enables user"""
mf_resp = mfsdk.users.enable(user_id= user_id, user_token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Changing the user password can be done by calling the update password function"""
mf_resp = mfsdk.users.update_password(
    old_secret="<old_secret>", new_secret="<new_secret>",
    user_token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Authorising a User"""
access_request = {
    "subject":  user_id,
    "object": group_id,
    "action": "<action>",
    "entity_type": "<entity_type>"
}
mf_resp = mfsdk.users.authorise_user(access_request=access_request, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Authorising a Client"""
access_request = {
    "subject": client_id,
    "object": channel_id,
    "action": "<action>",
    "entity_type": "<entity_type>"
}
mf_resp = mfsdk.clients.authorise_client(access_request=access_request, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a client, you need the client name and a user token"""
mf_resp = mfsdk.clients.create(
    client={"name": "<client_name>"}, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can create multiple clients at once
by entering a series of clients structures and a user token"""
mf_resp = mfsdk.clients.create_bulk(
    clients=[{"name": "<client_name>"}, {"name": "<client_name>"}, {"name": "<client_name>"}],
    token= token,
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get client information by entering the client ID and user token"""
mf_resp = mfsdk.clients.get(client_id= client_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all clients in the database by calling the get_all () function"""
mf_resp = mfsdk.clients.get_all(
    query_params={"offset": 0, "limit": 5}, token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a client entity in a database"""
mf_resp = mfsdk.clients.update(
    client_id=client_id, token= token, client={"name": "<client_name>"}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a client secret in a database"""
mf_resp = mfsdk.clients.update_client_secret(
    client_id=client_id, token= token, client={"secret": password}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a client's tags in a database"""
client=  {
    "id": client_id,
    "name": "<client_name>",
    "tags": [
    "dev","back"
    ]
  }
mf_resp = mfsdk.clients.update_client_tags(
    client_id=client_id, token= token, client=client
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updates a client's owner"""
client=  {
    "id": client_id,
    "name": "<client_name>",
    "owner": "<owner_id>",
}
mf_resp = mfsdk.clients.update_client_owner(
    client_id=client_id, token= token, client=client
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all client connected to channel"""
mf_resp = mfsdk.clients.get_by_channel(
    channel_id=channel_id,
    query_params={"offset": 1, "limit": 5},
    token=token,
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To disable a client you need a client ID and a user token"""
mf_resp = mfsdk.clients.disable(client_id=client_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect client to channel"""
mf_resp = mfsdk.clients.connect(
    channel_id=channel_id, client_id=client_id, action="<action>", token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect client from channel"""
mf_resp = mfsdk.clients.disconnect(
    channel_id=channel_id, client_id=client_id, token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Connect clients to channels"""
mf_resp = mfsdk.clients.connects(
    client_ids=[client_id, client_id2],
    channel_ids=[channel_id, channel_id2],
    actions="<action>",
    token= token,
)

if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Disconnect clients from channels"""
mf_resp = mfsdk.clients.disconnects(
    client_ids=[client_id, client_id2],
    channel_ids=[channel_id, channel_id2],
    token=token,
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Share client"""
mf_resp = mfsdk.clients.share_client(
    channel_id= channel_id, 
    user_id=  user_id, 
    actions= ["<actions>"], 
    token= token,
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message) 

"""To create a channel, you need a channel and a token"""
mf_resp = mfsdk.channels.create(
    channel={"name": "<channel_name>"}, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""As with clients, you can create multiple channels at once"""
mf_resp = mfsdk.channels.create_bulk(
    channels=[{"name": "<channel_name>"}, {"name": "<channel_name>"}],
    token= token,
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""Update channel entities in the database"""
mf_resp = mfsdk.channels.update(
    channel_id=channel_id,
    token= token,
    channel={"name": "<channel_name>"},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get channel information by entering the channel ID and user token"""
mf_resp = mfsdk.channels.get(token= token, channel_id=channel_id)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get all channels in the database by calling the get_all ()
function"""
mf_resp = mfsdk.channels.get_all(
    query_params={"offset": 0, "limit": 5}, token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""A list of all the channels to which a given client is connected"""
mf_resp = mfsdk.channels.get_by_client(
    client_id=client_id, query_params={"offset": 0, "limit": 5},
    token= token
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Identifies client when given client key"""
mf_resp = mfsdk.channels.identify_client(client_key="<client_secret>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Delete channels from the database"""
mf_resp = mfsdk.channels.disable(
    channel_id=channel_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""To create a group, you need the group name and a user token"""
mf_resp = mfsdk.groups.create(
    group={"name": "group_name"}, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get group information by entering the group ID and token"""
mf_resp = mfsdk.groups.get(group_id= group_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Group update"""
group={
    "id": group_id,
    "name": "<group_name>",
    "metdata": {
        "foo": "bar"
    }
 }
mf_resp = mfsdk.groups.update(
    token= token, group= group, group_id="group_id"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""You can get groups in the database by calling the get_all () function"""
mf_resp = mfsdk.groups.get_all(
    token= token, query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Assign user to a group"""
mf_resp = mfsdk.groups.assign(
    group_id=group_id,
    token= token,
    member_id="<member_id>",
    member_type=["<member_type>"],
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Unassign"""
mf_resp = mfsdk.groups.unassign(
    group_id="<object>",
    token= token,
    members_ids="<subject>",
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of children from group"""
mf_resp = mfsdk.groups.children(
    group_id=group_id, token= token,
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of parents from group"""
mf_resp = mfsdk.groups.parents(
    group_id=group_id, token= token,
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of members from group"""
mf_resp = mfsdk.groups.members(
    group_id=group_id, token= token,
    query_params={"offset": 0, "limit": 5}
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Get list of memberships from member"""
mf_resp = mfsdk.groups.memberships(
    member_id="<member_id>",
    token= token,
    query_params={"offset": 0, "limit": 5},
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Delete group from the database"""
mf_resp = mfsdk.groups.disable(group_id=group_id, user_token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Sends message via HTTP protocol"""
mf_resp = mfsdk.messages.send(
    channel_id=channel_id, msg='[<message>]', client_key="<client_secret>"
)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Reads messages from database for a given channel"""
mf_resp = mfsdk.messages.read(channel_id=channel_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Issue certs"""
mf_resp = mfsdk.certs.issue(client_id=client_id,valid="<time_limit>", token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
 
"""View Certs"""
mf_resp = mfsdk.certs.view_by_client(client_id=client_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
    
"""View Certs"""
mf_resp = mfsdk.certs.view_by_serial(cert_id="<cert_id>", token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Revoke Certs"""
mf_resp = mfsdk.certs.revoke(client_id=client_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Adds new config to the list of config owned by user identified using the provided access token."""
config = {
   "external_id": "<external_id>",
  "external_key": "<external_key>",
  "client_id": client_id,
  "name": "<name>"
}
mf_resp = mfsdk.bootstrap.add(config=config, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Updating state represents enabling/disabling Config, i.e.connecting and disconnecting corresponding Magistrala Client to the list of Channels."""
config = {
   "external_id": "<external_id>",
  "external_key": "<external_key>",
  "client_id": client_id,
  "name": "<name>"
}
mf_resp = mfsdk.bootstrap.whitelist(config=config, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message) 
 
"""Retrieves a configuration with given config id"""
mf_resp = mfsdk.bootstrap.view(client_id= client_id, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)  
  
"""Update is performed by replacing the current resource data with values provided in a request payload. Note that the owner, ID, external ID, external key, Magistrala Client ID and key cannot be changed."""
config = {
 "external_id": "<external_id>",
  "external_key": "<external_key>",
  "client_id": client_id,
  "name": "<name>"
}
mf_resp = mfsdk.bootstrap.update(config=config, token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message) 
   
"""Retrieves a configuration with given external ID and external key."""
mf_resp = mfsdk.bootstrap.bootstrap(external_id="<external_id>", external_key= "<external_key>")
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

"""Removes a Config. In case of successful removal the service will ensure that the removed config is disconnected from all the Magistrala channels."""
mf_resp = mfsdk.bootstrap.remove(config_id= "<config_id>", token= token)
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
