from urllib.parse import urlencode
from pip._vendor import requests
urrl = 'https://vk.com'
url = 'https://oauth.vk.com/authorize'
id = 7586347
oauth_params = {'client_id': id, 'display':'page', 'scope':'status', 'response_type': 'token', 'v': 5.122 }
print('?'.join((url, urlencode(oauth_params))))

friend_list = []

class Users:
    def __init__(self, token) -> None:
        self.token = token

    def get_friends(self):
        self.r = requests.get('https://api.vk.com/method/friends.get',
                         params=
                         {'access_token': self.token,
                          'v': 5.122})
        friends = self.r.json()['response']['items']
        return set(friends)

    def __and__(self, other_user):
        return print(self.get_friends() & other_user.get_friends())

    def get_id(self):
        self.r = requests.get('https://api.vk.com/method/users.get',
                         params=
                         {'access_token': self.token,
                          'v': 5.122})
        return print('/'.join((urrl,str(self.r.json()['response'][0]['id']))))


user1 = Users('42decf32f1faf52dd4ca866282320e4f5f6bffce5f54f63f6ab36cd0e93dc143d95ffd6a5a0313e544f04')
user2 = Users('10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c')
user1 & user2
user1.get_id()