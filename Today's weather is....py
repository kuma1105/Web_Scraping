import urllib.request
from bs4 import BeautifulSoup

url = "https://weather.naver.com/today/09680740"
result = urllib.request.urlopen(url)
soup = BeautifulSoup(result, 'html.parser')

#지역이름
location_name = soup.select("strong.location_name")
location_nameList = []
for r in location_name :
    location_nameList.append(r)

print("우리 동네 :",location_nameList[0].text,'\n') #지역이름

#<오늘의 날씨>
menu = soup.select("li a.menu")
menuList = []
for r in menu :
    menuList.append(r)

weather = soup.select("span.weather")
weatherList = []
for r in weather :
    weatherList.append(r)

print("<오늘의", menuList[0].text + ">") #<오늘의 날씨>
print(weatherList[0].text)

#종합날씨정보
weather2 = soup.select("p.summary")
weatherList2 = []
for r in weather2 :
    weatherList2.append(r)

if (weatherList[0].text in weatherList2[0].text) :
        weatherSummary =  weatherList2[0].text.rstrip(weatherList[0].text)

print(weatherSummary) #종합날씨정보

#현재온도
temperature = soup.select("strong.current")
temperatureList = []
for r in temperature :
    temperatureList.append(r)

print(temperatureList[0].text, '\n') #현재온도

#강수확률, 습도, 바람
term = soup.select("dt.term")
termList = []
for r in term :
    termList.append(r)

term_ = soup.select("dd.desc")
term_List = []
for r in term_ :
    term_List.append(r)

print(termList[0].text + ":" + term_List[0].text)         #강수확률
print(termList[1].text + ":" + term_List[1].text)         #습도
print(termList[2].text + ":" + term_List[2].text, '\n')   #바람

#<오늘의 미세먼지>, 미세먼지, 초미세먼지, 자외선
ttl = soup.select("strong.ttl")
ttlList = []
for r in ttl :
    ttlList.append(r)

level_text = soup.select("em.level_text")
level_textList = []
for r in level_text :
    level_textList.append(r)

print("<오늘의", menuList[1].text + ">")                      #<오늘의 미세먼지>
print(ttlList[0].text + ":" + level_textList[0].text)         #미세먼지
print(ttlList[1].text + ":" + level_textList[1].text)         #초미세먼지
print(ttlList[2].text + ":" + level_textList[2].text, '\n\n') #자외선

#프로그램 끝
input("Press enter to exit ;)")
