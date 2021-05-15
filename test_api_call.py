import requests
import json
from requests.structures import CaseInsensitiveDict

class TestWeather():

    # def test_call_weather(self):
    #     try:
    #         url="http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=f73015b328a72a967dbf893df339e54f"
    #         response=requests.get(url)
    #         dict_reponse=json.loads(response.content)
    #         int_temp=dict_reponse['main']['temp']
    #         return int_temp
    #     except Exception as e:
    #         print(e + "Unable to call API request")

    def test_cowin(self):
        try:
            url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode=201301&date=13-05-2021"
            headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJmZmE5Njc2YS04ZDkxLTQyYzMtYTg4My04OGViZTY0ZGZlYWUiLCJ1c2VyX2lkIjoiZmZhOTY3NmEtOGQ5MS00MmMzLWE4ODMtODhlYmU2NGRmZWFlIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5ODczNDk5MDk1LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjczMTQ1NDM2MzY0ODgwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTAuMC40NDMwLjkzIFNhZmFyaS81MzcuMzYiLCJkYXRlX21vZGlmaWVkIjoiMjAyMS0wNS0xM1QwNDo1MzoyMi43MDdaIiwiaWF0IjoxNjIwODgxNjAyLCJleHAiOjE2MjA4ODI1MDJ9.IA_Yhjsyx26hx6elXKKn54yT1K9DOeiir5TkR2QESDI"}
            #headers:{'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJmZmE5Njc2YS04ZDkxLTQyYzMtYTg4My04OGViZTY0ZGZlYWUiLCJ1c2VyX2lkIjoiZmZhOTY3NmEtOGQ5MS00MmMzLWE4ODMtODhlYmU2NGRmZWFlIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5ODczNDk5MDk1LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjczMTQ1NDM2MzY0ODgwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTAuMC40NDMwLjkzIFNhZmFyaS81MzcuMzYiLCJkYXRlX21vZGlmaWVkIjoiMjAyMS0wNS0xM1QwNDo1MzoyMi43MDdaIiwiaWF0IjoxNjIwODgxNjAyLCJleHAiOjE2MjA4ODI1MDJ9.IA_Yhjsyx26hx6elXKKn54yT1K9DOeiir5TkR2QESDI'}
            response=str(requests.get(url,verify = False, headers=headers))
            print(response)

            #dict_reponse=json.loads(response.content)
            #print(dict_reponse)
        except Exception as e:
            print(e + "Unable to call API request")

