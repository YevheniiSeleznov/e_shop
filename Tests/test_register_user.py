from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_register_user():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Navigate to the registration page
    driver.get("https://demowebshop.tricentis.com/register")

    # Fill in the registration form
    driver.find_element(By.ID, "FirstName").send_keys("Yevhenii")
    driver.find_element(By.ID, "LastName").send_keys("Doe")
    driver.find_element(By.ID, "Email").send_keys("Yevhenii.Selia@example.com")
    driver.find_element(By.ID, "Password").send_keys("Test@123")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@123")

    # Submit the registration form
    driver.find_element(By.CSS_SELECTOR, 'input[value="Register"]').click()

    # Wait for registration to complete (you might want to enhance this part based on the actual behavior of the website)
    time.sleep(3)

    # Verify that registration was successful
    success_message = driver.find_element(By.CLASS_NAME, "result").text
    assert "Your registration completed" in success_message

    # Close the browser
    driver.quit()

# Run the test
test_register_user()
