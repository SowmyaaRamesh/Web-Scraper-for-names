from bs4 import BeautifulSoup 
import requests 
import re

girl_names=[]
boy_names=[] 


def get_html_text(url):
    html_text = requests.get(url).text
    return html_text

def has_special_char(str):
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(special_char.search(string) == None):
        return 0
    else:
        return 1

def scrape_girl_names():
    # Site 1: Greek Goddesses
    html_text = get_html_text("https://nameberry.com/list/624/gorgeous-greek-goddess-names-for-babies")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.find_all('span', class_='jsx-1193454341 mr-10')
    for name in names:
        girl_names.append(name.text)

    #Site 2: Anime Girls 
    html_text = get_html_text("https://kidadl.com/articles/top-anime-girl-names-with-meanings")
    soup = BeautifulSoup(html_text, 'lxml')
    names = soup.select('p strong')
    try:
        for name in names:
            parsed_name = name.text.split('.')[1].replace(' ','')
            if(has_special_char(parsed_name) == 1):
                print(parsed_name)
            # girl_names.append()
    except:
        print("Ignoring unexpected string")



scrape_girl_names()
# print(girl_names)
