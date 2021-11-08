from bs4 import BeautifulSoup 
import requests
from jsonfuncs import add_name

girl_names=[]
boy_names=[] 
invalid = []

def get_html_text(url):
    return requests.get(url).text

def check_and_append(string):
    special_char = list('[@_!-#$.%^&*()<>?/\|}{~:]0123456789')
    for i in special_char:
        if (string.find(i)>=0):
            invalid.append(string)
            return 0
    if len(string)<3:
        return 0
    try:
        string.encode('ascii')
    except:
        invalid.append(string)
        return 0
    # girl_names.append(string)
    # boy_names.append(string)
    return 1



def scrape_girl_names():
    #Greek Goddesses
    html_text = get_html_text("https://nameberry.com/list/624/gorgeous-greek-goddess-names-for-babies")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('span', class_='jsx-1193454341 mr-10')
    for name in names:
        parsed_name = name.text
        if check_and_append(parsed_name):
            add_name("girls.json", parsed_name, {'origin':'greek', 'genre':'goddess'})

    #Anime Girls 
    html_text = get_html_text("https://kidadl.com/articles/top-anime-girl-names-with-meanings")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.select('p strong')
    for name in names:
        parsed_name = name.text.split(' ')[1]
        if check_and_append(parsed_name):
            add_name("girls.json", parsed_name, {'genre':'anime', 'origin':'japanese'})

    html_text = get_html_text("https://skdesu.com/en/women-of-anime-female-characters/")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.select('ol li')
    for name in names:
        parsed_name = name.text.split('[')[0].strip().split(' ')[0]
        if check_and_append(parsed_name):
            add_name("girls.json", parsed_name, {'genre':'anime', 'origin':'japanese'})
    
    #Genshin Cuties
    html_text = get_html_text("https://genshin-impact.fandom.com/wiki/Category:Female_Characters")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a', class_="category-page__member-link")
    for name in names:
        try:
            parsed_name = name.text.split(" ")[1]
        except:
            parsed_name = name.text
        if check_and_append(parsed_name):
            add_name("girls.json", parsed_name, {'genre':'video game', 'source': 'genshin impact'})
    
    html_text = get_html_text("https://genshin-impact.fandom.com/wiki/Category:Female_Characters?from=Sara")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a', class_="category-page__member-link")
    for name in names:
        try:
            parsed_name = name.text.split(" ")[1]
        except:
            parsed_name = name.text
        if check_and_append(parsed_name):
            add_name("girls.json", parsed_name, {'genre':'video game', 'source': 'genshin impact'})
    
       

    #Video Game characters
    html_text = get_html_text("https://en.wikipedia.org/wiki/Category:Female_characters_in_video_games")
    soup = BeautifulSoup(html_text,'lxml')
    names = soup.find_all('div', class_='mw-category-group')
    for nameline in names:
        parsed_names = nameline.text.split('\n')
        for name in parsed_names:
            parsed_name = name.split(" ")[0]
            if check_and_append(parsed_name):
                add_name("girls.json", parsed_name, {'genre':'video game'})        

    #Disney characters
    html_text = get_html_text("https://kidadl.com/articles/disney-female-character-names-to-be-inspired-by")
    soup = BeautifulSoup(html_text, 'lxml')
    body = soup.find('div', class_='rich-text-article-body w-richtext')
    names = body.find_all('strong')
    for name in names:
        parsed_name = name.text.split(".")[1]
        parsed_name = parsed_name.strip(" ")
        if check_and_append(parsed_name):
            add_name("girls.json", parsed_name, {'genre':'disney'})


def scrape_boy_names():

    #Genshin Characters
    html_text = get_html_text("https://genshin-impact.fandom.com/wiki/Category:Male_Characters")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a', class_='category-page__member-link')
    for name in names:
        try:
            parsed_name = name.text.split(" ")[1]
        except:
            parsed_name = name.text
    
        if check_and_append(parsed_name):
            add_name("boys.json", parsed_name, {'genre':'video game', 'source': 'genshin impact'})
    
    
    html_text = get_html_text("https://genshin-impact.fandom.com/wiki/Category:Male_Characters?from=Jinglun")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a', class_='category-page__member-link')
    for name in names:
        try:
            parsed_name = name.text.split(" ")[1]
        except:
            parsed_name = name.text
    
        if check_and_append(parsed_name):
            add_name("boys.json", parsed_name, {'genre':'video game', 'source': 'genshin impact'})


    html_text = get_html_text("https://genshin-impact.fandom.com/wiki/Category:Male_Characters?from=Royce")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a', class_='category-page__member-link')
    for name in names:
        try:
            parsed_name = name.text.split(" ")[1]
        except:
            parsed_name = name.text
    
        if check_and_append(parsed_name):
            add_name("boys.json", parsed_name, {'genre':'video game', 'source': 'genshin impact'})

    # Greek gods      
    html_text = get_html_text("https://momlovesbest.com/greek-mythology-baby-names")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('h3',class_="heading-list main")
    for name in names:
        parsed_name = name.text.split(' ')[1]
        add_name("boys.json", parsed_name, {'origin':'greek', 'genre':'god'})
       
    # Video game characters 
    html_text = get_html_text("https://en.wikipedia.org/wiki/Category:Male_characters_in_video_games")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('div',class_="mw-category-group")
    for nameline in names:
        parsed_names = nameline.text.split('\n')
        for name in parsed_names:
            parsed_name = name.split(" ")[0]
            if check_and_append(parsed_name):
                add_name("boys.json", parsed_name, {'origin':'video game'})

    #Anime characters 
    html_text = get_html_text("https://en.wikipedia.org/wiki/Category:Male_characters_in_anime_and_manga")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('div',class_="mw-category-group")
    for nameline in names:
        parsed_names = nameline.text.split('\n')
        for name in parsed_names:
            parsed_name = name.split(' ')[0]
            if(check_and_append(parsed_name)):
                add_name("boys.json", parsed_name, {'genre':'anime'})

    html_text = get_html_text("https://www.ranker.com/list/hot-anime-guys-and-boys/ranker-anime")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a',class_="gridItem_name__wCyGi gridItem_nameLink__2hPOH")
    for name in names:
        parsed_name = name.text.split(' ')[0]
        if check_and_append(parsed_name):
            add_name("boys.json",parsed_name,{'genre':'anime'})

    html_text = get_html_text("https://thebiem.com/top-100-hot-anime-guys/")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('h2')
    for name in names:
        try:
            parsed_name = name.text.split(' ')[1]
        except: 
            parsed_name = name.text
        if(check_and_append(parsed_name)):
            add_name("boys.json",parsed_name,{'genre':'anime'})
           

    
    

      
scrape_girl_names()
scrape_boy_names()
# print(boy_names)
# print(len(girl_names))
# print(girl_names)
# print(invalid)