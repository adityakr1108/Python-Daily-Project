from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Option 2: (Preferred) Using webdriver_manager to automatically handle ChromeDriver installation
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Optional: maximize window (you can also set window size)
driver.maximize_window()

# Navigate to a webpage
driver.get('https://www.geeksforgeeks.org/top-data-science-projects/#web-scraping-projects')
#driver.get('https://www.geeksforgeeks.org/top-data-science-projects/#web-scraping-projects')

# Close the driver after usage
driver.quit()
