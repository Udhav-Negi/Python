import requests
from bs4 import BeautifulSoup
# response = requests.get('https://www.codewithharry.com')
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title" : 'foo', 
#     "body" : 'bar', 
#     "userId" : 1
# }

# headers = {
#     'Content-type' : 'application/json; charset=UTF-8', 
# }

# response = requests.post(url, headers=headers, json=data)
# print(response.text)


# Another Example 
url = "https://www.codewithharry.com/blogpost/stackery-international-shopping-guide-india/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for heading in soup.find_all("h2"):
    print(heading.text)