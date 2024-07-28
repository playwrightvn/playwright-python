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
male_rb = page.locator("//input[@id='male']")
male_rb.check()

print(male_rb.is_checked())

reading_cb = page.locator('//input[@id="reading"]')
reading_cb.check()
reading_cb.set_checked(False)

# select option
country_select = page.locator('//select[@id="country"]')
country_select.select_option("Canada")

# input: set_input_files
profile_file = page.locator("//input[@id='profile']")
profile_file.set_input_files('/Users/apple/Documents.nosync/pw-python/02-pw-python/my_test.py')