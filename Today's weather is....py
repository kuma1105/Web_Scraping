import urllib.request
from bs4 import BeautifulSoup

url_1 = "http://ncov.mohw.go.kr/"                    # 대한민국 코로나 확진자 현황
result_1 = urllib.request.urlopen(url_1)
soup_1 = BeautifulSoup(result_1, 'html.parser')

url_2 = "https://weather.naver.com/today/(지역번호)"   #번호는 수정하여 사용   
result_2 = urllib.request.urlopen(url_2)
soup_2 = BeautifulSoup(result_2, 'html.parser')

######################################################################################################

Confirmed_person = soup_1.select("span.data")
Confirmed_personList = []
for r in Confirmed_person :
    Confirmed_personList.append(r)

print("<일일확진자 현황>")
print("COVID-19 국내발생 확진자 수 :", Confirmed_personList[0].text)
print("COVID-19 해외발생 확진자 수 :", Confirmed_personList[1].text,'\n')

social_distancing = soup_1.select("span.name")
social_distancingLevel = soup_1.select("button span.num")
social_distancingList = []
social_distancingLevelList = []
for r in social_distancing :
    social_distancingList.append(r)
for r in social_distancingLevel :
    social_distancingLevelList.append(r)
print("<거리 두기 단계>")
print(social_distancingList[0].text + ":" + social_distancingLevelList[0].text + '단계', '\n')

######################################################################################################

#지역이름
location_name = soup_2.select("strong.location_name")
location_nameList = []
for r in location_name :
    location_nameList.append(r)

#<오늘의 날씨>
menu = soup_2.select("li a.menu")
menuList = []
for r in menu :
    menuList.append(r)

weather = soup_2.select("span.weather")
weatherList = []
for r in weather :
    weatherList.append(r)

print("<오늘의", menuList[0].text + ">") #<오늘의 날씨>
print("우리 동네 :",location_nameList[0].text) #지역이름
print(weatherList[0].text)

#현재온도
temperature = soup_2.select("strong.current")
temperatureList = []
for r in temperature :
    temperatureList.append(r)

print(temperatureList[0].text) #현재온도

#강수확률, 습도, 바람
term = soup_2.select("dt.term")    # 제목
termList = []
for r in term :
    termList.append(r)

term_ = soup_2.select("dd.desc")   # 숫자
term_List = []
for r in term_ :
    term_List.append(r)

print(termList[0].text + ":" + term_List[0].text)         # 습도
print(termList[1].text + ":" + term_List[1].text)         # 풍향 : 풍속
print(termList[2].text + ":" + term_List[2].text, '\n')   # 체감온도

#<오늘의 미세먼지>, 미세먼지, 초미세먼지, 자외선
ttl = soup_2.select("strong.ttl")
ttlList = []
for r in ttl :
    ttlList.append(r)

level_text = soup_2.select("em.level_text")
level_textList = []
for r in level_text :
    level_textList.append(r)

print("<오늘의", menuList[1].text + ">")                      #<오늘의 미세먼지>
print(ttlList[0].text + ":" + level_textList[0].text)         #미세먼지
print(ttlList[1].text + ":" + level_textList[1].text)         #초미세먼지
print(ttlList[2].text + ":" + level_textList[2].text, '\n\n') #자외선

#프로그램 일시정지 시키기
input("Press enter to exit ;)")



######################################################################################################
#종합날씨정보
# weather2 = soup.select("p.summary")
# weatherList2 = []
# for r in weather2 :
#     weatherList2.append(r)
# if (weatherList[0].text in weatherList2[0].text) :
#         weatherSummary =  weatherList2[0].text.rstrip(weatherList[0].text)
# print(weatherSummary) #종합날씨정보
