import pytest

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

@pytest.fixture
def browser(request):
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()