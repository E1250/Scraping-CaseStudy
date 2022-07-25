import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest

url = "https://wuzzuf.net/search/jobs/?q=python&a=hpb"
titles = []
c_names = []
l_names = []
j_skills = []
links = []

# fetch html url
results = requests.get(url)

soup = BeautifulSoup(results.text, "lxml")
"""
print(soup) # print html code
print(soup.prettify()) # print html code in pretty format
"""

job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", {"class": "css-17s97q8"})
location_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})


for i in range(len(company_names)):
    print(job_titles[i].text)
    print(company_names[i].text)
    print(location_names[i].text)
    print(job_skills[i].text)
    print("\n")

    titles.append(job_titles[i].text)
    c_names.append(company_names[i].text)
    l_names.append(location_names[i].text)
    links.append(job_titles[i].find("a")["href"])
    j_skills.append(job_skills[i].text)

"""
these links are unabled to be scraped from wuzzuf

for link in links:
    url = "https://www.wuzzuf.net"+links[0]
    results = requests.get(url)
    soup = BeautifulSoup(results.content, "html.parser")
    print(soup.prettify())
    salary = soup.find("span", {"class": "css-wn0avc"})
    print(salary)
    # print("\n")
"""
# write to csv file
with open("wuzuf_scraping.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Company Name", "Location", "Skills","Links"])
    for i in range(len(titles)):
        writer.writerow([titles[i], c_names[i], l_names[i], j_skills[i],links[i]])
