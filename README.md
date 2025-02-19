# Obsidian WebClipper Template Generator

The **Obsidian WebClipper Template Generator** is a Python utility that automates the creation of JSON template files for the Obsidian WebClipper Chrome extension. In addition to generating the necessary folder structure and templates for various clipping scenarios, it also produces a comprehensive `README_IMPORT_GUIDANCE.txt` to help you seamlessly import and manage your templates.

Whether you’re new to the Obsidian ecosystem or looking to customize your clipping workflow, this tool and the curated resources below will get you up and running quickly.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Repository Structure](#repository-structure)
5. [Obsidian WebClipper Settings & Configuration](#obsidian-webclipper-settings--configuration)
6. [User Guidance & Resources](#user-guidance--resources)
    - [Guides on Creating & Managing Templates](#guides-on-creating--managing-templates)
    - [Video Tutorials](#video-tutorials)
    - [Template Repositories](#template-repositories)
    - [Key Template Management Features](#key-template-management-features)
7. [Additional Resources](#additional-resources)
    - [Official Documentation & Installation Sources](#official-documentation--installation-sources)
    - [Guides and Tutorials](#guides-and-tutorials)
    - [Community Resources](#community-resources)
    - [Developer Resources](#developer-resources)
    - [Additional Information](#additional-information)
8. [Obsidian WebClipper Templates](#obsidian-webclipper-templates)
9. [License](#license)
10. [Contact](#contact)
11. [Acknowledgements](#acknowledgements)

---

## Features

- **Automated Directory & File Generation**  
  Creates a structured set of subdirectories and JSON files for various clipping scenarios:
  - `Clippings/` &mdash; Core template.
  - `Clippings/Summaries/` &mdash; For summary templates.
  - `Clippings/Research/` &mdash; For research & AI insights templates.
  - `Clippings/Translations/` &mdash; For translation templates.
  - `Clippings/Articles/` &mdash; For news/blog article templates.
  - `Clippings/Highlights/` &mdash; For highlights-only templates.
  - `Clippings/GitHub/` &mdash; For GitHub page templates.
  - `Clippings/Medium/` &mdash; For Medium article templates.
  - `Clippings/Generic/` &mdash; For fallback generic templates.

- **Guided Import Process**  
  Automatically generates a `README_IMPORT_GUIDANCE.txt` with step-by-step instructions for importing your templates into Obsidian WebClipper.

- **Minimal Dependencies**  
  Requires only Python 3.7 or higher and uses only the standard library.

- **Comprehensive User Guidance**  
  Leverages curated resources—from detailed guides and video tutorials to community repositories—to help you master custom template creation and management.

---

## Installation

1. **Ensure Python 3.7+ is installed.**

2. *(Optional)* Set up a virtual environment to isolate dependencies:

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # Windows: .venv\Scripts\activate
    ```

3. **Clone this repository and navigate into it:**

    ```bash
    git clone https://github.com/thedavidyoungblood/Obsidian-WebClipper-Template-Generator.git
    cd Obsidian-WebClipper-Template-Generator
    ```

---

## Usage

Run the script from your terminal:

```bash
python generate_templates.py
```

When prompted, enter the full **VAULT-ROOT-PATH** where you want the templates and guidance file to be generated. The script will:

1. Create the required subdirectories.
2. Populate each folder with its designated JSON template.
3. Generate `README_IMPORT_GUIDANCE.txt` with detailed instructions for importing the templates into Obsidian WebClipper.

After execution, navigate to your specified vault root to review the created structure and guidance documentation.

---

## Repository Structure

```
.
├── generate_templates.py
└── README.md
```

After running the script, your vault root will have a structure similar to:

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

## Obsidian WebClipper Settings & Configuration

For advanced configuration of your Obsidian WebClipper extension, use the following settings URLs based on your installation type:

### Native Extension Settings
If you have installed the native extension, access its settings directly by entering this URL into your browser’s address bar:

```plaintext
chrome-extension://cnjifjpddelmedmihgijeibhnjfabmlf/settings.html?section=general
```

This page allows you to adjust general settings—such as template import options and clipping behavior—to tailor the extension to your workflow.

### Browser-Specific Configurations (Chromium-Based)
For users running a Chromium-based browser (e.g., Chrome, Brave, Arc, etc.), manage the extension’s configuration through your browser’s built-in extensions page. Replace `{browser}` in the URL below with your browser’s protocol:

```plaintext
{browser}://extensions/?id=cnjifjpddelmedmihgijeibhnjfabmlf
```

For example, in Chrome, use:

```plaintext
chrome://extensions/?id=cnjifjpddelmedmihgijeibhnjfabmlf
```

This interface enables you to enable/disable the extension, review permissions, and perform any browser-specific configuration.

---

## User Guidance & Resources

This section is designed to help you explore advanced template management techniques and get the most out of Obsidian WebClipper.

### Guides on Creating & Managing Templates

- **Step-by-Step Guide to Custom Templates**  
  Learn how to create custom templates, define unique names, and specify behaviors like creating new notes or appending to existing ones.  
  [Sascha D. Kasper's Guide](https://sascha-kasper.com/step-by-step-guide-to-the-obsidian-web-clipper/)

- **Effective Web Clipping with Custom Templates**  
  Detailed instructions for tailoring templates to specific web pages (e.g., PubMed articles) using metadata fields like `PMID`.  
  [Kristian Freeman's Guide](https://kristianfreeman.com/custom-obsidian-clippings)

- **Obsidian Help Documentation**  
  Official documentation on creating, editing, importing, and exporting templates—including advanced features like URL-based triggers.  
  [Obsidian Help](https://help.obsidian.md/web-clipper/templates)

### Video Tutorials

- **YouTube Walkthrough on Custom Templates**  
  A comprehensive video guide covering default templates, custom template creation, and advanced trigger features.  
  [Watch on YouTube](https://www.youtube.com/watch?v=oEtSLrfEj5o)

- **Custom Template Setup and Triggers**  
  Explains how to configure templates with properties, variables, and triggers for automating content capture.  
  [Watch on YouTube](https://www.youtube.com/watch?v=Kesi8sp2x7M)

### Template Repositories

- **Community Template Collections**  
  Access pre-defined templates created by the Obsidian community for clipping highlights, saving metadata, and organizing research notes.

- **Clipper-Templates Repository**  
  A dedicated GitHub repository featuring example templates for various clipping scenarios with instructions for import/export.  
  [Clipper-Templates Repo](https://github.com/kepano/clipper-templates)

### Key Template Management Features

- **Importing/Exporting Templates**  
  Easily import JSON files or export your custom templates for backup or sharing.
  
- **Template Triggers**  
  Automate template selection based on URL patterns or metadata.
  
- **Variables and Properties**  
  Utilize variables (e.g., `title`, `URL`, `date`) to dynamically populate note content during clipping.

---

## Additional Resources

For a deeper dive into the Obsidian WebClipper ecosystem, explore these curated resources:

### Official Documentation & Installation Sources

- **Obsidian WebClipper GitHub Repository**  
  Official instructions, developer resources, and feature roadmaps.  
  [obsidianmd/obsidian-clipper](https://github.com/obsidianmd/obsidian-clipper)

- **Obsidian Help Site**  
  Detailed documentation on using the WebClipper including highlighting, filters, and troubleshooting.  
  [Obsidian Help](https://help.obsidian.md/web-clipper)

- **Browser Extension Stores**  
  Install the extension directly from:
  - [Chrome: Chrome Web Store](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf)
  - [Firefox: Firefox Add-ons](https://addons.mozilla.org/en-US/firefox/addon/web-clipper-obsidian/)
  - [Safari: Obsidian WebClipper on Safari Extensions](https://obsidian.md/clipper)
  - [Edge: Microsoft Edge Add-ons](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf)

### Guides and Tutorials

- **Step-by-Step Guide by Sascha D. Kasper**  
  Comprehensive instructions covering installation, configuration, and usage.  
  [Step-by-Step Guide](https://sascha-kasper.com/step-by-step-guide-to-the-obsidian-web-clipper/)

- **YouTube Tutorial**  
  A video guide for setting up and using the Obsidian WebClipper effectively, including mobile support.  
  [Watch on YouTube](https://www.youtube.com/watch?v=icsQeiqDa34)

- **Supercharge Your Workflow Blog Post**  
  Insights on capturing content efficiently using templates, highlighters, and filters.  
  [Read the Blog Post](https://www.dsebastien.net/supercharge-your-knowledge-capture-workflow-with-the-obsidian-web-clipper/)

### Community Resources

- **Reddit Discussions**  
  User experiences and tips on using the Obsidian WebClipper.  
  [Reddit Thread](https://www.reddit.com/r/ObsidianMD/comments/1hatxd1/my_obsidian_web_clipper/)

- **Obsidian Forum Threads**  
  Troubleshooting, alternative clippers, and community support:
  - [Troubleshooting Thread](https://forum.obsidian.md/t/obsidian-web-clipper-add-to-obsidian-not-working/91124)
  - [Reliable Web Clippers Discussion](https://forum.obsidian.md/t/reliable-web-clipper-for-daily-notes-with-emphasis-on-reliable/36944)

### Developer Resources

- **Developer Setup Instructions**  
  Build the extension locally with Node.js and npm.  
  [obsidianmd/obsidian-clipper](https://github.com/obsidianmd/obsidian-clipper) | [mvavassori/obsidian-web-clipper](https://github.com/mvavassori/obsidian-web-clipper)

- **Feature Roadmap**  
  Planned enhancements include template validation, local image saving, markdown previews, and more.

### Additional Information

- **Obsidian Blog Announcement**  
  Learn about the WebClipper’s features and its impact on note-taking workflows.  
  [Read the Blog Post](https://obsidian.md/blog/save-the-web/)

- **App Store Reviews**  
  See what users are saying about customization and performance.  
  [Apple App Store – Obsidian WebClipper](https://apps.apple.com/us/app/obsidian-web-clipper/id6720708363)

---

## Obsidian WebClipper Templates [OFFICIAL]

Templates for [Obsidian Web Clipper](https://github.com/obsidianmd/obsidian-clipper) work seamlessly with the templates in [my Obsidian vault](https://github.com/kepano/kepano-obsidian).  
To install templates, see the instructions in the official [Obsidian Web Clipper documentation](https://help.obsidian.md/web-clipper/templates).

### Templates

Generic and schema-based templates:

- [Recipes](https://github.com/kepano/clipper-templates/blob/main/templates/recipes-clipper.json)
- [Product](https://github.com/kepano/clipper-templates/blob/main/templates/product-clipper.json) — e.g. Shopify

Specific Websites:

- [Arxiv](https://github.com/kepano/clipper-templates/blob/main/templates/arxiv-clipper.json)
- [Goodreads](https://github.com/kepano/clipper-templates/blob/main/templates/goodreads-clipper.json)
- [Google Maps](https://github.com/kepano/clipper-templates/blob/main/templates/google-maps-clipper.json)
- [IMDB](https://github.com/kepano/clipper-templates/blob/main/templates/imdb-clipper.json)
- [IMDB (reference view)](https://github.com/kepano/clipper-templates/blob/main/templates/imdb-reference-clipper.json)
- [Letterboxd](https://github.com/kepano/clipper-templates/blob/main/templates/letterboxd-clipper.json)
- [Redfin](https://github.com/kepano/clipper-templates/blob/main/templates/redfin-clipper.json)
- [Wikipedia](https://github.com/kepano/clipper-templates/blob/main/templates/wikipedia-clipper.json)
- [Youtube](https://github.com/kepano/clipper-templates/blob/main/templates/youtube-clipper.json)

For a complete view of the repository, visit the [clipper-templates GitHub repository](https://github.com/kepano/clipper-templates).

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
- **Website:** [louminai.com](http://louminai.com/)
- **GitHub:** [thedavidyoungblood/Obsidian-WebClipper-Template-Generator](https://github.com/thedavidyoungblood/Obsidian-WebClipper-Template-Generator)

---

## Acknowledgements

Special thanks to the Obsidian team, the open source community, and contributors like AI (ChatGPT) for inspiring and supporting this project.

*Happy Clipping!*
