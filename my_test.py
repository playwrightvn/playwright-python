from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False)
  
  page = browser.new_page()
  
  page.goto('https://material.playwrightvn.com/01-xpath-register-page.html')
  
  page.wait_for_timeout(10_000)