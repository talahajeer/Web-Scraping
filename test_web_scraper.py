from web_scraper import __version__
from web_scraper.web_scraper import *


def test_version():
    assert __version__ == '0.1.0'


def test_get_citations_needed_count():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual=get_citations_needed_count(URL)
    # print(actual)
    excepted='Number of citation 5'
    assert actual==excepted



def test_get_citations_needed_report():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual=len(get_citations_needed_report(URL))
    # print(actual)
    excepted= 4
    assert actual ==excepted

def test_get_citations_needed_report1():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    array=get_citations_needed_report(URL)
    actual = array[0]
    # print(actual)
    excepted= 'The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][6] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.'
    assert actual ==excepted


# cooperation with Noor . Manar




