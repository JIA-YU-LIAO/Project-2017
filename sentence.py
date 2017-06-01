#encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup
import re
HTML_PARSER = "html.parser"
def get_sentence():
  url = "http://www.appledaily.com.tw/index/dailyquote/"
  data = urllib.request.urlopen(url).read()
  data = data.decode('UTF-8')
  soup = BeautifulSoup(data, HTML_PARSER)
  article_tags = soup.find_all("article",{"class":"dphs"})
  #list
  article_str = []
  for x in article_tags[0]:
    article_str.append(str(x))
  #list to string     
  article = ''.join(article_str)
  sentence = article.split('</p>')
  sentence_result = sentence[0][4:]
  author = sentence[1].split('<time datetime="')
  author_result = author[0][5:]
  return("\n{0}\n\n                              {1}\n".format(sentence_result,author_result))
if __name__ == "__main__":
    get_sentence()  

  