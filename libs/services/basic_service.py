import requests
from abc import ABC


class BasicService:

    def __init__(self, base_url):

        self.base_url = base_url

    def request(self, method='GET', path='', data=None, headers=None, params=None):

        response = None
        try:
            response = requests.request(
                method=method,
                url=f'{self.base_url}/{path}',
                data=data,
                headers=headers,
                params=params
            )
        except requests.exceptions.RequestException as ex:
            print(ex)

        return response.json()

