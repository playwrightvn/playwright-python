from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

# selectors
page.goto('https://material.playwrightvn.com/01-xpath-register-page.html')

# by xpath
username_loc = page.locator('//input[@id="username"]')
username_loc.highlight()

# by css selector
email_loc = page.locator('#email')
email_loc.highlight()

# by playwright selector
submit_btn = page.get_by_role('button', name="Register")
submit_btn.highlight()

# mouse actions: click, dbclick, click w modifier
page.goto('https://material.playwrightvn.com/018-mouse.html')
click_area = page.locator('#clickArea')
click_area.highlight()
click_area.click()
click_area.dblclick()
click_area.click(modifiers=['Shift'])

# input action: fill, clear, type
page.goto('https://material.playwrightvn.com/01-xpath-register-page.html')
username_loc = page.locator('//input[@id="username"]')
username_loc.highlight()

username_loc.fill('Playwright Viet Nam')
username_loc.clear()
username_loc.type('Playwright Viet Nam', delay=2000)

# checkbox action: check, uncheck, setchecked, click()


# select option

# input: set_input_files