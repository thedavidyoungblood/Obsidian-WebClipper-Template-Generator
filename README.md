# Obsidian WebClipper Template Generator

The **Obsidian WebClipper Template Generator** is a single-script tool that automates the creation of JSON template files for the Obsidian WebClipper Chrome extension. With a simple prompt for a VAULT-ROOT-PATH, it recursively creates the required directory structure and populates it with JSON templates for various clipping scenarios. Additionally, it generates a `README_IMPORT_GUIDANCE.txt` file containing step-by-step instructions for importing these templates into Obsidian WebClipper.

## Features

- **Automated Directory & File Generation**  
  Creates a structured set of subdirectories and JSON files:
  - `Clippings/` &mdash; Contains the core template.
  - `Clippings/Summaries/` &mdash; For summary templates.
  - `Clippings/Research/` &mdash; For research & AI insights templates.
  - `Clippings/Translations/` &mdash; For translation templates.
  - `Clippings/Articles/` &mdash; For news/blog article templates.
  - `Clippings/Highlights/` &mdash; For highlights-only templates.
  - `Clippings/GitHub/` &mdash; For GitHub page templates.
  - `Clippings/Medium/` &mdash; For Medium article templates.
  - `Clippings/Generic/` &mdash; For the generic fallback template.
  
- **Guided Import Process**  
  Automatically generates a `README_IMPORT_GUIDANCE.txt` in your vault root to help you import the JSON templates into Obsidian WebClipper.

- **Minimal Dependencies**  
  Requires only Python 3.7 or higher; uses only the standard library.

---

## Installation

Ensure you have **Python 3.7** or higher installed.

(Optional) Set up a virtual environment to isolate dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

---

## Usage

Run the script from your terminal or command prompt:

```bash
python generate_templates.py
```

When prompted, enter the full **VAULT-ROOT-PATH** where you want the templates and guidance file to be generated. The script will:

1. Create the necessary subdirectories.
2. Write each JSON template into its designated folder.
3. Generate a `README_IMPORT_GUIDANCE.txt` with detailed import instructions for Obsidian WebClipper.

After execution, navigate to your specified vault root to verify that the templates and documentation have been created.

---

## Repository Structure

```
.
├── generate_templates.py
└── README.md
```

After running the script, the target vault root will have a structure similar to:

```
vault-root/
├── Clippings/
│   ├── Custom_Default_Verbatim_Clone_Clean.json
│   ├── Summaries/
│   │   └── Custom_Summary.json
│   ├── Research/
│   │   ├── Custom_Research_AI_Insights.json
│   │   └── Research_Academic.json
│   ├── Translations/
│   │   └── Custom_Translation.json
│   ├── Articles/
│   │   ├── Custom_News_Blog_Article.json
│   │   └── Article_Blog.json
│   ├── Highlights/
│   │   └── Custom_Highlights_Only.json
│   ├── GitHub/
│   │   └── GitHub_Page.json
│   ├── Medium/
│   │   └── Medium_Article.json
│   └── Generic/
│       └── Generic_Web_Clip.json
└── README_IMPORT_GUIDANCE.txt
```

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 David Youngblood

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact

- **Email:** [opensource@louminai.com](mailto:opensource@louminai.com)
- **Website:** [louminai.com](http://louminai.com)
- **GitHub:** [thedavidyoungblood/Obsidian-WebClipper-Template-Generator](https://github.com/thedavidyoungblood/Obsidian-WebClipper-Template-Generator)

---

## Acknowledgements

Special thanks to the team at `OBSIDIAN`, AI(ChatGPT), and the open source community for their support and inspiration.

---

*Happy Clipping!*
