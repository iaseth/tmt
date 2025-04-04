import json
import os



def get_json(json_path):
	if os.path.isfile(json_path):
		with open(json_path) as f:
			jo = json.load(f)
		return jo
	else:
		return None


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


