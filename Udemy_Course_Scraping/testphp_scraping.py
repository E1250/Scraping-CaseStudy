import requests
from bs4 import BeautifulSoup

url = "http://testphp.vulnweb.com/"

req = requests.get(url)
print("Response Code : "+str(req))  # <Response [200]>
# Response [404] page not found

print(req.text) # HTML Code

# Saving HTML Code to a file
f = open("page.html","w")
f.write(req.text)
f.close()


# BeautifulSoup
soup = BeautifulSoup(req.text,"html.parser") #same as req.text

find = soup.find("h2")  # returns <h2> section
print(find.text) # print value of <h2>
print(find.prettify())

find = soup.find_all("div")  # returns all <div> sections
print(find.text)  # print value of <h2>
print(find.prettify())

######## Find By Id #########
find = soup.find(id='pageName')  # find by id
find = soup.find('h2',id='pageName')  # find by id & tag
find = soup.find_all(id='pageName')  # find by id 

######## Find By Class #########
find = soup.find(class_='story')  # find by class
find = soup.find_all(class_='story')  # find by class
find = soup.find('div',class_='story')  # find by class

