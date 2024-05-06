import requests
import json
print("1. Business")
print("2. Entertainment")
print("3. General")
print("4. Health")
print("5. Science")
print("6. Sports")
print("7. Technology")
x = int(input("Tell us the type of news you want to see. "))

match x:
    case 1 : 
        news = requests.get('https://newsapi.org/v2/top-headlines?category=business&apiKey=5ece9840967645baaeec4aabf7dc2914')
        # print(f"news for business is {json.loads(news.text)}")
        news = json.loads(news.text)
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])
            print("-----------------------------------------------------")
    case 2:
        news = requests.get('https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=5ece9840967645baaeec4aabf7dc2914')
        print(f"news for business is {news.text}")
    case 3:
        news = requests.get('https://newsapi.org/v2/top-headlines?category=general&apiKey=5ece9840967645baaeec4aabf7dc2914')
        print(f"news for business is {news.text}")
    case 4:
        news = requests.get('https://newsapi.org/v2/top-headlines?category=health&apiKey=5ece9840967645baaeec4aabf7dc2914')
        print(f"news for business is {news.text}")
    case 5:
        news = requests.get('https://newsapi.org/v2/top-headlines?category=science&apiKey=5ece9840967645baaeec4aabf7dc2914')
        print(f"news for business is {news.text}")
    case 5:
        news = requests.get('https://newsapi.org/v2/top-headlines?category=sports&apiKey=5ece9840967645baaeec4aabf7dc2914')
        print(f"news for business is {news.text}")
    case 5:
        news = requests.get('https://newsapi.org/v2/top-headlines?category=technology&apiKey=5ece9840967645baaeec4aabf7dc2914')
        print(f"news for business is {news.text}")
    case default:
        print("Please enter valid input")


# business entertainment general health science sports technology