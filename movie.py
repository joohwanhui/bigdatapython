import requests
from bs4 import BeautifulSoup

def get_watcha_daily_popular_movies():
    """
    왓챠 웹페이지(또는 왓챠피디아 메인/랭킹 페이지)에서
    일간 영화 인기 순위를 가져오려 시도하는 예시 코드입니다.
    
    실제 URL, 클래스명, 태그 구조는 달라질 수 있으므로,
    개발자 도구(F12)로 확인 후 수정하세요.
    """
    # (예시) 왓챠피디아 메인 페이지를 대상으로 함
    url = "https://pedia.watcha.com/ko-KR"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("페이지 요청 중 오류가 발생했습니다:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # HTML 구조 예시 (실제로는 달라질 수 있음):
    # <section class="chart-item" ...> 안에
    # 1위부터 N위까지 리스트가 존재한다고 가정

    ranking_section = soup.find("section", class_="chart-item")
    if not ranking_section:
        print("일간 영화 인기 순위 섹션을 찾지 못했습니다. HTML 구조를 확인하세요.")
        return []

    # (가정) ranking_section 안에 영화 리스트 <li> 태그들이 있다고 가정
    movie_items = ranking_section.find_all("li", limit=10)
    
    results = []
    for idx, item in enumerate(movie_items, start=1):
        # 예: 제목이 <a class="movie-title">에 들어 있다고 가정
        title_tag = item.find("a", class_="movie-title")
        if title_tag:
            movie_title = title_tag.get_text(strip=True)
        else:
            movie_title = "영화 제목 확인 불가"
        
        results.append((idx, movie_title))

    return results

if __name__ == "__main__":
    top10_movies = get_watcha_daily_popular_movies()
    
    if not top10_movies:
        print("데이터를 가져오지 못했습니다.")
    else:
        print("왓챠 일간 인기 영화 TOP 10 (예시)")
        for rank, title in top10_movies:
            print(f"{rank}위: {title}")