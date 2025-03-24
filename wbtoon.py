import requests
from bs4 import BeautifulSoup

def get_webtoon_top10_really_simple():
    # 1. 페이지 불러오기
    url = "https://comic.naver.com/index"
    response = requests.get(url)
    response.raise_for_status()

    # 2. HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. 페이지 안의 모든 <li> 태그 찾기
    li_tags = soup.find_all("li")

    # 4. 상위 10개 <li> 태그 텍스트 출력
    for i, li in enumerate(li_tags[:10], start=1):
        # get_text(strip=True)로 공백 제거
        print(f"{i}위: {li.get_text(strip=True)}")

if __name__ == "__main__":
    get_webtoon_top10_really_simple()