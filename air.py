
import requests
import pandas as pd

def get_air_quality_data():
    API_KEY = "YOUR_API_KEY"  # 공공데이터포털에서 발급받은 API 키 입력
    URL = "http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst"
    
    params = {
        "serviceKey": API_KEY,
        "returnType": "json",
        "numOfRows": 100,
        "pageNo": 1,
        "sidoName": "전국",  # 전국 데이터 조회
        "searchCondition": "DAILY"  # 일별 데이터
    }
    
    response = requests.get(URL, params=params)
    data = response.json()
    
    return data["response"]["body"]["items"]

def get_top10_cleanest_cities():
    data = get_air_quality_data()
    df = pd.DataFrame(data)
    
    # PM10(미세먼지) 및 PM2.5(초미세먼지) 기준으로 정렬하여 상위 10개 도시 선정
    df["pm10Value"] = pd.to_numeric(df["pm10Value"], errors='coerce')
    df["pm25Value"] = pd.to_numeric(df["pm25Value"], errors='coerce')
    df_clean = df.sort_values(by=["pm10Value", "pm25Value"], ascending=[True, True]).head(10)
    
    return df_clean[["cityName", "pm10Value", "pm25Value"]]

if __name__ == "__main__":
    top10_cities = get_top10_cleanest_cities()
    print(top10_cities)