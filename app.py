from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)

    # Create a new page
    page = browser.new_page()

    # Visit the playwright website
    page.goto("https://playwright.dev")

    page.get_by_role('link', name="Docs").click()

    page.wait_for_timeout(10_000)
