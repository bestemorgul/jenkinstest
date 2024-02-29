from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

s = Service('/home/bestemorgul/chromedriver')
driver=webdriver.Chrome(service=s)

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
