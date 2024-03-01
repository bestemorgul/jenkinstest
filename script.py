from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
option.add_argument('disable-notifications')
option.add_argument('allow-running-insecure-content')
option.add_argument('headless')
option.add_argument("remote-debugging-port=9222")
option.add_argument("window-size=1280x800")
options.add_argument('no-sandbox')
options.add_argument('disable-gpu')
driver = webdriver.Chrome(options=option)

try:
    # Google'a gidin
    driver.get("https://www.google.com")

    # Arama kutusunu bulun
    search_box = driver.find_element("name", "q")

    # Arama yapın
    search_box.send_keys("Python Selenium Dockerize")

    # Enter tuşuna basın
    search_box.submit()

    # Sayfanın yüklenmesini bekleyin
    time.sleep(5)

    # Sayfa başlığını yazdırın
    print("Arama Sonuçları Sayfasının Başlığı:", driver.title)

finally:
    # Tarayıcı penceresini kapat
    driver.quit()
