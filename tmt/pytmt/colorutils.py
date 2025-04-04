from .data import htmlcolors



def is_valid_hex_color(s: str) -> bool:
	if s.startswith("#"):
		s = s[1:]  # Remove the '#' if it exists

	if len(s) not in (3, 6):  # Hex colors should be 3 or 6 characters long
		return False

	try:
		int(s, 16)  # Try converting to an integer base 16
		return True
	except ValueError:
		return False



def get_hex_color(arg: str) -> bool:
	if arg[0] == '#' and len(arg) in [4, 7] and is_valid_hex_color(arg):
		return arg

	if arg[0] != '#' and len(arg) in [3, 6] and is_valid_hex_color(arg):
		return f"#{arg}"

	for color in htmlcolors:
		if color['name'].lower() == arg.lower():
			return color['code']

	return None


