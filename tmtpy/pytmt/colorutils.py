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


def hex_to_rgb(hex_color):
	hex_color = hex_color.lstrip("#")
	return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def print_colored(message, foreground="#FFFFFF", background="#000000"):
	fg = hex_to_rgb(foreground)
	bg = hex_to_rgb(background)

	ansi_code = (
		f"\033[38;2;{fg[0]};{fg[1]};{fg[2]}m"
		f"\033[48;2;{bg[0]};{bg[1]};{bg[2]}m"
	)

	reset = "\033[0m"
	print(f"{ansi_code}{message}{reset}")


