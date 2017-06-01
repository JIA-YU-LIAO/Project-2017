#encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup
import re
HTML_PARSER = "html.parser"
def get_uvi_stem(city):
  url = "http://www.cwb.gov.tw/V7/forecast/taiwan/inc/UVI/"+city+".htm"
  data = urllib.request.urlopen(url).read()
  data = data.decode('UTF-8')
  soup = BeautifulSoup(data, HTML_PARSER)
  td_tags = soup.find_all(lambda tag:tag.name == "td")
  #list
  tems = []
  uvis = []
  for x in td_tags[0]:
    tems.append(str(x))
  for x in td_tags[7]:
    uvis.append(str(x))
  #list to string     
  tem_val = ''.join(tems)
  uvi_str = ''.join(uvis)
  uvi_val = re.search(r'UVI/[0-9]+.gif',uvi_str)
  uvi_result = uvi_val.group(0)[4:len(uvi_val.group(0))-4]
  warning = ''
  if int(uvi_result)>=0 and int(uvi_result)<=2:
    level = '低量級'
  elif  int(uvi_result)>=3 and int(uvi_result)<=5:
    level = '中量級'
  elif  int(uvi_result)>=6 and int(uvi_result)<=7:
    level = '高量級'
    warning = '晒傷時間:30分鐘內\n防曬措施:帽子/陽傘+防曬液+太陽眼鏡+儘量待在陰涼處'
  elif  int(uvi_result)>=8 and int(uvi_result)<=10:
    level = '過量級'
    warning = '晒傷時間:20分鐘內\n防曬措施:帽子/陽傘+防曬液+太陽眼鏡+陰涼處+長袖衣物+10至14時最好不在烈日下活動'
  elif  int(uvi_result)>=11:
    level = '危險級'
    warning = '晒傷時間:15分鐘內\n防曬措施:帽子/陽傘+防曬液+太陽眼鏡+陰涼處+長袖衣物+10至14時最好不在烈日下活動'    
  return("體感溫度為 {0} ℃\n紫外線指數為 {1}\n曝曬級數為 {2}\n{3}".format(tem_val,uvi_result,level,warning))      
  

if __name__ == "__main__":
    get_uvi_stem('Tainan_City')
  