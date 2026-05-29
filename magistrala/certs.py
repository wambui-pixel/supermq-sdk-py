import requests

from magistrala import response
from magistrala import errors
from magistrala import utils


class Certs:
    """Magistrala Certificates API
    
        Certs is used to issue, view, and revoke certificates.
        It is used to issue certificates for clients. 
        
        Args:
            url (str): Magistrala Certificates API URL.
            CERTS_ENDPOINT (str): Certificates API endpoint.
    """
    CERTS_ENDPOINT = "certs"

    def __init__(self, url: str):
        """Initializes Certs with the provided URL.
        
            Args:
                url (str): Magistrala Certificates API URL.
                
            Returns:
                Certs: Certs object.
        """
        self.url = url

    def issue(self, client_id: str, valid: str, token: str):
        """
        Issues a certificate for a given client ID.
        
        Args:
            client_id (str): Client ID.
            valid (str): Certificate validity period.
            token (str): Authorization token.
            
        Returns:
            Response: Magistrala response.
            
        Usage:
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(certs_url="http://localhost:9019")
            >>> client_id = "client_id"
            >>> valid = "1h"
            >>> mf_resp = mfsdk.certs.issue(client_id, valid)
            >>> mf_resp
        """ 
        payload = {
            "client_id": client_id,
            "ttl": valid,
        }
        mf_resp = response.Response()
        http_resp = requests.post(
            self.url + "/" + self.CERTS_ENDPOINT,
            json=payload,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["issue"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def view_by_client(self, client_id: str, token: str):
        """Retrieves a list of certificates' serial IDs for a given client ID.
        
        Provides a list of certificates' serial IDs for a given client ID.
        
        Params:
            client_id (str): Client ID.
            token (str): Authorization token.
            
        Returns:
            mf_resp : response.Response - response object.
            
        Usage:
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(certs_url="http://localhost:9019")
            >>> client_id = "client_id"
            >>> mf_resp = mfsdk.certs.view_by_thing(client_id)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/serials" + "/" + client_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["view_by_client"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp
    
    def view_by_serial(self, cert_id: str, token: str):
        """Retrieves a certificate for a given cert ID.
        
        Provides a certificate for a given cert ID.
        
        Params:

            cert_id (str): Certificate ID.
            token (str): Authorization token.
            
        Returns:
            mf_resp : response.Response - response object.
            
        Usage:

            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(certs_url="http://localhost:9019")
            >>> cert_id = "cert_id"
            >>> mf_resp = mfsdk.certs.view_by_serial(cert_id)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.get(
            self.url + "/" + self.CERTS_ENDPOINT + "/" + cert_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["view_by_serial"], http_resp.status_code
            )
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def revoke(self, client_id: str, token: str):
        """Revokes a certificate for a given client ID.
        
        Deletes a certificate for a given client ID and valid token.

        params:
            client_id (str): client id
            token (str): valid authorization token used to delete the certificate

        Returns:
            mf_resp : response.Response - response object.
            
        Usage:
        
            >>> from magistrala import sdk
            >>> mfsdk = sdk.SDK(certs_url="http://localhost:9019")
            >>> client_id = "client_id"
            >>> mf_resp = mfsdk.certs.revoke(client_id)
            >>> mf_resp
        """
        mf_resp = response.Response()
        http_resp = requests.delete(
            self.url + "/" + self.CERTS_ENDPOINT + "/" + client_id,
            headers=utils.construct_header(token, utils.CTJSON),
        )
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(
                errors.certs["revoke"], http_resp.status_code
            )
        else:
            mf_resp.value = "DELETED"
        return mf_resp
