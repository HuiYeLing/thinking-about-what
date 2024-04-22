import requests
from bs4 import BeautifulSoup

def fetch_web_title(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # �����Ӧ��״̬�벻��200�����׳��쳣
        response.encoding = response.apparent_encoding  # �������ݷ���������Ӧ���ݱ��뷽ʽ
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title
        if title is not None:
            return title.text
        else:
            return "No title found"
    except requests.RequestException as e:
        print(f"Failed to fetch web title: {e}")
        return None

url = 'http://192.168.30.10:8080/acmhome/showstatus.do?problemId=null&contestId=null&userName=null&result=&language=&page=2'
title = fetch_web_title(url)
if title is not None:
    print(title)