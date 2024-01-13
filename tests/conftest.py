import pytest 
from rymscraper import scraper

@pytest.fixture(autouse=True, scope='session')
def rymscraper():
    s = scraper.Scraper()
    yield s
    s.driver.quit()