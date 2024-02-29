import requests  # εισαγωγή της βιβλιοθήκης
import datetime

while(1):
    url = input("\nInsert the url: ")  # προσδιορισμός του url

    with requests.get(url) as response:
        Headers = response.headers
        print("\n1. The Response Headers are:", Headers)

    if "Server" in Headers:
        print("\n2. The Server for this url is:", Headers["Server"])
    else:
        print("\n2. There is No Server\n")

    if "Set-Cookie" in Headers:
        print("\n3. The Cookies of this url:")
        Cookies = response.cookies
        for cookie in Cookies:
            Name = cookie.name
            if cookie.expires != 0:
                print(Name + " which expires on", datetime.datetime.fromtimestamp(cookie.expires))
            else:
                print(Name +" which does not expire.\n")
    else:
        print("\n3. There are no Cookies\n")

    x = input ("\nDo you want to check another url? yes/no\n")
    if x == "no":
        break
    



