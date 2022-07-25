""""
open Codeforces website and see the following:
the first problem in the site: 
its name is [Three Minimums] 
and the algorithms that is used to solve this problem is: [combinatorics, fft, math]
the problem:
Use Requests package to scrap codeforces site to find 
the most used algorithm in the first 2 pages.
print the algorithm name and how many times this algorithm appeared in the 2 pages

codeforces url: "https://codeforces.com/problemset"
example:
the third page in Codeforces site is: https://codeforces.com/problemset/page/3
and the algorithms used in this page is:
{'2-sat': 1,
 'binary search': 8,
 'bitmasks': 6,
 'brute force': 23,
 'combinatorics': 8,
 'constructive algorithms': 23,
 'data structures': 30,
 'dfs and similar': 14,
 'divide and conquer': 4,
 'dp': 14,
 'dsu': 5,
 'fft': 3,
 'geometry': 3,
 'graph matchings': 2,
 'graphs': 23,
 'greedy': 36,
 'hashing': 4,
 'implementation': 28,
 'interactive': 13,
 'math': 31,
 'matrices': 2,
 'number theory': 5,
 'shortest paths': 6,
 'sortings': 14,
 'strings': 5,
 'trees': 9,
 'two pointers': 3}
 so the most used algorithm is 'greedy' appeared 36 times in the third page
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
cf_url = "https://codeforces.com/problemset/page/"
fromPage = 1
toPage = 2
data = {}
for page in range(fromPage,toPage+1):
    cf_response = urlopen(cf_url+str(page))
    cf_page = bs(cf_response.read(), 'html.parser')
    problems = cf_page.find('table', class_="problems")
    style = "float: right; font-size: 1.1rem; padding-top: 1px; text-align: right;"
    names = problems.findAll('div', style=style)
    for name in names:
        val = name.find('a').text.strip();
        if(val in data.keys()):
            data[val] += 1
        else: 
            data.update({val: 1})

for(key,value)in data.items():
    print("{} : {}".format(key,value))