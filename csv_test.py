import csv

data = """순위,제목,가수
1,곡 제목1,가수1
2,곡 제목2,가수2
3,곡 제목3,가수3"""

# 문자열 데이터를 파일처럼 처리하기 위해 StringIO 사용
import io

file = io.StringIO(data)

reader = csv.reader(file)

# 헤더 출력
header = next(reader)
print(header)

# 데이터 출력
for row in reader:
    print(row)