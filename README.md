# Learning logs

## Day 1
```bash
python -m venv venv
pip install playwright
playwright --version
```

- Cài đặt browser
```bash
playwright install
```

- Mở browser và click

```python
browser = playwright.chromium.launch(headless=False)

# Create a new page
page = browser.new_page()

# Visit the playwright website
page.goto("https://playwright.dev")

page.get_by_role('link', name="Docs").click()

page.wait_for_timeout(10_000)
```

- Run code:

```bash
python app.py
```

## Day 2: Locators
- Có thể chạy python ở interactive mode
    - Mở terminal lên
    - Active `. venv/bin/activate`
    - Gõ lệnh: `python`
    - Từ đây có thể gõ từng câu lệnh cho chạy.
- Nếu dùng button, có thể dùng lệnh `.highlight()`
- Kết thúc, dùng lệnh: `browser.close()`, `playwright.stop()`