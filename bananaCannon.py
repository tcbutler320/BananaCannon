import requests 
import sys
import os

banner = '''
  ____                                
 | __ )  __ _ _ __   __ _ _ __   __ _ 
 |  _ \ / _` | '_ \ / _` | '_ \ / _` |
 | |_) | (_| | | | | (_| | | | | (_| |
 |____/ \__,_|_| |_|\__,_|_| |_|\__,_|
  / ___|__ _ _ __  _ __   ___  _ __   
 | |   / _` | '_ \| '_ \ / _ \| '_ \  
 | |__| (_| | | | | | | | (_) | | | | 
  \____\__,_|_| |_|_| |_|\___/|_| |_| 
                  By: Tyler Butler 🍌
'''

usage = '{ERROR} Usage: python3 kingKong.py [username] [session uid] [authorization bearer]'
auth_bearer = '' # add your auth bearer
uid = '' # add your uid
username = '' 
userID = '' # add your user id


def inject_bananas():
    username = sys.argv[1]

    url = "https://us-central1-monkey-type.cloudfunctions.net:443/checkLeaderboards"
    headers = {
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\"",
        "Authorization": "Bearer "+ auth_bearer,
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://monkeytype.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://monkeytype.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close"
       }

    myjson = {
    "data": {
        "uid": uid,
        "lbMemory": {
            "time15": {
                "global": None,
                "daily": None
            },
            "time60": {
                "global": None,
                "daily": None
            }
        },
        "name": username,
        "banned": None,
        "verified": None,
        "discordId": None,
        "result": {
            "wpm": 200.00,
            "rawWpm": 200.00,
            "correctChars": 250,
            "incorrectChars": 6,
            "allChars": 250,
            "acc": 92,
            "mode": "time",
            "mode2": 15,
            "quoteLength": -1,
            "punctuation": False,
            "numbers": False,
            "timestamp": 1622147912060,
            "language": "english",
            "restartCount": 0,
            "incompleteTestSeconds": 0,
            "difficulty": "normal",
            "testDuration": 15.001134999999515,
            "afkDuration": 0,
            "blindMode": False,
            "theme": "9009",
            "tags": [],
            "consistency": 83.22,
            "keyConsistency": 45.56,
            "funbox": "none",
            "bailedOut": False,
            "customText": None,
            "uid": uid,
            "id": userID
                }
            }
        }
    print('{!} ------ Injecting New Bananas')
    try:
        requests.post(url, headers=headers, json=myjson)
        print('{!} ------ Success! Welcome to the leaderboard 🙊')
    except requests.exceptions.RequestException as e:  
        print('{ERROR} ------ Oops we made a mistake, back to the zoo')
        print('{ERROR}',e)

    return

def main():
    if len(sys.argv) < 2:
        print(usage)
        sys.exit(0)
    else: 
        print(banner,'\n{!} Starting Banana Handler for user',sys.argv[1])
        inject_bananas()
    sys.exit(0)

if __name__ == "__main__":
    main()