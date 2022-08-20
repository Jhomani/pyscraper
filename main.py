from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

def test_eight_components():
  driver = webdriver.Firefox(service=Service(executable_path='/home/jhomani/projects/python/geckodriver'))

  driver.get("https://www.bing.com/translator")
  driver.implicitly_wait(0.5)

  src_options = driver.find_element(by=By.ID, value="tta_srcsl")
  src_options.click()
  option = src_options.find_element(by=By.CSS_SELECTOR, value="option[value=es]")
  option.click()

  src_options = driver.find_element(by=By.ID, value="tta_tgtsl")
  src_options.click()
  option = src_options.find_element(by=By.CSS_SELECTOR, value="option[value=ca]")
  option.click()

  text_box = driver.find_element(by=By.ID, value="tta_input_ta")

  large_text = "En ese ejemplo, pasamos una función anónima (pero también podríamos definirla explícitamente como lo hicimos anteriormente para que pueda ser reutilizada). El primer y único argumento que se pasa a nuestra condición es siempre una referencia a nuestro objeto controlador, WebDriver. En un entorno de subprocesos múltiples, debe tener cuidado de operar con la referencia del controlador pasada a la condición en lugar de la referencia al controlador en el ámbito externo."

  text_box.send_keys(large_text)

  WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME,"tta_playc"))

  target_box = driver.find_element(by=By.ID, value="tta_output_ta")

  # for el in spans_with_target:
  print(target_box.get_attribute('value'))

  # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


  # submit_button.click()

  # message = driver.find_element(by=By.ID, value="message")

  # value = message.text

  # print(value)

  # assert value == "Received!"

  driver.quit()

test_eight_components()