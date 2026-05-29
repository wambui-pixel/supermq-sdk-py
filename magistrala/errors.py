def handle_error(error_dict, status_code):
    if status_code in error_dict.keys():
        return error_dict[status_code]
    elif status_code in errors.keys():
        return errors[status_code]
    else:
        return "Unknown error"


errors = {
    400: "Failed due to malformed JSON.",
    401: "Missing or invalid access token provided.",
    403: "Missing or invalid access token provided.",
    404: "A non-existent entity request.",
    409: "Entity already exist.",
    415: "Missing or invalid content type.",
    422: "Database can't process request.",
    500: "Unexpected server-side error occurred.",
}

users = {
    "create": {
        409: "Failed due to using an existing identity.",
    },
    "login": {
        409: "Failed due to using an existing email address.",
    },
    "refresh_token": {
        404: "A non-existent entity request.",
    },
    "get": {
        400: "Failed due to malformed query parameters.",
    },
    "get_all": {
        400: "Failed due to malformed query parameters.",
    },
    "update": {
        404: "Failed due to non existing user.",
    },
    "update_user_identity": {
        401: "Missing or invalid access token provided.",
    },
    "update_user_tags": {
        401: "Missing or invalid access token provided.",
    },
    "update_user_owner": {
        401: "Missing or invalid access token provided.",
    },
    "enable": {
        404: "Failed due to non existing user."
    },
    "disable": {
        404: "Failed due to non existing user."
    },
    "reset_password_request": {
        400: "Failed due to malformed JSON."
    },
    "reset_password": {
        400: "Failed due to malformed JSON."
    },
    "authorise_user":{
        400: "Failed due to malformed JSON."
    }
}

clients = {
    "create": {
        422: "Unprocessable Entity."
    },
    "create_bulk": {
    },
    "get": {
        400: "Failed due to malformed query parameters.",
        404: "Client does not exist.",
    },
    "get_all": {
        404: "Client does not exist.",
    },
    "get_by_channel": {
        400: "Failed due to malformed query parameters.",
    },
    "update": {
        404: "Client does not exist.",
    },
    "update_client_secret": {
        401: "Missing or invalid access token provided.",
    },
    "update_client_tags": {
        401: "Missing or invalid access token provided.",
    },
    "update_client_owner": {
        401: "Missing or invalid access token provided.",
    },
    "delete": {
        400: "Failed due to malformed client's ID.",
    },
    "connect": {
        400: "A non-existent entity request."
    },
    "disconnect": {
        400: "Failed due to malformed query parameters.",
        404: "Channel or client does not exist.",
    },
    "share_thing": {
        400: "A non-existent entity request."
    },
    "authorise_thing":{
        403: "False",
    },
}

channels = {
    "create": {
        409: "Failed due to using an existing identity."
    },
    "create_bulk": {
        401: "Missing or invalid access token provided."
    },
    "get": {
        401: "Missing or invalid access token provided."
    },
    "get_all": {
        400: "Failed due to malformed channel's ID.",
        404: "Channel does not exist.",
    },
    "get_by_thing": {
        400: "Failed due to malformed query parameters.",
        404: "Client does not exist.",
    },
    "update": {
        404: "Channel does not exist."
    },
    "delete": {
        400: "Failed due to malformed channel's ID."
    },
    "identify_thing":{
        401: "Client and channel are not connected, or client with specified key doesn't exist."
    },
}

messages = {
    "send": {
        400: "Message discarded due to its malformed content.",
        403: "Message discarded due to missing or invalid credentials.",
        404: "Message discarded due to invalid channel id.",
        415: "Message discarded due to invalid or missing content type.",
    },
    "read": {
        400: "Failed due to malformed query parameters.",
    },
}

groups = {
    "create": {
        409: "Failed due to using an existing email address.",
    },
    "get": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "get_all": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "update": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "members": {
        409: "Failed due to using an existing email address.",
    },
    "memberships":{
        400: "Failed due to malformed query parameters."  
    },
    "parents": {
        400: "Failed due to malformed query parameters."
    },
    "children": {
        400: "Failed due to malformed query parameters."
    },
    "assign": {
        400: "Failed due to malformed JSON."
    }, 
    "unassign": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
    "disable": {
        400: "Failed due to malformed query parameters.",
        404: "Group does not exist.",
    },
}

bootstrap = {
    "add": {
        401: "Missing or invalid access token provided.",
    },
    "view": {
        404: "Config does not exist.",
    },
    "whitelist": {
        204: "Config removed.",
        400: "Failed due to malformed config's ID.",
    },
    "update": {
        404: "Config does not exist.",
    },
    "bootstrap": {
        404: "Failed to retrieve corresponding config."
    },
    "remove": {
        400: "Failed due to malformed config ID."
    } 
}
certs = {
    "issue": {
        401: "Missing or invalid access token provided.",
    },
    "view_by_thing": {
        404: "Failed to retrieve corresponding certificate.",
    },
    "view_by_serial": {
        404: "Failed to retrieve corresponding certificate.",
    },
    "revoke": {
        404: "Failed to revoke corresponding certificate.",
    },
    "serials": {
        404: "Failed to retrieve corresponding certificates.",
    },
}

