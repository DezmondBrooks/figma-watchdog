from playwright.sync_api import sync_playwright

def get_element_layouts(url, selectors):
    layout_data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        for name, selector in selectors.items():
            el = page.query_selector(selector)
            if el:
                box = el.bounding_box()
                text = el.inner_text()
                layout_data[name] = {"boundingBox": box, "text": text}

        browser.close()
    return layout_data
