######## Selenium
#### clutch.co
#### https://clutch.co/agencies/digital-marketing?client_type=field_pp_cs_enterprise&client_type=field_pp_cs_midmarket

# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By  # For locating elements
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import pandas as pd  # For working with dataframes
import undetected_chromedriver as uc

# Initialize empty lists to store data
names = []
locations = []
websites = []
summaries = []

# Create a ChromeOptions object
options = uc.ChromeOptions()

# Add the "--disable-popup-blocking" argument to the ChromeOptions
options.add_argument("--disable-popup-blocking")

driver = uc.Chrome(options=options)

# Open the target website
driver.get('https://clutch.co/agencies/digital-marketing?client_type=field_pp_cs_enterprise&client_type=field_pp_cs_midmarket')

# Wait for 1 second to allow the page to load
time.sleep(1)

# Close pop-up
driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonAccept"]').click()

time.sleep(1)

# Initialize a variable to keep track of the page number
page = 0

# Initialize a variable to control the loop
next_button_enabled = True

while next_button_enabled:

    # Wait for 3 seconds before proceeding
    time.sleep(3)

    # Find the container element that holds the listings
    countainer = driver.find_element(By.XPATH , '//ul [ @class = "directory-list" ]')

    # Find all the listing elements within the container
    listing = countainer.find_elements( By.XPATH , './li' )
    
    time.sleep(1)

    # Loop through each listing
    for ls in listing:

        # Try to extract the name of the company from the listing
        try :
            name = ls.find_element(By.XPATH, './/h3[@class="company_info"]').text
            names.append(name)
        except:
            name = None
            names.append(name)
        
        # Try to extract the location of the company from the listing
        try :
            location = ls.find_element(By.XPATH, './/span [ @class = "locality" ]').text
            locations.append(location)
        except:
            location = None
            locations.append(location)

       # Try to extract the website of the company from the listing
        try :
            web = ls.find_element(By.XPATH, './/ul [ @class = "nav-right-profile" ]/li/a').get_attribute("href")
            websites.append(web)
        except:
            web = None
            websites.append(web)

       
        # Print the extracted data for the current listing
        print(name, ":", location, ":", web )
   
    # Increment the page number
    page += 1

    if page == 10:
        break

    # Check if there is a next page button and click it
    try:
        next_page = driver.find_element(By.XPATH, '//*[@id="providers"]/nav/ul/li[@class="page-item next"]/a').click()
    except:
        next_button_enabled = False

        # Print the status of the current page
    print(f'page{page}: Done')
        

# Create a pandas DataFrame from the scraped data
df = pd.DataFrame(list(zip(names, locations, websites)), columns=["Name", "Location", "Website"])

# Save the DataFrame to a CSV file
df.to_csv("agencies.csv", index=False, encoding="utf-8-sig")

# Quit the browser
driver.quit()






