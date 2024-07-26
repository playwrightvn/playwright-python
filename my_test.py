from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False)
  
  page = browser.new_page()
  
  page.goto('https://material.playwrightvn.com')
  
  page.wait_for_timeout(10_000)