domains = {
    "create": {
        409: "Failed due to using an existing domain name.",
    },
    "get": {
        404: "Domain does not exist.",
    },
    "list": {
        400: "Failed due to malformed query parameters.",
    },
    "update": {
        404: "Domain does not exist.",
    },
    "enable": {
        404: "Domain does not exist.",
    },
    "disable": {
        404: "Domain does not exist.",
    },
    "freeze": {
        404: "Domain does not exist.",
    },
    "send_invitation": {
        400: "Failed due to malformed JSON.",
    },
    "get_invitation": {
        404: "Invitation does not exist.",
    },
    "list_invitations": {
        400: "Failed due to malformed query parameters.",
    },
    "accept_invitation": {
        404: "Invitation does not exist.",
    },
    "reject_invitation": {
        404: "Invitation does not exist.",
    },
    "delete_invitation": {
        404: "Invitation does not exist.",
    },
}

health = {
    "check": {
        500: "Service is not healthy.",
    },
}

journal = {
    "list_by_entity": {
        400: "Failed due to malformed query parameters.",
        404: "Entity does not exist.",
    },
    "list_by_user": {
        400: "Failed due to malformed query parameters.",
        404: "User does not exist.",
    },
    "client_telemetry": {
        404: "Client does not exist.",
    },
}

pats = {
    "create": {
        400: "Failed due to malformed JSON.",
    },
    "get": {
        404: "PAT does not exist.",
    },
    "list": {
        400: "Failed due to malformed query parameters.",
    },
    "update_name": {
        404: "PAT does not exist.",
    },
    "update_description": {
        404: "PAT does not exist.",
    },
    "delete": {
        404: "PAT does not exist.",
    },
    "delete_all": {
        401: "Missing or invalid access token provided.",
    },
    "reset_secret": {
        404: "PAT does not exist.",
    },
    "revoke": {
        404: "PAT does not exist.",
    },
    "add_scope": {
        400: "Failed due to malformed JSON.",
    },
    "list_scopes": {
        400: "Failed due to malformed query parameters.",
    },
    "delete_scopes": {
        404: "Scope does not exist.",
    },
    "delete_all_scopes": {
        404: "PAT does not exist.",
    },
}

alarms = {
    "list": {
        400: "Failed due to malformed query parameters.",
    },
    "view": {
        404: "Alarm does not exist.",
    },
    "update": {
        404: "Alarm does not exist.",
    },
    "delete": {
        404: "Alarm does not exist.",
    },
}

rules = {
    "create": {
        400: "Failed due to malformed JSON.",
        422: "Unprocessable Entity.",
    },
    "view": {
        404: "Rule does not exist.",
    },
    "list": {
        400: "Failed due to malformed query parameters.",
    },
    "update": {
        404: "Rule does not exist.",
    },
    "update_tags": {
        404: "Rule does not exist.",
    },
    "update_schedule": {
        404: "Rule does not exist.",
    },
    "enable": {
        404: "Rule does not exist.",
    },
    "disable": {
        404: "Rule does not exist.",
    },
    "delete": {
        404: "Rule does not exist.",
    },
}

reports = {
    "generate": {
        400: "Failed due to malformed JSON.",
    },
    "add_config": {
        400: "Failed due to malformed JSON.",
        409: "Report config already exists.",
    },
    "get_config": {
        404: "Report config does not exist.",
    },
    "list_configs": {
        400: "Failed due to malformed query parameters.",
    },
    "update_config": {
        404: "Report config does not exist.",
    },
    "update_schedule": {
        404: "Report config does not exist.",
    },
    "delete_config": {
        404: "Report config does not exist.",
    },
    "enable_config": {
        404: "Report config does not exist.",
    },
    "disable_config": {
        404: "Report config does not exist.",
    },
    "update_template": {
        404: "Report config does not exist.",
    },
    "get_template": {
        404: "Report config does not exist.",
    },
    "delete_template": {
        404: "Report config does not exist.",
    },
}

roles = {
    "list_available_actions": {
        401: "Missing or invalid access token provided.",
    },
    "create_role": {
        400: "Failed due to malformed JSON.",
        409: "Role already exists.",
    },
    "list_roles": {
        400: "Failed due to malformed query parameters.",
    },
    "get_role": {
        404: "Role does not exist.",
    },
    "update_role": {
        404: "Role does not exist.",
    },
    "delete_role": {
        404: "Role does not exist.",
    },
    "add_role_actions": {
        400: "Failed due to malformed JSON.",
    },
    "list_role_actions": {
        404: "Role does not exist.",
    },
    "delete_role_actions": {
        404: "Role does not exist.",
    },
    "delete_all_role_actions": {
        404: "Role does not exist.",
    },
    "add_role_members": {
        400: "Failed due to malformed JSON.",
    },
    "list_role_members": {
        404: "Role does not exist.",
    },
    "delete_role_members": {
        404: "Role does not exist.",
    },
    "delete_all_role_members": {
        404: "Role does not exist.",
    },
    "list_entity_members": {
        400: "Failed due to malformed query parameters.",
    },
}

# Additional entries for new methods on existing modules
users["delete"] = {404: "User does not exist."}
users["send_verification"] = {400: "Failed due to malformed JSON."}
users["verify_email"] = {400: "Failed due to malformed JSON."}

clients["enable"] = {404: "Client does not exist."}
clients["set_parent_group"] = {400: "Failed due to malformed JSON."}
clients["delete_parent_group"] = {400: "Failed due to malformed query parameters."}

channels["enable"] = {404: "Channel does not exist."}
channels["connect"] = {400: "A non-existent entity request."}
channels["disconnect"] = {
    400: "Failed due to malformed query parameters.",
    404: "Channel or client does not exist.",
}
channels["set_parent_group"] = {400: "Failed due to malformed JSON."}
channels["delete_parent_group"] = {400: "Failed due to malformed query parameters."}

groups["enable"] = {404: "Group does not exist."}
groups["delete"] = {404: "Group does not exist."}
