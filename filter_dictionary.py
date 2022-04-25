response = {
    "users": [
        {
            "name": "abc",
            "age": 25,
            "enabled": 'true'
        },
        {
            "name": "def",
            "age": 28,
            "enabled": 'false'
        },
        {
            "name": "ijk",
            "age": 32,
            "enabled": 'true'
        }
    ]
}

# for i in response['users']:
#     if i['enabled'] == 'true':
#         print(i)


for i in response['users']:
    if i['enabled'] == 'true':
        print(i)