import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_download_report():
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    # Open the EPAM about page
    driver.get("https://www.epam.com/about")

    try:
        # Locate the link to download the report
        download_link = driver.find_element(By.XPATH, "//a[contains(@href,'Corporate_Overview_2023_Report')]")

        # Get the download link URL
        download_url = download_link.get_attribute("href")

        # Extract the filename from the URL
        file_name = os.path.basename(download_url)

        # Download the file
        driver.get(download_url)

        # Wait for the file to download (adjust the wait time based on your network speed)
        time.sleep(5)

        # Check if the file exists in the Downloads directory
        downloads_directory = os.path.expanduser("~") + "/Downloads/"
        file_path = os.path.join(downloads_directory, file_name)

        # Assert that the file exists
        assert os.path.exists(file_path), f"File not found: {file_path}"

        # Assert that the file has the correct extension (adjust the expected extension)
        expected_extension = ".pdf"  # Adjust the expected extension based on the actual file type
        assert file_name.endswith(expected_extension), f"Unexpected file extension: {file_name}"

    finally:
        # Close the browser
        driver.quit()

# Run the test
test_download_report()
