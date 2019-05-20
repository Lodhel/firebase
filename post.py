import requests
import json

key = 'ваш ключ'
url = 'http://fcm.googleapis.com/fcm/send'

headers = {'Content-type': 'application/json',
           'Authorization': 'key={}'.format(key)
           }

data = {
    "notification": {
        'title': 'заголовок',
        'subtitle': 'подзаголовок',
        'body': "тело",
        'sound': None,
        'badge': None,

    },
    'dry_run': False,  # булеаой флажок тестирования запроса

    'priority': 'high',
    'content_available': True,
    "to": 'куда',

}
answer = requests.post(url, json=data, headers=headers)
print(answer.text)
print(answer.status_code)