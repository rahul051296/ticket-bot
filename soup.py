from bs4 import BeautifulSoup

import requests


def searchBingMeaning(query):
    r = requests.get("https://www.bing.com/search?q=meaning+of+{}".format(query))
    data = r.text
    soup = BeautifulSoup(data)
    print(soup.find('div', {'class': "dc_mn"}).text)


def searchBingWeather(location):
    r = requests.get("https://www.bing.com/search?q=weather+in+{}".format(location))
    data = r.text
    soup = BeautifulSoup(data)
    print(soup.find('div', { 'class': "wtr_currTemp b_focusTextLarge"}).text)


def translateBing(word, language):
    r = requests.get("https://www.bing.com/search?q=translate+{}+in+{}".format(word,language))
    data = r.text
    soup = BeautifulSoup(data)
    print(soup.find('textarea', {'id': "tta_tv"}).text)


if __name__ == '__main__':
    translateBing("wheel", "tamil")