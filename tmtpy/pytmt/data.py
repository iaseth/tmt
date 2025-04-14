from .utils import get_json



htmlcolors_json = get_json('data/htmlcolors.json')
htmlcolors = htmlcolors_json['colors'] if htmlcolors_json else []


tailwindcolors_json = get_json('data/tailwindcolors.json')
tailwindcolors = tailwindcolors_json['colors'] if tailwindcolors_json else []
background_classes = {}
foreground_classes = {}
for palette in tailwindcolors:
	name = palette['name']
	for shade in palette['shades']:
		bg_class_name = f"bg-{name}-{shade['shade']}"
		fg_class_name = f"text-{name}-{shade['shade']}"
		background_classes[bg_class_name] = shade['hex']
		foreground_classes[fg_class_name] = shade['hex']

themes = get_json('data/themes.json')
