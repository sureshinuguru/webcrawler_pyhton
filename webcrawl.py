import requests
from bs4 import BeautifulSoup

urls = {}
root= "http://wiprodigital.com"
def get_urls(url):
    print "URL: %s" % url
    urls[url] = {}
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text,"html.parser")
        soup.prettify()
        child_urls = [ a['href'] for a in  soup.find_all('a', href=True) if  a['href'].startswith(root)]
        images = [tag['src'] for tag in soup.findAll('img')]
        print "\t URLS=> %r" % child_urls
        print "\t IMAGES=> %r" % images
        urls[url]['imgs'] = images
        if child_urls:
            urls[url]['hrefs'] = child_urls
            [ get_urls(curl) for curl in child_urls if not urls.has_key(curl)]

get_urls(root)
print urls
