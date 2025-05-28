def compare_layouts(figma_layouts, dom_layouts, tolerance=5):
    mismatches = []
    for name in figma_layouts:
        if name not in dom_layouts:
            mismatches.append(f"Missing DOM element for '{name}'")
            continue

        fig_box = figma_layouts[name]['boundingBox']
        dom_box = dom_layouts[name]['boundingBox']

        for key in ['x', 'y', 'width', 'height']:
            if abs(fig_box.get(key, 0) - dom_box.get(key, 0)) > tolerance:
                mismatches.append(f"'{name}' differs in {key}: Figma={fig_box[key]}, DOM={dom_box[key]}")
    return mismatches
