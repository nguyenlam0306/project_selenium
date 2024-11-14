from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Đường dẫn đến ChromeDriver trên máy của bạn
driver_path = './chromedriver-win64/chromedriver.exe'  # Cập nhật đúng đường dẫn

# Khởi tạo ChromeDriver với Service
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Mở file HTML tĩnh
    driver.get("E:\CTU\PTPM\Selenum_project\index.html")

    # Kiểm tra tiêu đề trang
    assert "Static Web Test" in driver.title
    print("Title test passed")

    # Tìm và kiểm tra nội dung của thẻ h1
    header = driver.find_element(By.ID, "header")
    assert header.text == "Welcome to My Website"
    print("Header test passed")

    # Tìm nút và nhấn vào
    button = driver.find_element(By.ID, "clickMe")
    button.click()

    # Đợi trang cập nhật
    time.sleep(1)

    # Kiểm tra nội dung sau khi nhấn nút
    message = driver.find_element(By.ID, "message")
    assert message.text == "Hello, Selenium!"
    print("Button click test passed")

finally:
    # Đóng trình duyệt
    driver.quit()
