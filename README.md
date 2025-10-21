
# SpencerTool

<details>
<summary>⚠️ Important Safety & Legal Notice</summary>

This tool contains operations that can terminate processes, remove browser extensions, delete directories, and create many files quickly. Running it with administrative privileges or on systems you do not own can cause data loss, break software, or violate laws/policies. **Do not run this on systems you do not control.** Use at your own risk.

</details>

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options Explained](#menu-options-explained)
- [Examples](#examples)
- [Limitations & Known Issues](#limitations--known-issues)
- [Security & Responsible Use](#security--responsible-use)
- [Contributing](#contributing)
- [License](#license)
- [Changelog](#changelog)

---

## Features

<details>
<summary>Click to expand features</summary>

- Simple textual menu for executing Windows commands.
- Quickly kill processes (e.g. `msedge.exe`, arbitrary `.exe`).
- Remove Microsoft Edge extension folders by ID or a built-in `WebBlock` path.
- Show running tasks via `tasklist`.
- A small terminal-like mini-shell that runs commands in the current working directory.
- A file spammer utility (creates many `.txt` files with sample content).

</details>

## Requirements

- **Windows** (script uses `taskkill`, `tasklist`, and Windows user folder paths).
- Python 3.8+ recommended.
- Permissions: some operations will require Administrator privileges (e.g. killing system processes, removing files inside protected folders).

## Installation

```powershell
# Clone or download the repo
python spencertool.py
````

## Usage

Run the script, then type the number (or letter) corresponding to the desired action and press Enter.

## Menu Options Explained

<details>
<summary>Click to expand menu options</summary>

* `[001] Links` - Prints a list of helpful links.
* `[002] Close MSEdge` - Terminates Microsoft Edge.
* `[003] Kill smartscreen` - Terminates the Windows SmartScreen process.
* `[004] Show tasks` - Lists currently running processes.
* `[005] Stop WebBlock` - Removes a hard-coded Edge extension directory.
* `[006] Delete an extension` - Prompts for an extension ID and removes its directory.
* `[007] File Spammer` - Repeatedly creates files in a chosen directory.
* `[008] Proxies` - Placeholder, currently unused.
* `[009] Quit process` - Terminates a user-specified process.
* `[A] Start Process` - Placeholder, currently unused.
* `[B] Terminal` - Mini terminal for running commands in the current working directory.

</details>

## Examples

<details>
<summary>Click to expand examples</summary>

* Kill Microsoft Edge:

  ```
  1. Run the script
  2. Type `2` and press Enter
  ```

* Delete an Edge extension by ID:

  ```
  1. Run the script
  2. Type `6` and press Enter
  3. Input the extension ID
  ```

* Create spam files in `C:\Temp` with prefix `spam`:

  ```
  1. Run the script
  2. Type `7` and press Enter
  3. Enter `spam` for the file name and `C:\Temp` for the directory
  ```

</details>

## Limitations & Known Issues

* Infinite loops may cause the script to hang if deletion fails.
* Minimal exception handling around filesystem operations.
* Windows-only paths and `os.getlogin()` assumptions.
* Some menu placeholders (`A`, `8`) are non-functional.

## Security & Responsible Use

* Tool can be destructive. Use on systems you control.
* Suggested improvements: confirmation prompts, dry-run mode, limits for loops, logging.

## Contributing

1. Fork the repo
2. Make changes on a feature branch
3. Submit a PR with a clear description

## License

No explicit license header in the source. Treat as unlicensed by default.

## Authors

* T.G (sgtflixy)
* S.H (TERRATOME)

## Changelog

* Initial README generated from the current source
