from selenium import webdriver

from pages.quotes_page import  QuotePage

chrome = webdriver.Chrome(executable_path="c:/projects/chromedriver.exe")
chrome.get('http://quotes.toscrape.com')
#page_content = requests.get('http://quotes.toscrape.com').content
page = QuotePage(chrome)

for quote in page.quotes:
    print(quote.content)

