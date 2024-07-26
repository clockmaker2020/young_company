import requests
import os

def download_file(file_url, save_path):
    try:
        response = requests.get(file_url)  # 파일 URL에 GET 요청 보내기
        response.raise_for_status()  # 요청이 성공했는지 확인
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # HTTP 에러 출력
        return
    except Exception as err:
        print(f"Other error occurred: {err}")  # 기타 에러 출력
        return

    try:
        with open(save_path, 'wb') as f:  # 저장할 파일을 바이너리 쓰기 모드로 열기
            f.write(response.content)  # 응답의 내용을 파일에 쓰기
        print(f"File downloaded successfully and saved to {save_path}")
    except IOError as io_err:
        print(f"File write error: {io_err}")  # 파일 쓰기 에러 출력

# URL과 저장 경로 변수를 지정합니다.
url = 'https://apihub.kma.go.kr/api/typ03/cgi/wrn/nph-wrn7?out=0&tmef=1&city=1&name=0&tm=201611082300&lon=127.7&lat=36.1&range=300&size=685&wrn=W,R,C,D,O,V,T,S,Y,H,&authKey=zkv5nxk5SAqL-Z8ZOagKOg'
save_file_path = r'C:\Users\John\Downloads\weather_warning_image.png'  # 파일이 저장될 경로와 파일 이름

print("Starting the process...")

# 파일이 존재하는지 확인하고, 존재하지 않으면 다운로드 함수를 호출합니다.
if not os.path.exists(save_file_path):
    print(f"The file {save_file_path} does not exist. Proceeding with download.")
    download_file(url, save_file_path)
else:
    print(f"The file {save_file_path} already exists. Attempting to overwrite.")
    download_file(url, save_file_path)

print("Process finished.")
