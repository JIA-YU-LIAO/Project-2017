import xml.etree.ElementTree as ET
import urllib.request

def get_current_weather(city):
    #讀xml
    response = urllib.request.urlopen('http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-FD776FF2-695B-4736-9380-96C24F1CF1B1')
    tree = ET.parse(response)
    root = tree.getroot()
    found = 0

    for location in root.findall('.//{urn:cwb:gov:tw:cwbcommon:0.1}location'):
        if city in location[0].text:
            found = 1
            return ('%s目前的天氣狀況為%s。\n' \
                   '溫度為 %s ~ %s ℃，降雨機率為 %s %%' \
                   % (location[0].text, location[1][1][2][0].text,
                      location[3][1][2][0].text, location[2][1][2][0].text,
                      location[5][1][2][0].text))

    if found == 0:
      return('很抱歉，無法提供您該城市的天氣')
if __name__ == "__main__":
    get_current_weather('臺南市')
