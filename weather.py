import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from collections import defaultdict

def fetch_and_classify_weather(nx=60, ny=127):
    """
    - nx, ny: 기상청 그리드 좌표 (기본값은 서울)
    - 반환: {day_offset: "맑음" or "비옴"}
    """
    # 1) RSS 조회
    url = "https://www.kma.go.kr/wid/queryDFS.jsp"
    resp = requests.get(url, params={"gridx": nx, "gridy": ny})
    resp.encoding = 'utf-8'
    resp.raise_for_status()

    # 2) 파싱
    soup = BeautifulSoup(resp.text, 'html.parser')
    data_nodes = soup.find_all('data')

    # 3) 일별 강수확률 최대값 수집
    pops_by_day = defaultdict(int)
    for node in data_nodes:
        day_off = int(node.find('day').text)  # 0: 오늘, 1: 내일, ...
        pop = int(node.find('pop').text)      # 강수확률
        # 7일치만
        if 0 <= day_off < 7:
            pops_by_day[day_off] = max(pops_by_day[day_off], pop)

    # 4) 분류
    result = {}
    for d in range(7):
        result[d] = "비옴" if pops_by_day.get(d, 0) >= 60 else "맑음"

    return result

def print_weekly_forecast(nx=60, ny=127):
    today = datetime.now().date()
    weather = fetch_and_classify_weather(nx, ny)

    print("🗓 오늘부터 7일간 날씨 (맑음/비옴)")
    print("-" * 30)
    for offset, status in weather.items():
        date = today + timedelta(days=offset)
        print(f"{date} ({offset}일차): {status}")
    print("-" * 30)

if __name__ == "__main__":
    # 서울(60,127) 기준. 다른 지역은 좌표만 바꿔주세요.
    print_weekly_forecast()