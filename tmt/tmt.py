#!/usr/bin/env python3
import argparse
import subprocess
import sys

from pytmt.data import background_classes, foreground_classes
from pytmt.printutils import *
from pytmt.colorutils import get_hex_color



be_verbose = False
def verbose(*args, **kwargs):
	if be_verbose:
		print(*args, **kwargs)


def get_default_profile():
	"""Retrieve the default GNOME Terminal profile ID."""
	try:
		profile_id = subprocess.check_output(
			["gsettings", "get", "org.gnome.Terminal.ProfilesList", "default"],
			universal_newlines=True
		).strip().strip("'")
		return profile_id
	except subprocess.CalledProcessError:
		print("Error: Could not retrieve GNOME Terminal profile ID.")
		sys.exit(1)

def set_terminal_setting(setting, value, profile_id):
	profile = f"org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:{profile_id}/"
	command = [
		"gsettings", "set", profile,
		setting, str(value)
	]
	"""Apply GNOME Terminal settings using gsettings."""
	verbose(f"$ {green(' '.join(command))}")
	subprocess.run(command)


def main():
	parser = argparse.ArgumentParser(description="Modify GNOME Terminal settings.")
	parser.add_argument("-c", "--css", help="set background / foreground via Tailwind CSS bg-* and text-* class")
	parser.add_argument("-b", "--background", help="set terminal background color (e.g., '#000000')")
	parser.add_argument("-f", "--foreground", help="set terminal foreground color (e.g., '#ffffff')")
	parser.add_argument("-t", "--transparency", type=int, choices=range(0, 101, 5),
		help="set terminal transparency (0-100, 0 = opaque, 100 = fully transparent)")
	parser.add_argument("-z", "--fontsize", type=int, help="set terminal font size")
	parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
	args = parser.parse_args()

	profile_id = get_default_profile()
	global be_verbose
	be_verbose = args.verbose

	if args.background:
		color = get_hex_color(args.background)
		if color:
			set_terminal_setting("background-color", f"'{color}'", profile_id)
			print(f"Background color set to {color}")
		else:
			print(f"Invalid color: '{args.background}'")

	if args.foreground:
		color = get_hex_color(args.foreground)
		if color:
			set_terminal_setting("foreground-color", f"'{color}'", profile_id)
			print(f"Foreground color set to {color}")
		else:
			print(f"Invalid color: '{args.foreground}'")

	if args.css:
		if args.css in background_classes:
			color = background_classes[args.css]
			set_terminal_setting("background-color", f"'{color}'", profile_id)
			print(f"Background color set to '{color}'")
		elif args.css in foreground_classes:
			color = foreground_classes[args.css]
			set_terminal_setting("foreground-color", f"'{color}'", profile_id)
			print(f"Foreground color set to '{color}'")
		else:
			print(f"CSS class not found: '{args.css}'")

	if args.transparency is not None:
		set_terminal_setting("use-transparent-background", "true", profile_id)
		set_terminal_setting("background-transparency-percent", args.transparency, profile_id)
		print(f"Transparency set to {args.transparency}%")

	if args.fontsize:
		font_setting = f"Monospace {args.fontsize}"
		subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "monospace-font-name", font_setting])
		print(f"Font size set to {args.fontsize}")


if __name__ == "__main__":
	main()
