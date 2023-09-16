import os.path

from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from config import load_config

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")


def spider_entire_website(driver: webdriver.Chrome, url: str, xpath: str, ignored_paths: list, visited_paths: list):
    driver.get(url)
    # TODO 
    # PROBLEM WITH THIS: list will explode
    # Must clean it up (remove the oldest values when it reaches a certain threshold?)
    visited_paths.append(url)

    # Get relevant information of this page
    # TODO 
    #
    #

    elems = driver.find_elements(By.XPATH, xpath)
    # print(elems)
    elems_hrefs = []
    # Get all the hrefs values
    for elem in elems:
        try:
            elems_hrefs.append(elem.get_attribute("href"))
        except StaleElementReferenceException:
            pass
    # Remove all duplicate links
    elems_hrefs = list(dict.fromkeys(elems_hrefs))
    # base case: empty hrefs list
    if len(elems_hrefs) == 0:
        return
    for element_href in elems_hrefs:
        if element_href in ignored_paths or element_href in visited_paths:
            # base case: path is in ignored_paths
            continue
        if 'https://supercasa.pt' not in element_href:
            # base case: not in the https://supercasa.pt website
            continue 
        use_current_path = 1
        for path in ignored_paths:
            if path in element_href:
                use_current_path = 0
                break
        if use_current_path:
            print(element_href)
            # Recursive calls to get hrefs 
            spider_entire_website(driver, element_href, xpath, ignored_paths, visited_paths)


def extract_house_information(driver, house_href):
    driver.get(house_href)
    # Get all relevant information from the house
    try:
        property_title = driver.find_element(By.CLASS_NAME, 'property-title').text
    except:
        property_title = ''

    print(property_title)

    try:
        property_price = driver.find_element(By.CLASS_NAME, 'property-price').text
    except:
        property_price = ''

    print(property_price)

    try:
        property_list_title = driver.find_element(By.CLASS_NAME, 'property-list-title').text
    except:
        property_list_title = ''

    print(property_list_title)

    try:
        property_features = driver.find_elements(By.CLASS_NAME, 'property-features')
        property_features = [property_feature.text for property_feature in property_features]
    except:
        property_features = []

    
    print(property_features)

    try:
        property_features_highlights = driver.find_element(By.CLASS_NAME, 'property-features highlights')
        property_features_highlights = [highlight.text for highlight in property_features_highlights]
    except:
        property_features_highlights = []

    
    print(property_features_highlights)

    try:
        detail_info_description_txt = driver.find_element(By.CLASS_NAME, 'detail-info-description-txt').text
    except:
        detail_info_description_txt = ''

    print(detail_info_description_txt)

    # TODO: Get detail-info-features-list class information
    
    # Save the information into a dictionary
    house_information = {
        'Link': house_href,
        'Title': property_title,
        'Price': property_price,
        'Location': property_list_title,
        'Features': property_features,
        'Highlights': property_features_highlights,
        'Description text': detail_info_description_txt
    }

    return house_information


def spider_specific_house_locations(driver, url, house_location_list, current_page):
    # * Use pagination the click function of selenium to click on the next page (the website must use pagination)
    # * Access only the div that contains the list with the relevant links to the houses
    # *
    driver.get(url)
    houses_class = driver.find_elements(By.CLASS_NAME, 'property-link')
    houses_hrefs = [house.get_attribute('href') for house in houses_class]

    print(houses_hrefs)
    # Get relevant information of all the houses found
    for house_href in houses_hrefs:
        house_dict = extract_house_information(driver, house_href)

        # Send the house dict through Kafka
        # TODO Start Kafka Producer 
        

    # Setup the same url again 
    driver.get(url)
    # Get next page
    next_page_url = driver.find_element(By.CLASS_NAME, 'list-pagination-next').get_attribute('href')
    print(next_page_url)
    spider_specific_house_locations(driver, next_page_url, house_location_list, current_page+1)



def testing_webcrawling():
    # url = 'https://www.idealista.pt/imovel/31687430'
    # step 1: web crawl supercasa.pt website
    # step 2: get all the links that are related to real state
    # step 3: extract relevant information
    base_url = 'https://supercasa.pt/comprar-casas/aveiro-distrito'

    config = load_config('supercasa')

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(base_url)
    
    # JDCookieNotifier_element = driver.find_element(By.XPATH, '//*[@id="JDCookieNotifier"]')

    # print(JDCookieNotifier_element)
    visited_paths = []

    # ! ############################################################################################################
    # ! Problem: Takes an extremely large amount of time to crawl the entire website and to find out the pages with 
    # ! the relevant information
    # !
    # ! spider_entire_website(driver, base_url, "//a[@href]", config['ignored_paths'], visited_paths)
    # ! ############################################################################################################
    
    spider_specific_house_locations(driver, base_url, config['house_location_list'], 1)

    driver.quit()

