from bs4 import BeautifulSoup
import requests
import time

# https://www.timesjobs.com/
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

print("Put some skills that you are not failair with")
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', {'class':"clearfix job-bx wht-shd-bx"})
    for index,job in enumerate(jobs):
        published_date = job.find( 'span', {'class': "sim-posted"}).span.text.replace(" ", "")
        if('few' in published_date):
            company_name = job.find("h3", {'class': 'joblist-comp-name'}).text.replace(" ","")
            skills = job.find('span', {'class':"srp-skills"}).text.replace(" ","")
            more_info = job.header.h2.a
            #more_info = job.header.h2.a.get("href")
            #more_rstinfo = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"{company_name.strip()} \n")
                    f.write(f"{skills.strip()} \n")
                    f.write(f"{more_info.get('href')}")
                    f.close()
                print("File Saved")


                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More info: {more_info.get('href')}")
                print(" ")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting for {time_wait} minutes..... ")
        time.sleep(time_wait*60)
