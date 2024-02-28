# # from django.test import TestCase
#
# # Create your tests here.
# import requests
#
# data = {
#     'old_password': 'acts',
#     'new_password1': '123',
#     'new_password2': '123'
# }
# headers = {'Authorization': 'Bearer ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2NjkxNjU2LCJqdGkiOiIxMmQ5NzkxNmQxMzc0MGJmYjY1Nzk0NjEyNzdiZjFiNSIsInVzZXJfaWQiOjF9._g4MdCVaKQXOxuqExZ_4_zn4uk5RXG7fhKnAyOhgkPQ'}
# response = requests.post('http://192.168.1.79:8000/auth/change_password/', data=data, headers=headers)
# print(response.status_code)
# print(response.json())