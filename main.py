from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time

# Instantiate a new WebDriver (assuming Chrome for this example)
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the provided link
driver.get("https://www.staysucasa.com/")
print("Navigated to the link: https://www.staysucasa.com/")


# Define XPaths
Sucasa_Standard = By.XPATH, "//div[@class='main']//div[@class='container standard']//h2[contains(text(), 'The Sucasa Standard')]"
Work_From_home = By.XPATH, "//div[@class='container standard']//div[@class='d-flex flex-wrap flex-container justify-content-center justify-content-xl-between']//div[@class='standard-item']//h4[contains(text(), 'Work From Anywhere')]"
Transparent_Pricing = By.XPATH, "//div[@class='container standard']//div[@class='d-flex flex-wrap flex-container justify-content-center justify-content-xl-between']//div[@class='standard-item']//h4[contains(text(), 'Transparent Pricing')]"
Premium_Properties = By.XPATH, "//div[@class='container standard']//div[@class='d-flex flex-wrap flex-container justify-content-center justify-content-xl-between']//div[@class='standard-item']//h4[contains(text(), 'Premium Properties')]"

# Function to verify text presence in a section
def verify_text_in_section(section_xpath, text_to_verify):
    section = driver.find_element(*section_xpath)
    assert text_to_verify in section.text, f"Text '{text_to_verify}' not found in the section."

# Verify Page URL should be equal to https://www.staysucasa.com
assert driver.current_url == "https://www.staysucasa.com/", "Page URL is not as expected."
print("Verified the Page URL is https://www.staysucasa.com.")


# Take a screenshot and save it with a unique name
timestamp = datetime.datetime.now().strftime("%H-%M-%S")
screenshot_name = f"FIRST_{timestamp}.png"
driver.save_screenshot(screenshot_name)
print(f"Took a screenshot and saved as {screenshot_name}.")

# Go to The Sucasa Standard section
su = driver.find_element(*Sucasa_Standard)
time.sleep(5)
print("Clicked on The Sucasa Standard section.")


# Verify the presence of the specified texts in The Sucasa Standard section
verify_text_in_section(Work_From_home, "Work From Anywhere")
verify_text_in_section(Transparent_Pricing, "Transparent Pricing")
verify_text_in_section(Premium_Properties, "Premium Properties")
print("Verified texts in The Sucasa Standard section.")

# Go to Work From Anywhere section
driver.find_element(*Work_From_home)
print("Clicked on Work From Anywhere section.")



# Close the browser window
driver.quit()
print("Browser closed.")
