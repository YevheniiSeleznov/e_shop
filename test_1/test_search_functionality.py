from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_functionality():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the EPAM homepage
    driver.get("https://www.epam.com/")

    try:
        # Locate the search input field
        search_input = driver.find_element(By.XPATH, "//input[@id='headerSearch']")

        # Type the search query "AI"
        search_input.send_keys("AI")

        # Submit the search form
        search_input.submit()

        # Wait for the search results to load (adjust the wait time based on your page load time)
        driver.implicitly_wait(10)

        # Check if the search results are displayed
        search_results = driver.find_elements(By.XPATH, "//div[@class='search-results-item']")

        assert search_results, "Search results not found for the query 'AI'"

    finally:
        # Close the browser
        driver.quit()


# Run the test
test_search_functionality()
