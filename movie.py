import requests
from bs4 import BeautifulSoup

def scrape_rotten_tomatoes_top10():
    url = "https://www.rottentomatoes.com/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("페이지 요청 중 에러 발생:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    #───────────────────────────────────────────────────────────
    # (예시) 메인 페이지 내에서 'Top Box Office' 섹션을 찾아
    # 영화 제목 10개를 가져온다고 가정. 실제 구조는 달라질 수 있음.
    # 개발자 도구로 해당 영역의 class나 태그를 먼저 확인해야 합니다.
    #───────────────────────────────────────────────────────────

    # 예: <section id="Top-Box-Office" ...> 같은 요소가 있을 수 있음
    # 실제로는 class나 id가 다를 수 있으므로 개발자 도구로 확인 필수
    box_office_section = soup.find("section", id="Top-Box-Office")  
    if not box_office_section:
        print("Top-Box-Office 섹션을 찾지 못했습니다. HTML 구조가 달라졌을 수 있습니다.")
        return []

    # 이후, 섹션 안에 있는 영화 목록 항목들(예: li, div 등)을 찾아서 10개만 추출
    movie_items = box_office_section.find_all("li", limit=10)
    
    results = []
    for idx, item in enumerate(movie_items, start=1):
        # 영화 제목이 들어 있는 태그를 찾아 get_text(). 
        # 예: <a> 태그 안에 movieTitle 이 있다고 가정.
        # 실제 구조는 확인 후 수정해야 합니다.
        title_tag = item.find("a", class_="movieTitle")  
        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            # 만약 해당 태그가 없다면, 다른 태그를 찾거나 기본값 설정
            title = "제목 정보 없음"
        
        results.append((idx, title))

    return results

if __name__ == "__main__":
    top10_movies = scrape_rotten_tomatoes_top10()
    if not top10_movies:
        print("데이터를 가져오지 못했습니다.")
    else:
        print("로튼토마토 영화 순위 (예시) TOP 10")
        for rank, movie_title in top10_movies:
            print(f"{rank}위: {movie_title}")