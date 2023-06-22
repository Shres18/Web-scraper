import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
res2 = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup.select('.titleline')
subtext2 = soup.select('.subtext')

mega_links= links+links2
mega_subtext= subtext +subtext2
# print(votes[0])
# print(votes[0].get('id'))
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = links[idx].get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points >99:
              hn.append({'title': title, 'votes': points}) # dictionary has to be converted
    return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
