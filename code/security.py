users = [
    {
        'id': 1,
        'username': 'ben',
        'password': '1234'

    }
]

username_mapping = { 'ben': {
        'id': 1,
        'username': 'ben',
        'password': '1234'
    }
}

userid_mapping = { 1: {
        'id': 1,
        'username': 'ben',
        'password': '1234'
    }
}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user