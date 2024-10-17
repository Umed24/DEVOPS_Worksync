import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Config:
    BASE_URL = "http://54.224.132.202:3000"
    SIGNUP_URL = f"{BASE_URL}/signup"
    LOGIN_URL = f"{BASE_URL}/login"

# Provide the path to your locally installed ChromeDriver
CHROME_DRIVER_PATH = r'C:\Users\Umed\OneDrive\Desktop\Worksync-main (2)\Worksync-main\chromedriver-win64\chromedriver.exe'

# List of user credentials for testing
user_credentials = [
    {"email": "testuser1@example.com", "password": "password123", "username": "TestUser1"},
    {"email": "testuser2@example.com", "password": "password456", "username": "TestUser2"},
]

class TestSignupLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup Chrome WebDriver with options to ignore SSL certificate errors
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors=yes")
        
        cls.service = Service(CHROME_DRIVER_PATH)
        cls.driver = webdriver.Chrome(service=cls.service, options=chrome_options)
        cls.driver.implicitly_wait(10)

    def test_signup_and_login(self):
        for user in user_credentials:
            test_email = user["email"]
            test_password = user["password"]
            test_username = user["username"]

            try:
                # Test the Sign-Up Functionality
                self.driver.get(Config.SIGNUP_URL)

                # Fill in the sign-up form
                self.driver.find_element(By.NAME, "email").send_keys(test_email)
                self.driver.find_element(By.NAME, "username").send_keys(test_username)
                self.driver.find_element(By.NAME, "password").send_keys(test_password)

                # Submit the sign-up form
                self.driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

                # Wait for the sign-up to complete and check for success message
                WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Account created!')]"))
                )
                print(f"Sign Up Test Passed for {test_email}")

                # Test the Login Functionality
                self.driver.get(Config.LOGIN_URL)

                # Fill in the login form
                self.driver.find_element(By.NAME, "username").send_keys(test_username)
                self.driver.find_element(By.NAME, "password").send_keys(test_password)

                # Click the login button
                self.driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

                # Wait for the login to complete and check for successful navigation
                WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Add Task')]"))
                )
                print(f"Login Test Passed for {test_email}")

            except Exception as e:
                print(f"Test failed for {test_email}: {e}")
                print(f"Current URL: {self.driver.current_url}")
                print(f"Page Title: {self.driver.title}")

            finally:
                # Navigate back to the sign-up page before the next iteration
                self.driver.get(Config.SIGNUP_URL)

    @classmethod
    def tearDownClass(cls):
        # Cleanup the WebDriver
        cls.driver.quit()
        cls.service.stop()

if __name__ == "__main__":
    unittest.main()
