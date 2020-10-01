
import requests
from bs4 import BeautifulSoup
import sys

PATH = '/mnt/c/Users/Ryusuke/wsl_home/pro/html/shiryo/'


def main():
    # コマンドライン引数からURL取得
    url = sys.argv[1]

    # コマンドライン引数からファイル名取得
    filename = PATH + sys.argv[2]

    # HTML取得
    r = requests.get(url)

    # HTMLの書き込み
    with open(filename, mode='w') as f:
        f.write(r.text)


if __name__ == '__main__':
    main()
