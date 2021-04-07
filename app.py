from selenium import webdriver

from pages.quotes_page import  QuotePage

chrome = webdriver.Chrome(executable_path="c:/projects/chromedriver.exe")
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotePage(chrome)

author = input("Enter the author you'd like quotes from: ")
page.select_author(author)

