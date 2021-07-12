from urllib.request import urlopen, Request
import urllib
import bs4

location = input("입력:")
while(True): 
    enc_location = urllib.parse.quote(location + '+미세먼지')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    print('현재 ' + location + ' 미세먼지는 ' +
          soup.find('div', class_='state_info _fine_dust')
          .find('span', class_='num _value').text + '입니다.')


    print('현재 ' + location + ' 초미세먼지는 ' +
          soup.find('div', class_='state_info _ultrafine_dust')
          .find('span', class_='num _value').text + '입니다.')
