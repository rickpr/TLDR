import os
import time

import jwt
import requests

class DownloadEula:
    def __init__(self, app_id: str) -> None:
        self.app_id  = app_id

    def download(self) -> str:
        return requests.get(
            # 'https://api.appstoreconnect.apple.com/v1/apps',
            f'https://api.appstoreconnect.apple.com/v1/apps/{self.app_id}/endUserLicenseAgreement' ,
            # f'https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/{self.app_id}' ,
            headers={ 'Authorization': f'Bearer {self._authorization_token()}' }
        )


    def _authorization_token(self) -> str:
        return jwt.encode(
            {
                'iss': os.environ['APPLE_ISSUER_ID'],
                'iat': int(time.time()),
                'exp': int(time.time()) + 600,
                'aud': 'appstoreconnect-v1'
            },
            open('AuthKey.p8').read(),
            algorithm = 'ES256',
            headers = {
                'alg': 'ES256',
                'kid': os.environ['APPLE_KEY_ID'],
                'typ': 'JWT'
            }
        )
