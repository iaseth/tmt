
# tmt

`tmt` is a Python script designed to modify GNOME Terminal settings directly from the command line. It allows users to customize aspects such as background and foreground colors, transparency levels, and font sizes, enhancing the terminal's visual appearance and usability.

## Features

- **Set Background Color**: Change the terminal's background to any specified hex color.
- **Set Foreground Color**: Adjust the text color using a desired hex value.
- **Adjust Transparency**: Modify the terminal's transparency level within a range of 0% (opaque) to 100% (fully transparent).
- **Change Font Size**: Update the terminal's font size to improve readability.

## Prerequisites

- **GNOME Terminal**: Ensure that GNOME Terminal is installed on your system.
- **Python 3**: The script requires Python 3 to execute.
- **gsettings**: This utility should be available for the script to interact with GNOME settings.

## Installation

Just run the following in your terminal and you are good to go.
This just fetches the `tmt` (zipped executable release) from the repo,
and adds it to your `PATH`.

```bash
wget https://raw.githubusercontent.com/iaseth/tmt/refs/heads/master/build/tmt && chmod +x tmt && cp tmt ~/.local/bin
```

## Usage

Run the script with the desired options to customize your GNOME Terminal settings:

```bash
tmt [options]
```

### Options

- `-b`, `--background`: Set the terminal background color. Accepts a hex color code (e.g., `#000000` or `000000`).
- `-f`, `--foreground`: Set the terminal foreground (text) color. Accepts a hex color code (e.g., `#ffffff` or `ffffff`).
- `-t`, `--transparency`: Set the terminal transparency level. Accepts an integer between 0 and 100, where 0 is fully opaque and 100 is fully transparent.
- `-z`, `--fontsize`: Set the terminal font size. Accepts an integer representing the desired font size.
- `-v`, `--verbose`: Enable verbose output to display detailed information about the changes being applied.

### Examples

- **Change Background and Foreground Colors**:
  Set the background color to a dark shade (`#1d1f21`) and the foreground (text) color to a light grey (`#c5c8c6`):
  ```bash
  tmt -b 1d1f21 -f c5c8c6
  ```

  Set the background and the foreground color using Tailwind classes:
  ```bash
  tmt --css bg-zinc-900 text-zinc-50
  ```

  Set the background and the foreground color using themes:
  ```bash
  tmt --theme Monokai
  ```
  Run `tmt --theme` without arguments to list all themes.

- **Adjust Transparency**:
  Set the terminal transparency to 20%, making it slightly transparent:
  ```bash
  tmt -t 20
  ```

  Turn off Transparency:
  ```bash
  tmt --opaque
  ```

  Turn on Transparency:
  ```bash
  tmt --transparent
  ```

- **Change Font Size**:
  ```bash
  tmt -z 12 -v
  ```
  Sets the font size to 12.

- **Print current Profile Settings**:
  ```bash
  tmt --print
  ```

## Build it Yourself

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iaseth/tmt.git
   ```
2. **Navigate to the Directory**:
   ```bash
   cd tmt
   ```
3. **Run the script**:
   ```bash
   python3 tmtpy -p
   ```

## Notes

- The script retrieves the default GNOME Terminal profile ID to apply the settings.
- Invalid color codes or unsupported values will result in error messages without applying changes.
- Transparency adjustments require the terminal to support background transparency.

## License

This project is licensed under the MIT License. 
