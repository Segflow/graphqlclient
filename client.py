import requests
import json

class GraphQLClient:
    def __init__(self, endpoint, token=None):
        self.endpoint = endpoint
        self.token = token

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token):
        self.token = token

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers['Authorization'] = 'Bearer %s' % self.token

        try:
            response = requests.post(self.endpoint, data=json.dumps(data), headers=headers)
            # print(response.text)
            return response.json()
        except requests.RequestException as e:
            print(e.read())
            print('')
            raise e
