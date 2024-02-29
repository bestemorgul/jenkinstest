from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")

options.add_argument(r"--user-data-dir=/home/luiz/.config/google-chrome/")
options.add_argument(r'--profile-directory=Default')
driver = webdriver.Chrome(options=options)


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
