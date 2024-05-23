import re

import requests
from bs4 import BeautifulSoup
import sys

def get_class_values_from_url(url):
    print("url :: ", url)

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 클래스명에 해당하는 모든 요소를 찾음
        elements = soup.find_all(class_="bd_1g_zz")
        # 클래스명에 해당하는 값들을 추출하여 리스트에 저장
        values = [element.text.strip() for element in elements]
        return values
    else:
        print("Failed :: ", response.status_code)
        return []


def extract_number_from_value(value):
    match = re.search(r'(\d+)(?=개마다 부과)', value)
    print('dddddddddddddddddddddddd', match)
    if match:
        number = match.group(1) #매치된문자열중 첫번째그룹
        print(f"개마다 부과 앞 숫자: {number}")
        return number
    else:
        print("일치하는 패턴이 없습니다.")
        return None

url = sys.argv[1]
class_values = get_class_values_from_url(url)
result = None
for value in class_values:
    number = extract_number_from_value(value)
    if number:
        result = number
        break



# if __name__ == "__main__":
#     # URL을 명령행에서 입력받음
#     url = sys.argv[1]
#
#     # 함수 호출하여 클래스명에 해당하는 값들을 가져옴
#     class_values = get_class_values_from_url(url)
#     for value in class_values:
#         number = extract_number_from_value(value)
#         if number:
#             break