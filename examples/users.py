# Copyright (c) Abstract Machines
# SPDX-License-Identifier: Apache-2.0

from magistrala import sdk

default_url = "http://localhost"

mgsdk = sdk.SDK(
    users_url=default_url + ":9002",
)

token = "<token>"
user_id = "<userId>"

resp = mgsdk.users.create(
    user={
        "first_name": "<firstName>",
        "last_name": "<lastName>",
        "email": "<email>",
        "credentials": {"username": "<username>", "secret": "<password>"},
    },
    token="",
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.login(
    user={"username": "<username>", "secret": "<password>"}
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.refresh_token(refresh_token="<refreshToken>")
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.get(user_id=user_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.get_profile(token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.get_all(query_params={"offset": 0, "limit": 10}, user_token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.search(query_params={"username": "<username>"}, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update(
    user={"id": user_id, "name": "<name>", "metadata": {"foo": "bar"}},
    user_token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update_user_identity(
    user={"id": user_id, "credentials": {"identity": "<newIdentity>"}},
    user_token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update_user_tags(
    user={"id": user_id, "tags": ["tag1", "tag2"]},
    user_token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update_username(
    user={"id": user_id, "credentials": {"username": "<newUsername>"}},
    user_token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update_profile_picture(
    user={"id": user_id, "profile_picture": "<url>"},
    user_token=token,
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update_password(
    old_secret="<oldPassword>", new_secret="<newPassword>", user_token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.reset_password_request(
    email="<email>", url="http://localhost/reset-request"
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.reset_password(
    password="<newPassword>", confirm_password="<newPassword>", token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.update_role(
    user={"id": user_id, "role": "<role>"}, user_token=token
)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.enable(user_id=user_id, user_token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.disable(user_id=user_id, user_token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.delete(user_id=user_id, token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.send_verification(token=token)
print(resp.value if resp.error.status == 0 else resp.error.message)

resp = mgsdk.users.verify_email(token="<verificationToken>")
print(resp.value if resp.error.status == 0 else resp.error.message)
