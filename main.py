from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib.parse

print(Fore.GREEN+"😎 😎 Welcome to Wodpecker 😎 😎"+Style.BRIGHT)
print(Fore.BLUE+"😎 😎 I will do jobsearch for you 😎 😎"+Style.RESET_ALL)

print(Fore.YELLOW+"For this i need some information 🤔, Dont worry i will keep it private"+Style.RESET_ALL)
print("🫣🫣")
username = input(Fore.CYAN+"Enter your linked in username : "+Style.RESET_ALL)
print("🫣🫣")
password = getpass.getpass(Fore.CYAN+"Enter your password : "+Style.RESET_ALL)

print(Fore.GREEN+"Ok, Sit back and relax, i will do it"+Style.RESET_ALL)

print("For what role you are looking for")
job_role = getpass.getpass(Fore.CYAN+"Enter your Role : "+Style.RESET_ALL)

# Automatically download and use the correct ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def url_encode(text: str) -> str:
    return urllib.parse.quote(text)

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


# v2
url = f"https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords={url_encode(job_role)}&origin=FACETED_SEARCH&sid=be%3A"
driver.get(url)


# now we are in the page


driver.implicitly_wait(15)

# Keep browser open
input("Press Enter to exit...")
driver.quit()
