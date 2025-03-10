from selenium import webdriver
# from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options

from app.application import Application

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)


    ### SAFARI ###
    # context.driver = webdriver.Safari()

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='put your path to driver file here')
    # context.driver = webdriver.Firefox(service=service)

    ## HEADLESS MODE FOR Chrome####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
    ## HEADLESS MODE FOR FIREFOX####
    # options = Options()
    # options.add_argument('--headless')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(service=service, options=options)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'oleksiihalaktion_xqs9Ku'
    bs_key = 'rqsmdpydZ9zzXe9JvfKQ'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os" : "OS X",  # Windows / OS X /
        "osVersion" : "Big Sur",    # 11 / 10 - For Windows. Sequoia / Ventura ... / - for OS X(Mac)
        'browserName': 'Firefox',
        'sessionName': scenario_name,
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
