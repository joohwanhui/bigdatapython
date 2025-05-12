import func

# 사용자의 입력을 받아서 멜론 차트 출력 프로그램 만들기
# 각각 기능(함수)을 만들어서 메인 파일에서 코드 작성
print("===================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("6. 파일에 저장(멜론100)")
print("===================")
# 만약에 1을 입력하면
# func.m100("멜론 100")
# 만약에 2를 입력하면
# func.m50("멜론 50")

# func.m10("멜론 10")
# func.m000("멜론 내맘데로 출력", 7)
# func.m_random("노래추천 기능")

# func.m_save_csv("파일에 저장(멜론100)")

choice = input("원하는 기능을 선택하세요: ")

if choice == '1':
    func.m100("멜론 100 차트")
elif choice == '2':
    func.m50("멜론 50 차트")
elif choice == '3':
    func.m10("멜론 10 차트")
elif choice == '4':
    func.m_random("AI 추천 노래 기능")
elif choice == '5':
    print("[가수 이름 검색 기능은 현재 준비 중입니다.]")
    print("===================")
elif choice == '6':
    # Call the new m_save_csv function
    func.m_save_csv("멜론 100 차트를 CSV 파일로 저장")
elif choice == '0':
    print("[프로그램을 종료합니다.]")
else:
    print("[잘못된 입력입니다. 1, 2, 3, 4, 5, 6 또는 0을 입력하세요.]")
    print("===================")