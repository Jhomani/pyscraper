# Schedule Tasks on Windows
# SCHTASKS /CREATE /SC DAILY /TN "MyTasks\EnterToWork Task" /TR "C:\Users\Rene\projects\python\scraper\cron_job.bat" /ST 7:28
# SCHTASKS /CREATE /SC DAILY /TN "MyTasks\ReturningFromLaunching Task" /TR "C:\Users\Rene\projects\python\scraper\cron_job.bat" /ST 14:29
# SCHTASKS /CREATE /SC DAILY /TN "MyTasks\GoToLaunching Task" /TR "C:\Users\Rene\projects\python\scraper\cron_job.bat" /ST 13:02
# SCHTASKS /CREATE /SC DAILY /TN "MyTasks\GetOutFromWork Task" /TR "C:\Users\Rene\projects\python\scraper\cron_job.bat" /ST 18:02 

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

config = {
  'uri': 'https://odoo.develoop.net/web#action=133&cids=1&menu_id=95',
  'driver_path':'C:\\Users\\Rene\\projects\\python\\scraper\\geckodriver.exe',
  'binary': r"C:\Program Files\Mozilla Firefox\firefox.exe",
  'target': 'o_hr_attendance_sign_in_out_icon',
}

def innit_driver():
  options = Options()
  options.binary_location=config['binary']
  options.add_argument('--headless')

  driver = webdriver.Firefox(
    service=Service(
      executable_path=config['driver_path'],
      log_path="C:\\Users\\Rene\\projects\\python\\scraper\\geckodriver.log",
    ),
    options=options
  )

  driver.get(config['uri'])
  driver.implicitly_wait(0.5)

  return driver

wait_translation = lambda driver: driver.find_element(By.CLASS_NAME, config['target'])
def translate_phrases():
  driver = innit_driver()

  driver.find_element(by=By.ID, value="login").send_keys('jmamani@develoop.net')
  driver.find_element(by=By.ID, value="password").send_keys('34353435')


  driver.find_element(by=By.CSS_SELECTOR, value="button[type=submit]").click()

  WebDriverWait(driver, timeout=60).until(wait_translation)

  driver.find_element(By.CLASS_NAME, config['target']).click()

  driver.quit()

translate_phrases()
