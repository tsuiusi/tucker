from bs4 import BeautifulSoup
import urllib3

def find_wotd(url):
    http = urllib3.PoolManager()

    page = http.request(method="GET", url=url)

    soup = BeautifulSoup(page.data, "html.parser")
    
    if url == "https://www.merriam-webster.com/":
        wotd = soup.find('div', attrs={"class":"d-inline-block"}).text.strip()
    elif url == "https://www.nytimes.com/column/learning-word-of-the-day":
        wotd = soup.find("h3", attrs={"class":"css-1kv6qi e15t083i0"}).text.strip().replace("Word of the Day: ", "")
        # byclass = soup.find_all("h3", attrs={"class": "css-1kv6qi e15t083i0"})
    
    # for i in range(len(byclass)):
    #    byclass[i] = byclass[i].text.strip().replace("Word of the Day: " ,"")
        
    return wotd

def find_all(links):
    words = []
    for i in links:
        try:
            words.append(find_wotd(i))
        except:
            print(f"Error with {i}, next")

    return words


