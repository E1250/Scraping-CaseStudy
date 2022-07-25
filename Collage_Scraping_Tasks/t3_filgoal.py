# open filgoal site through this link(https://www.filgoal.com/teams/1/matches?isResults=true&pageNumber=1) 
# get first 19 pagesNumbers till you reach to the first match for Pitso Mosimane with al ahly at: (4-10-2020) - which is: Al-Ahly VS El Mokawloon in the end of pageNumber 19.

# Now, let's have fun:

# get all goals that Al-Ahly scored through all 19 pages, save all goals in numpy array with name ['AL-AHLY-S'] and print these statistics:
# average number of goals that Al-Ahly scored
# all number of goals that al ahly scored
# max number of goals scored in one match

# then:
# get all goals that Al-Ahly received through all 19 pages, save all goals in numpy array with name ['AL-AHLY-R'] and print these statistics:
# average number of goals that Al-Ahly received
# all number of goals that al ahly received
# max number of goals received in one match


from cgitb import strong
import requests
import numpy as np
from bs4 import BeautifulSoup as bs

def remove_sign(text):
    if ')' in text:
        return int(text.split(")")[1].strip())
    else:
        return int(text)

fromPage = 1
toPage = 19

al_ahly_s = []
al_ahly_r = []

for page in range(fromPage,toPage+1):
    url = 'https://www.filgoal.com/teams/1/matches?isResults=true&pageNumber='+str(page)
    response = requests.get(url)
    assert response.status_code, 200
    page = bs(response.content, 'html.parser')
    cf_matches = page.find_all('div', class_='cin_cntnr')

    for match in cf_matches:
        goals1 = match.find('div', class_='f')
        f = goals1.find('b')

        goals2 = match.find('div', class_='s')
        b = goals2.find('b')

        if goals1.find('strong').text == "الأهلي":
            if f.text.strip() != "-" and b.text.strip() != "-":
                al_ahly_s.append(remove_sign(f.text))
                al_ahly_r.append(remove_sign(b.text))
        else:
            if f.text != "-" and b.text != "-":
                al_ahly_r.append(remove_sign(f.text))
                al_ahly_s.append(remove_sign(b.text))

print("Al_Ahly Scores:")
arr_s = np.array(al_ahly_s, dtype=np.int64)
print("Average : ",np.average(arr_s))
print("Sum : ",np.sum(arr_s))
print("Max : ",np.max(arr_s))

print("Al_Ahly Receives:")
arr_r = np.array(al_ahly_r, dtype=np.int64)
print("Average : ",np.average(arr_r))
print("Sum : ",np.sum(arr_r))
print("Max : ",np.max(arr_r))

