from bs4 import BeautifulSoup 
import requests

girl_names=[]
boy_names=[] 
invalid = []

def get_html_text(url):
    html_text = requests.get(url).text
    return html_text

def has_special_char(string):
    special_char = list('[@_!#$%^&*()<>?/\|}{~:]0123456789')
    for i in special_char:
        if (string.find(i)>=0):
            print("invalid found: "+string)
            return 1
    try:
        string.encode('ascii')
    except:
        print("invalid found: "+string)
        return 1
    return 0

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
    for name in names:
        parsed_name = name.text.split(' ')[1]
        if has_special_char(parsed_name):
            invalid.append(parsed_name)
        else:
            girl_names.append(parsed_name)

scrape_girl_names()
print(girl_names)
print(invalid)
