from urllib.parse import urlencode
from pip._vendor import requests
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
    

    

user1 = Users('b6224fa094f54ef3b6242b08db3e9414c5c7017538af0c0096da06758f8659da92cd633b52b4c68ace029')
user2 = Users('10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c')
print(user1.get_friends() & user2.get_friends())
