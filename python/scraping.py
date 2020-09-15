from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONST
URL = 'https://www.netflix.com/jp/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse%2Fgenre%2F34399'
DRIVER_PATH = './chromedriver.exe'
ID = 'ps34h.k.r@gmail.com'
PASSWORD = 'ryusuke43'


def main():
    # Seleniumをあらゆる環境で起動させるChromeオプション
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--proxy-server="direct://"')
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')  # ※ヘッドレスモードを使用する場合、コメントアウトを外す

    # ブラウザの起動
    driver = webdriver.Chrome(
        executable_path=DRIVER_PATH, options=options)

    # 待機処理
    wait = WebDriverWait(driver, 10)

    # ページに遷移
    driver.get(URL)

    # 待機
    wait.until(EC.visibility_of_all_elements_located)

    # id入力
    id = driver.find_element_by_id('id_userLoginId')
    id.send_keys(ID)

    # パスワード入力
    password = driver.find_element_by_id('id_password')
    password.send_keys(PASSWORD)

    # クリック
    buttons = driver.find_elements_by_tag_name('button')

    for button in buttons:
        if button.text == 'ログイン':
            button.click()
            break


if __name__ == '__main__':
    main()
