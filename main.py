from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print(Fore.GREEN+"😎 😎 Welcome to Wodpecker 😎 😎"+Style.BRIGHT)
print(Fore.BLUE+"😎 😎 I will do jobsearch for you 😎 😎"+Style.RESET_ALL)

print(Fore.YELLOW+"For this i need some information 🤔, Dont worry i will keep it private"+Style.RESET_ALL)
print("🫣🫣")
username = input(Fore.CYAN+"Enter your linked in username : "+Style.RESET_ALL)
print("🫣🫣")
password = getpass.getpass(Fore.CYAN+"Enter your password : "+Style.RESET_ALL)

print(Fore.GREEN+"Ok, Sit back and relax, i will do it"+Style.RESET_ALL)


# Automatically download and use the correct ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open LinkedIn
driver.get("https://www.linkedin.com")
driver.maximize_window()

# login to linkedin
# implicitly wait for 5 sec to lead the button
driver.implicitly_wait(5)

# click in login button
sign_in_button = driver.find_element(By.XPATH, "//a[contains(@class, 'sign-in-form__sign-in-cta')]")
sign_in_button.click()

# wait for load
driver.implicitly_wait(5)
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys(username)
password_input.send_keys(password)

# submit
sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
sign_in_button.click()

driver.implicitly_wait(20)

# find search box
search_box = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")

# Enter a search query
search_box.send_keys("hiring python")

driver.implicitly_wait(6)

# Press Enter to search
search_box.send_keys(Keys.RETURN)

# wait for results
driver.implicitly_wait(6)

# FILTER 1
# click in post button to fiter out
post_filter_button = driver.find_element(By.CLASS_NAME, "search-reusables__filter-pill-button")
post_filter_button.click()
driver.implicitly_wait(15)

# FILTER 2
# click in date posted button to fiter out
date_posted_filter_button = driver.find_element(By.ID, "searchFilter_datePosted")
date_posted_filter_button.click()

driver.implicitly_wait(5)

# Find the radio button by ID and click
label = driver.find_element(By.XPATH, "//label[@for='datePosted-past-week']")
label.click()

# click in show results
download_button_path = "//div[contains(@class, 'artdeco-modal')]//button[@aria-label='Apply current filter to show results']"

wait = WebDriverWait(driver, 10)
download_button = wait.until(EC.element_to_be_clickable((By.XPATH, download_button_path)))
download_button.click()

driver.implicitly_wait(15)

# Keep browser open
input("Press Enter to exit...")
driver.quit()
