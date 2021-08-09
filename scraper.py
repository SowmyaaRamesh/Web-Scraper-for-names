from bs4 import BeautifulSoup 
import requests

girl_names=[]
boy_names=[] 
invalid = []

def get_html_text(url):
    html_text = requests.get(url).text
    return html_text

def check_and_append(string):
    special_char = list('[@_!#$%^&*()<>?/\|}{~:]0123456789')
    for i in special_char:
        if (string.find(i)>=0):
            print("invalid found: "+string)
            invalid.append(string)
            return 1
    try:
        string.encode('ascii')
    except:
        print("invalid found: "+string)
        invalid.append(string)
        return 1
    girl_names.append(string)
    return 0

def scrape_girl_names():
    # Site 1: Greek Goddesses
    html_text = get_html_text("https://nameberry.com/list/624/gorgeous-greek-goddess-names-for-babies")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('span', class_='jsx-1193454341 mr-10')
    for name in names:
        parsed_name = name.text
        check_and_append(parsed_name)

    #Site 2: Anime Girls 
    html_text = get_html_text("https://kidadl.com/articles/top-anime-girl-names-with-meanings")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.select('p strong')
    for name in names:
        parsed_name = name.text.split(' ')[1]
        check_and_append(parsed_name)
    
    #Site 3: Genshin Cuties
    html_text = get_html_text("https://genshin-impact.fandom.com/wiki/Category:Female_Characters")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('a', class_="category-page__member-link")
    for name in names:
        parsed_name = name.text
        check_and_append(parsed_name)

    #Site 4: Video Game characters
    html_text = get_html_text("https://en.wikipedia.org/wiki/Category:Female_characters_in_video_games")
    soup = BeautifulSoup(html_text,'lxml')
    names = soup.find_all('div', class_='mw-category-group')
    for name in names:
        parsed_name = name.text
        check_and_append(parsed_name)


scrape_girl_names()
print(girl_names)
print(len(girl_names))
print(invalid)
