#encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup
import re
HTML_PARSER = "html.parser"
def get_zodiac(zodiac):
  url = "http://daily-zodiac.herokuapp.com/mobile/zodiac/"+zodiac
  data = urllib.request.urlopen(url).read()
  data = data.decode('UTF-8')
  soup = BeautifulSoup(data, HTML_PARSER)
  article_tags = soup.find_all(lambda tag:tag.name == "article")
  #list
  article_str = []
  for x in article_tags[0]:
    article_str.append(str(x))
  #list to string     
  advice = ''.join(article_str)
  return("今日運勢:{0}\n".format(advice))
if __name__ == "__main__":
    get_zodiac('Capricorn')  

  