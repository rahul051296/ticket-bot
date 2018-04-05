from bs4 import BeautifulSoup

import requests


def searchWeatherDetails(location):
    s = requests.Session()
    s.headers[
        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r = s.get(
        "https://www.google.co.in/search?q=weather+in+{}&oq=weather+inche&aqs=chrome.1.69i57j0l5.5039j0j7&sourceid=chrome&ie=UTF-8".format(
            location))
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    celcius = soup.find('span', attrs={'class': 'wob_t'}).text
    result = "Weather in {} is {}° Celcius".format(location.capitalize(), celcius)
    return result


def searchWordMeaning(query):
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r = s.get("https://www.google.co.in/search?ie=UTF-8&q=meaning+of+{}".format(query))
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    var = soup.find('div', attrs={'class': 'PNlCoe'}).text.split('.')[0]
    result = "{} means {}".format(query, var)
    return result


def translateGoogle(word, language):
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    r = s.get('https://www.google.co.in/search?q=translate+{}+in+{}&ie=UTF-8'.format(word, language))
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    translated = soup.find('pre', attrs={'id': 'tw-target-text'}).text
    return translated


if __name__ == '__main__':
    print(searchWordMeaning("life"))
