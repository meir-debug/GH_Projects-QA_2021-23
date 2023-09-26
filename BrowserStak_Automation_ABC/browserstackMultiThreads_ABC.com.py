from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from threading import Thread
from SeleniumWebdriverPython_test.BrowserStack import my_key

caps = [{
    'os_version': '10',
    'os': 'Windows',
    'browser': 'chrome',
    'browser_version': 'latest',
    'name': 'Parallel Test1_Win10_Chrome',  # test name
    'build': 'BStack-[Python] Sample Build'  # Your tests will be organized within this build
},
    {
        'os_version': '10',
        'os': 'Windows',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test2_Win10_Firefox',  # test name
        'build': 'BStack-[Python] Sample Build'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'chrome',
        'browser_version': 'latest',
        'name': 'Parallel Test3_OSX_Chrome',  # test name
        'build': 'BStack-[Python] Sample Build'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'Firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test4_OSX_Firefox',  # test name
        'build': 'BStack-[Python] Sample Build'
    }]


def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor=my_key.key,  # you need to use your own key here
        desired_capabilities=desired_cap)

    driver.get("https://google.com")
    driver.maximize_window()

    # driver.find_element_by_name("q").send_keys("abc")
    driver.find_element(By.NAME, "q").send_keys("abc")

    print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))  # Google logo image
    print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
    print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

    time.sleep(2)
    driver.find_element(By.NAME, "btnK").click()
    time.sleep(2)
    driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
    time.sleep(2)
    assert "ABC Home Page - ABC.com" in driver.title
    print(driver.title)

    time.sleep(10)
    driver.find_element(By.XPATH, "//span[@class='Searchlist__icon__search']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='search for a show']").send_keys("Dancing")
    driver.implicitly_wait(10)
    # Find el Dancing
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Dancing with the Stars').click()
    time.sleep(2)
    assert "Watch Dancing with the Stars TV Show - ABC.com" in driver.title
    print(driver.find_element(By.XPATH, "//img[@class='Header__Logo__img']").get_attribute("title"))

    # quit from browser
    driver.quit()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run
# each session in parallel
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()
