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

## Day 3: Events
- Auto waiting là một tính năng rất mạnh của Playwright.
- Ví dụ với auto wait element:
    - visible
    - enable
    - stable
- Page navigation
```python
page.goto('', wait_util='loaded')
```
- Load & domcontentloaded
    - Load: gồm cả image load xong
    - domcontentloađe: không gồm image load xong.
    - commit: chỉ cần server trả về là xong.
    - networkidle: = network in & network out stop.
- Custom waiting:
    - element.wait_for
- Event listener
    - page.on('event_name')
        - example w: page load, request, file_chooser
- Dialog
    - alert
    - prompt
    - confirmation
- Download: 2 cách
    - page.on
    ```python
    def on_download(download):
        download.save_as("abc.png")

    page.on("download", on_download)
    ```
    - handle as object
    ```python
    with page.expect_download() as download_info:
        btn.click()
    download = download_info.value
    download.save_as('abc.png')
    ```
    - page.once
- Sync và async

