import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = "sender_id=TXTIND&message=This is a test message&route=v3&numbers=6383664520"
headers = {
    'authorization': "tglhqzDde7CSJOiGvYy9RAXVjmIua6P51WkFp4bLs3U2rKT0wZrNtasovd1CIPKRzUcAgkTZ9bHjhWBy",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
