# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from kanary_project.models.demographics import Person


def scrape_person(person: Person, url="https://golookup.com/") -> str:
    """
    Searches for a person by name and location on the website given by the url. If at least one person is found,
    information on those people is returned. If a person is not found or if the search fails, a descriptive message with
    this information is returned.

    Parameters
    __________
    person : Person
        The person being searched represented as a Pydantic object.
    website : Website
        The website where the person is being searched represented as a Pydantic object.

    Returns
    ______
    str
        The results if at least one person meeting the parameters described above is found.
        The string "No results found." if a person meeting the parameters described above is not found.
        The string "Error executing search." if neither of the above conditions was met.
    """

    # launch Firefox browser via selenium in headless mode
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)

    # find form fields that need to be filled
    first = browser.find_element(By.NAME, "firstName")
    last = browser.find_element(By.NAME, "lastName")
    state = browser.find_element(By.NAME, "state")

    # fill out form
    first.send_keys(person.first_name.name)
    last.send_keys(person.last_name.name)
    state.send_keys(person.location.state)

    # submit form
    # find search button
    search = browser.find_element(By.CLASS_NAME, "frm-submit")
    # click button
    search.click()

    # wait for page to load
    time.sleep(45)

    # parse web page and save sensible response
    results = browser.find_element(By.XPATH, "/html/body").text
    if "No records found" in results:
        result = "No results found."
    elif "SUCCESS: Select the Results below, that Best Fit your Search!" in results:
        result = browser.find_element(By.ID, "results").text
    else:
        result = "Error executing search."

    # quit Firefox browser
    browser.quit()

    return result
