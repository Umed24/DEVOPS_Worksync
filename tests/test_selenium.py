import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSignupLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Specify the path to chromedriver.exe
        chrome_driver_path = r"C:\Users\Umed\Downloads\Worksync-main (2)\Worksync-main\chromedriver-win64\chromedriver.exe"  # Adjust to your path
        cls.service = Service(chrome_driver_path)
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)  # Set an implicit wait

    def test_signup_and_login(self):
        # Step 1: Open the Signup page
        self.driver.get("http://localhost:3000/signup")  # Change to your app's URL

        # Step 2: Wait for the signup heading to appear
        wait = WebDriverWait(self.driver, 20)
        signup_heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Signup')]")))
        self.assertIsNotNone(signup_heading)  # Ensure we are on the signup page

        # Step 3: Fill in the signup form
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("password123")
        
        # Step 4: Submit the signup form
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'SignUp')]").click()

        # Step 5: Wait for redirection to login page
        login_button_text = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Already having an account? Login here")))
        self.assertIsNotNone(login_button_text)

        # Step 6: Click the login link and verify redirection
        login_button_text.click()
        login_heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Login')]")))
        self.assertIsNotNone(login_heading)  # Ensure we are on the login page

        # Step 7: Perform login
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("password123")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()

        # Step 8: Verify redirection to the home page after login
        home_page_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Add Task')]")))
        self.assertIsNotNone(home_page_text)  # Ensure the user is logged in and on the home page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.service.stop()

if __name__ == "__main__":
    unittest.main()
