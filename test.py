from selenium import webdriver
from platform import platform

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.ft.com")
filename = f"{platform()}.png"
el = driver.find_element_by_tag_name('body')
driver.set_window_size(el.size["width"], el.size["height"])
driver.save_screenshot(filename)
driver.close()
print(f"saved {filename}")
