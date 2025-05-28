import os
import json
from figma_watchdog import figma_api, dom_extractor, matcher, report

def main():
    # Config
    FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")
    FILE_ID = os.getenv("FIGMA_FILE_ID")
    FRAME_NAME = "Home Page"
    URL = "https://your-production-site.com"
    SELECTOR_MAP_PATH = "config/mapping.json"

    # Load selector mappings
    with open(SELECTOR_MAP_PATH) as f:
        selector_map = json.load(f)

    # Figma
    figma = figma_api.FigmaClient(FIGMA_TOKEN, FILE_ID)
    figma_layout = figma.extract_layout_data(FRAME_NAME)

    # DOM
    dom_layout = dom_extractor.get_element_layouts(URL, selector_map)

    # Compare
    mismatches = matcher.compare_layouts(figma_layout, dom_layout)
    report.print_report(mismatches)

    # Optional: exit 1 on fail
    if mismatches:
        exit(1)

if __name__ == "__main__":
    main()
