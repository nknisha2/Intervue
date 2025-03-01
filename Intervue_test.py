from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.intervue.io/")
driver.maximize_window()

def take_screenshot(step_name):
    """Capture a screenshot if any step fails"""
    driver.save_screenshot(f"{step_name}_failed.png")

try:
    # Wait and click Login button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='iv-homepage-login']//span[contains(text(),'Login')]"))
    ).click()

    # Switch to new login window
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])

    # Click on Candidate Login
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/login/candidate']//div[normalize-space()='Login']"))
    ).click()

    # Enter login credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_email"))).send_keys("test@example.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_password"))).send_keys("123456")

    # Click login button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    # Verify successful login by checking if the dashboard is visible
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard')]"))
    )

    if dashboard_element:
        print("Login successful!")

    # Search for a name (e.g., "Hello")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
    )
    search_box.send_keys("Hello")
    
    # Verify search results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Hello')]"))
    )
    print("Search successful!")

    # Click Logout button
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Logout')]"))
    )
    logout_button.click()
    
    print("Logout successful!")

except Exception as e:
    print(f"Test case failed: {e}")
    take_screenshot("test_failure")

finally:
    driver.quit()
