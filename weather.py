import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 예시 지역: 서울특별시 (좌표에 따라 변경 가능)
def get_weather_rss(nx=60, ny=127):
    base_url = "https://www.kma.go.kr/wid/queryDFS.jsp"
    params = {
        "gridx": nx,  # 서울 기준 x
        "gridy": ny   # 서울 기준 y
    }

    response = requests.get(base_url, params=params)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print("날씨 정보를 가져오는데 실패했습니다.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('data')

    print("📅 7일간의 날씨 예보")
    print("지역 좌표 (x={}, y={})".format(nx, ny))
    print("="*40)

    for item in data:
        hour = item.find("hour").text
        day = int(item.find("day").text)
        temp = item.find("temp").text
        sky = item.find("wfKor").text
        pty = item.find("pty").text
        pop = item.find("pop").text

        forecast_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        forecast_time = forecast_time.replace(day=forecast_time.day + day)

        print(f"🕓 시간: {hour}시 / 날짜: {forecast_time.strftime('%Y-%m-%d')}")
        print(f"🌡 기온: {temp}℃ / 🌤 상태: {sky} / ☔ 강수확률: {pop}%")
        print("-"*40)

# 실행
get_weather_rss()