from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from sql_connector import MySQL

driver_path = 'C:\\Users\\Rene\\projects\\python\\scraper\\chromedriver.exe'

def innit_driver():
  driver = webdriver.Chrome(service=Service(executable_path=driver_path))

  driver.get("https://www.bing.com/translator")
  driver.implicitly_wait(0.5)

  src_options = driver.find_element(by=By.ID, value="tta_srcsl")
  src_options.click()
  src_options.find_element(by=By.CSS_SELECTOR, value="option[value=es]").click()

  src_options = driver.find_element(by=By.ID, value="tta_tgtsl")
  src_options.click()
  src_options.find_element(by=By.CSS_SELECTOR, value="option[value=ca]").click()

  return driver

wait_translation = lambda d : d.find_element(By.CSS_SELECTOR, "div[class=tta_playc]")

models = [
  "answer",
  "community",
  "content",
  "course",
  "feedback",
  "key",
  "material_type",
  "perspective",
  "province",
  "question",
  "resource",
  "sub_answer",
  "toolkit",
] 

lang = {
  1: "ES",
  2: "CA",
}

def translate_phrases():
  driver = innit_driver()

  input_box = driver.find_element(by=By.ID, value="tta_input_ta")
  output_box = driver.find_element(by=By.ID, value="tta_output_ta")
  clear_btn = driver.find_element(by=By.ID, value="tta_clear")

  sql = MySQL('answer')
  sql.init()
  tuples = sql.fetch()

  count = 0

  for item in tuples:
    values = []

    for i, value in enumerate(item):
      localed = value

      if(i == 0):
        localed = 2

      if(type(localed) == str and len(localed) > 2):
        input_box.send_keys(value)
        WebDriverWait(driver, timeout=60).until(wait_translation)
        localed = output_box.get_attribute('value')
        
        clear_btn.click()

      values.append(localed)

    sql.create(tuple(values))
    count += 1
    print(count)

    if(count % 5 == 0):
      sql.commit()

  if(count % 5 != 0):
    sql.commit()
  driver.quit()

translate_phrases()
