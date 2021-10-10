# key - 304747e89f2d4873a863f9f80d6e07f5

def listen(n):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    return speak.Speak(n)

if __name__ == '__main__':
    import requests
    import json
    intro = "\n Hello, Welcome here! Let's Read News." \
            "\nwhat do you want to listen ." \
            "\n0.Top Headlines" \
            "\n1.business" \
            "\n2.entertainment"  \
            "\n3.health " \
            "\n4.science" \
            "\n5.sports" \
            "\n6.technology"
    listen(intro);print(intro)
    inp = int(input("Enter your choice with choice number - "))
    if inp == 0:
        print("\n*************|Top Headlines|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(20):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    elif inp == 1:
        print("\n*************|Business News|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(10):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    elif inp == 2:
        print("\n*************|Entertainment News|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(1,10):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    elif inp == 3:
        print("\n*************|Health News|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(10):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    elif inp == 4:
        print("\n*************|Science News|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(10):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    elif inp == 5:
        print("\n*************|Sports News|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(10):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    elif inp == 6:
        print("\n*************|Technology News|***************")
        req = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=304747e89f2d4873a863f9f80d6e07f5")
        data = json.loads(req.content)
        for i in range(10):
            print(f"{i} - {data['articles'][i]['title']}")
            listen(data['articles'][i]['title'])
    else:
        print("Invalid Input!!")
print("Thanks for listening...`")

