from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

def get_youtube_trending():
    options = Options()
    options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.youtube.com/feed/trending")
    
    time.sleep(5)  # 페이지 로딩 대기
    
    videos = driver.find_elements(By.XPATH, "//h3[@class='style-scope ytd-video-renderer']/a")
    
    trending_videos = []
    for video in videos[:10]:  # Top 10 videos
        title = video.text.strip()
        link = video.get_attribute("href")
        trending_videos.append({"title": title, "link": link})
    
    driver.quit()
    
    return pd.DataFrame(trending_videos)

if __name__ == "__main__":
    top10_videos = get_youtube_trending()
    print(top10_videos)