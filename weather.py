from bs4 import BeautifulSoup #웹사이트 정보를 크롤링 해오기위해 Beautiful Soup4 라이브러리를 사용해야함
#bs4 라는 명칭으로 사용되는 라이브러리는 웹사이트의 html이나 css같은 정보를 모두 끌어모아주는 역할
import urllib.request
import datetime
import json

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

print("\n Weather Webcrawling Project \n")
print(' 환영합니다,' + nowDate)
print('오늘의 6개 광역시 주요 정보를 요약해 드리겠습니다.\n')

def naver():
    # requests를 이용해서 웹페이지의 전체 소스코드를 갖고옴
    #인천날씨
    url1 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B8%EC%B2%9C%EB%82%A0%EC%94%A8') #웹페이지 요청 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
    soup = BeautifulSoup(url1, "html.parser")
    Incheontemp = soup.find('div',attrs= {'class':'temperature_text'}).get_text().replace('현재 온도','')#온도 표시
    Incheoncast = soup.find('p',attrs= {'class':'summary'}).get_text()#어제보다 ~높아요 ~맑음 흐림표시
    print('--> 인천 날씨 :',Incheontemp , Incheoncast)

    #부산날씨
    url2 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8') #웹페이지 요청 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
    soup = BeautifulSoup(url2, "html.parser")
    Busantemp = soup.find('div',attrs= {'class':'temperature_text'}).get_text().replace('현재 온도','') #온도 표시
    Busancast = soup.find('p',attrs= {'class':'summary'}).get_text()#어제보다 ~높아요 ~맑음 흐림표시
    print('--> 부산 날씨 :',Busantemp, Busancast)
    
    #광주날씨
    url3 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B4%91%EC%A3%BC%EB%82%A0%EC%94%A8') #웹페이지 요청 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
    soup = BeautifulSoup(url3, "html.parser")
    Gwangjutemp = soup.find('div',attrs= {'class':'temperature_text'}).get_text().replace('현재 온도','') #온도 표시
    Gwangjucast = soup.find('p',attrs= {'class':'summary'}).get_text()#어제보다 ~높아요 ~맑음 흐림표시
    print('--> 광주 날씨 :',Gwangjutemp, Gwangjucast)

    #대전날씨
    url4 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=4&acq=%EB%8C%80%EC%A0%84%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%8C%80%EC%A0%84%EB%82%A0%EC%94%A8') #웹페이지 요청 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
    soup = BeautifulSoup(url4, "html.parser")
    Daejeontemp = soup.find('div',attrs= {'class':'temperature_text'}).get_text().replace('현재 온도','') #온도 표시
    Daejeoncast = soup.find('p',attrs= {'class':'summary'}).get_text()#어제보다 ~높아요 ~맑음 흐림표시
    print('--> 대전 날씨 :',Daejeontemp, Daejeoncast)

    #대구날씨
    url5 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8') #웹페이지 요청 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
    soup = BeautifulSoup(url5, "html.parser")
    Daegutemp = soup.find('div',attrs= {'class':'temperature_text'}).get_text().replace('현재 온도','') #온도 표시
    Daegucast = soup.find('p',attrs= {'class':'summary'}).get_text()#어제보다 ~높아요 ~맑음 흐림표시
    print('--> 대구 날씨 :',Daegutemp, Daegucast)

    #울산날씨
    url6 = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9A%B8%EC%82%B0%EB%82%A0%EC%94%A8') #웹페이지 요청 특정 url을 적으면 웹페이지에 대한 소스코드를 볼 수 있음
    soup = BeautifulSoup(url6, "html.parser")
    Ulsantemp = soup.find('div',attrs= {'class':'temperature_text'}).get_text().replace('현재 온도','') #온도 표시
    Ulsancast = soup.find('p',attrs= {'class':'summary'}).get_text()#어제보다 ~높아요 ~맑음 흐림표시
    print('--> 울산 날씨 :',Ulsantemp, Ulsancast)


    weather = []
    try:
        weather.append(Incheontemp)
        weather.append(Incheoncast)
        weather.append(Busantemp)
        weather.append(Busancast)
        weather.append(Gwangjutemp)
        weather.append(Gwangjucast)
        weather.append(Daejeontemp)
        weather.append(Daejeoncast)
        weather.append(Daegutemp)
        weather.append(Daegucast)
        weather.append(Ulsantemp)
        weather.append(Ulsancast)
        
    except IndexError:
        pass
    return weather