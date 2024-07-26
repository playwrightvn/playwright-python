from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)

page = browser.new_page()

page.goto('https://material.playwrightvn.com/01-xpath-register-page.html')


# Locator
# Xpath
username_loc = page.locator('//input[@id="username"]')
username_loc.highlight()

# CSS 
email_loc = page.locator('//input[@id="email"]')
email_loc.highlight()

# Playwright locator
register_loc = page.get_by_role("button", name="Register")
register_loc.highlight()

# Action

# click
page.goto('https://material.playwrightvn.com/018-mouse.html')
click_area = page.locator('//input[@id="clickArea"]')
click_area.click()
click_area.dblclick()
click_area.click(modifiers=[])