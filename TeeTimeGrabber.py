import requests; #library to send HTTP requests
from selenium import webdriver; #this library will help us interact with the site
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


#SSL certificate was valid, but we could not parse the server. Wrote this fix
#to disable the Selenium certificate validation in the meantime
options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

#go to website
url = "https://www.costamesacountryclub.com/";
driver.get(url);
driver.maximize_window()

#clicking the tee time button
tee_time_button = driver.find_element(By.LINK_TEXT, "Book a Tee Time");
tee_time_button.click();
print("Successfully selected Book a Tee Time")
time.sleep(2)

#Switch to Iframe to click the buttons in iframe
iframe_xpath = 'teeleader'
iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, iframe_xpath)))
print("Successfully switched to iFrame")

#Calendar Button - Select Date
saturday_parent_element = driver.find_element(By.XPATH, '//div[@class="react-calendar__month-view__days"]')
saturday_button = saturday_parent_element.find_element(By.XPATH, './button[21]')
saturday_button.click()
print("Successfuly Selected Date") 
time.sleep(2)

#Select the time 
tee_time = driver.find_element(By. XPATH, '//*[@id="app-container"]/div/div[2]/div/div[2]/div[2]/div/div[4]/div/button')
actions = ActionChains(driver)
actions.click(tee_time).perform()
print("Successfully clicked Tee Time button")
time.sleep(2)

#Select Amount of Golfers
amount_of_golfers = driver.find_element(By.XPATH, '//*[@id="app-body"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/button')
amount_actions = ActionChains(driver)
amount_actions.click(amount_of_golfers).perform()
print("Successfully Selected 2 Golfers")
time.sleep(2)

#Checkout
checkout = driver.find_element(By.XPATH, '//*[@id="app-body"]/div[2]/div[3]/div/div[3]/div/button[2]')
checkout_actions = ActionChains(driver)
checkout_actions.click(checkout).perform()
print("Successfully Checked Out")
time.sleep(2)

#checkout as guest
email_field = driver.find_element(By.XPATH, '//*[@id="txtGuestEmailAddress"]')
email_field.send_keys('Email')
continue_as_guest = driver.find_element(By.XPATH, '//*[@id="login"]/div[2]/div[1]/div[2]/div/form/div/div[2]/button')
continue_as_guest_actions = ActionChains(driver)
continue_as_guest_actions.click(continue_as_guest).perform()
print("Successfully Continued as Guest")
time.sleep(2)

#payment information
name_field = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/input')
name_field.send_keys('Name')

phone = driver.find_element(By.XPATH, '//*[@id="phone-form-control"]')
phone.send_keys("phone number here")


card = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/input')
card.send_keys('Card info here')

# Find the dropdown element and click on it to open the options
month_drop = driver.find_element(By.XPATH, '//*[@id="mui-component-select-Payment.CC.ExpirationMonth"]')
month_drop.click()

# Wait for the dropdown options to appear
month_wait = WebDriverWait(driver, 5)
month_options = month_wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="menu-Payment.CC.ExpirationMonth"]/div[3]/ul/li')))

# Select the desired month
desired_month = 'desired month'  # Replace with the month you want to select

# Iterate over the options and click on the desired month
for option in month_options:
    if option.text == desired_month:
        option.click()
        break

year_drop = driver.find_element(By.XPATH, '//*[@id="mui-component-select-Payment.CC.ExpirationYear"]')
year_drop.click()

year_wait = WebDriverWait(driver, 2)
year_options = year_wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="menu-Payment.CC.ExpirationYear"]/div[3]/ul/li')))
desired_year = 'desired year'

for year in year_options:
    if year.text == desired_year:
        year.click()
        break

cvv_field = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div[3]/div/div/div/input')
cvv_field.send_keys('CVV')

card_name_field = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/input')
card_name_field.send_keys('Name')

address = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[4]/div/input')
address.send_keys("Address")
                                            
zipcode = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[5]/div[1]/div/input')
zipcode.send_keys("Zip Code")

country_drop = driver.find_element(By.XPATH, '//*[@id="mui-component-select-Payment.Address.Country"]')
country_drop.click()

country_wait = WebDriverWait(driver, 2)
country_options = country_wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="menu-Payment.Address.Country"]/div[3]/ul/li')))
desired_country = 'United States'

for country in country_options:
    if country.text == desired_country:
        country.click()
        break

checkbox = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/label/span[1]/span[1]/input').click()
checkbox_actions = ActionChains(driver)
checkbox_actions.click(checkbox).perform()
print("Successfully Entered Information and Agreed to Terms")

complete = driver.find_element(By.XPATH, '//*[@id="app-container"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/button')
complete_actions = ActionChains(driver)
complete_actions.click(complete).perform();
wait = WebDriverWait(driver, 10);
confirmation = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]")))

print("Congratulations on your Tee Time")