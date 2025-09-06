#Alexey Mishin
#Cs490-101
#Exercise 1
import sys
import requests

API_URL = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

#Payload with Data
payload = {
    "UCID": "am488",
    "first_name": "Alexey",
    "last_name": "Mishin",
    "github_username": "AlexeyMish7",
    "discord_username": "alexm488",
    "favorite_cartoon": "SpongeBob SquarePants",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Project Hail Mary",
    "section": "101"
}

#POST
def post():
    print("POST  student info...")
    r = requests.post(API_URL, json=payload, timeout=20)
    print("Status:", r.status_code)
    print("Body:", r.text)
    r.raise_for_status()

#GET
def get():
    print("GET student info...")
    params = {"UCID": payload["UCID"], "section": payload["section"]}
    r = requests.get(API_URL, params=params, timeout=20)
    print("Status:", r.status_code)
    print("Body:", r.text)
    r.raise_for_status()

#PUT
def put():
    print("PUT student info...")
    r = requests.put(API_URL, json=payload, timeout=20)
    print("Status:", r.status_code)
    print("Body:", r.text)
    r.raise_for_status()

#DELETE
def delete():
    print("DELETE student info...")
    params = {"UCID": payload["UCID"], "section": payload["section"]}
    r = requests.delete(API_URL, params=params, timeout=20)
    print("Status:", r.status_code)
    print("Body:", r.text)
    r.raise_for_status()

if __name__ == "__main__":
    # Check if the user typed an action after the script name
    if len(sys.argv) > 1:
        action = sys.argv[1].lower()  # take whatever they typed (post, get, put, delete)
    else:
        action = "post"  # default to "post" if nothing was typed

    #Run whichever method the user puts in or alert them the action is unknown
    try:
        if action == "post":
            post()
        elif action == "get":
            get()
        elif action == "put":
            put()
        elif action == "delete":
            delete()
        else:
            print("Unknown action. Use: post | get | put | delete")
    except requests.RequestException as e:
        print("Request failed:", e)

