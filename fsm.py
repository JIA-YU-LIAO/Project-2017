from transitions.extensions import GraphMachine
from weather_city import get_current_weather
from uvi_tem import get_uvi_stem
from zodiac import get_zodiac
from sentence import get_sentence

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )  
                
    def is_going_to_state1(self, update):
        global city_temp
        if update.message != None:
            text = update.message.text
            city = text[0:3]
            func = text[3:]
            res = '很抱歉,無法提供您該城市的天氣'
            function2 = '天氣'
            if get_current_weather(city) == res:
                return False
            elif func != function2:
                return False
            else:
                city_temp = city
                return True
        else:
            return False            

    def is_going_to_state2(self, update):
        if update.message != None:
            text = update.message.text
            if text.lower() == '詳細資料':
                return True
            else:
                if text.lower() =='不用':
                    update.message.reply_text('很高興能為你服務,掰掰囉～')
                    self.go_back(update)
                else:    
                    update.message.reply_text('請輸入"詳細資料"來取得後續服務,若不想取得後續服務請輸入"不用"')
                    return False    
        else:
            return False    

    def is_going_to_state3(self, update):
        if update.message != None:
            text = update.message.text
            if text.lower() == '星座運勢':
                return True
        else:
            return False            

    def is_going_to_state4(self, update):
        global zodiac
        zodiac = ''
        if update.message != None:
            text = update.message.text
            if text == '牡羊座':
                zodiac = 'Aries'
            elif text == '金牛座':
                zodiac = 'Taurus'
            elif text == '雙子座':
                zodiac = 'Gemini'
            elif text == '巨蟹座':
                zodiac = 'Cancer'
            elif text == '獅子座':
                zodiac = 'Leo'
            elif text == '處女座':
                zodiac = 'Virgo'
            elif text == '天秤座':
                zodiac = 'Libra'
            elif text == '天蠍座':
                zodiac = 'Scorpio'
            elif text == '射手座':
                zodiac = 'Sagittarius'
            elif text == '魔羯座':
                zodiac = 'Capricorn'
            elif text == '水瓶座':
                zodiac = 'Aquarius'
            elif text == '雙魚座':
                zodiac = 'Pisces'
            if zodiac == '':
                update.message.reply_text('請確定您的輸入正確的星座')
                return False
            else:
                return True                                                    
        else:
            return False
    def is_going_to_state5(self, update):
        if update.message != None:
            text = update.message.text
            if text.lower() == '每日一句':
                return True
            else:
                update.message.reply_text('輸入格式錯誤,請確定格式後重新輸入')
                return False    
        else:
            return False    

    def on_enter_state1(self, update):
        update.message.reply_text(get_current_weather(city_temp))

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        city_english = ''
        if city_temp == '臺北市':
            city_english = 'Taipei_City'
        elif city_temp == '新北市':
            city_english = 'New_Taipei_City'
        elif city_temp == '桃園市':
            city_english = 'Taoyuan_City'
        elif city_temp == '新竹市':
            city_english = 'Hsinchu_City'
        elif city_temp == '新竹縣':
            city_english = 'Hsinchu_County'
        elif city_temp == '苗栗縣':
            city_english = 'Miaoli_County'
        elif city_temp == '臺中市':
            city_english = 'Taichung_City'
        elif city_temp == '彰化縣':
            city_english = 'Changhua_County'
        elif city_temp == '雲林縣':
            city_english = 'Yunlin_County'
        elif city_temp == '嘉義縣':
            city_english = 'Chiayi_County'
        elif city_temp == '嘉義市':
            city_english = 'Chiayi_City' 
        elif city_temp == '臺南市':
            city_english = 'Tainan_City'
        elif city_temp == '高雄市':
            city_english = 'Kaohsiung_City'
        elif city_temp == '屏東縣':
            city_english = 'Pingtung_County'
        elif city_temp == '南投縣':
            city_english = 'Nantou_County'
        elif city_temp == '基隆市':
            city_english = 'Keelung_City'
        elif city_temp == '宜蘭縣':
            city_english = 'Yilan_County'
        elif city_temp == '花蓮縣':
            city_english = 'Hualien_County'
        elif city_temp == '台東縣':
            city_english = 'Taitung_County'
        elif city_temp == '連江縣':
            city_english = 'Lienchiang_County'
        elif city_temp == '金門縣':
            city_english = 'Kinmen_County'
        elif city_temp == '澎湖縣':
            city_english = 'Penghu_County'
        update.message.reply_text(get_uvi_stem(city_english))
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text('請輸入您的星座')

    def on_exit_state3(self, update):
        print('Leaving state3')
    def on_enter_state4(self, update):
        update.message.reply_text(get_zodiac(zodiac))
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text(get_sentence())
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')        
            

