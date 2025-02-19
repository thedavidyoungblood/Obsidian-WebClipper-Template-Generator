#!/usr/bin/env python3
"""
§ - "meRead" - as a 'mini-Readme,' in the script itself - §

# Header Metadata

**Script Name**: Obsidian WebClipper Template Generator  
**Author**: David Youngblood  
**Creation Date**: 2025-02-18  
**Last Modified Date**: 2025-02-18  
**Version**: 1.0.0  
**Dependencies**:
- Python 3.7 or higher

**Description**:  
This script automates the creation of JSON template files for Obsidian WebClipper. It prompts the user for a VAULT-ROOT-PATH and recursively generates the required directory structure along with all the JSON templates in their respective subdirectories. Additionally, it produces a README_IMPORT_GUIDANCE.txt file with detailed instructions on how to import these templates into the Obsidian WebClipper Chrome extension.

**Usage**:

1. **Set up the environment** (if desired):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

2. **Run the Script**:
   Execute the script from your terminal or command prompt:
   ```bash
   python generate_templates.py
   ```
   When prompted, enter the full VAULT-ROOT-PATH where you want the templates and documentation generated.

3. **Importing Templates**:
   After the script finishes, navigate to the specified vault root. Review the generated `README_IMPORT_GUIDANCE.txt` for step-by-step instructions on importing the JSON templates into Obsidian WebClipper.

**Contact Information**:  
Email: opensource@louminai.com  
Website: [louminai.com](http://louminai.com)  
GitHub: [https://github.com/LouminAILabs/Obsidian-WebClipper-Template-Generator](https://github.com/LouminAILabs/Obsidian-WebClipper-Template-Generator)  
License: MIT

---

# Script Overview and Purpose

The Obsidian WebClipper Template Generator is designed to streamline the setup of your Obsidian Vault with pre-defined JSON templates for the WebClipper extension. The script:
- Prompts for a VAULT-ROOT-PATH.
- Creates a structured set of subdirectories.
- Writes each JSON template into its respective directory.
- Generates documentation to guide you in importing these templates into Obsidian WebClipper.

## Linkages and Backlinks

- **Related File**:  
  - `generate_templates.py` (this script)

- **Output Document**:  
  - `README_IMPORT_GUIDANCE.txt` (generated in the vault root)

## Integration Pointers

- **Interacts with**:  
  - Obsidian WebClipper (Chrome extension) via imported JSON templates.
- **Outputs**:  
  - A structured folder of JSON template files.
  - A guidance README for template import.

## Prerequisites and Dependencies

- **Python Version**: Requires Python 3.7 or higher.
- **Libraries**: Uses only the Python Standard Library—no additional modules required.

## Versioning Details

- **Script Version**: 1.2.0  
- **Last Updated**: 2025-02-18  
- **Change Log**:
  - **v1.0.0**: Initial release with full template generation and guidance documentation.
  - **v1.2.0**: updated bug in JSON properties causing error in import of templates.

## Example Usage in Production

```bash
# (Optional) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Run the template generator script
python generate_templates.py

# Follow the on-screen prompt to enter the VAULT-ROOT-PATH.
# After execution, check the vault root for the generated JSON templates and the README_IMPORT_GUIDANCE.txt.
```

---

MONO-SCRIPT to generate Obsidian WebClipper JSON template files

This script:
  1. Prompts for a VAULT-ROOT-PATH.
  2. Creates the necessary subdirectories for each template.
  3. Writes each JSON template (with its variant) into its designated folder.
  4. Creates a supporting documentation file with guidance for importing these
     templates into the Obsidian WebClipper browser extension.

Templates generated:
  1. Custom Default – Verbatim Clone (Clean)        --> Clippings/
  2. Custom Summary                                 --> Clippings/Summaries/
  3. Custom Research & AI Insights                  --> Clippings/Research/
  4. Custom Translation                             --> Clippings/Translations/
  5. Custom News/Blog Article                       --> Clippings/Articles/
  6. Custom Highlights Only                         --> Clippings/Highlights/
  7. GitHub Page (Triggered)                        --> Clippings/GitHub/
  8. Medium Article (Triggered)                     --> Clippings/Medium/
  9. Research / Academic (Triggered)                --> Clippings/Research/
  10. Article / Blog (Triggered)                    --> Clippings/Articles/
  11. Generic Web Clip (Fallback Triggered)         --> Clippings/Generic/

After running this script, use the generated “README_IMPORT_GUIDANCE.txt”
for instructions to import these JSON files as templates into Obsidian WebClipper.
"""

import os
import sys

# List of template definitions
TEMPLATES = [
    {
        "name": "Custom Default - Verbatim Clone (Clean)",
        "filename": "Custom_Default_Verbatim_Clone_Clean.json",
        "subfolder": os.path.join("Clippings"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Custom Default - Verbatim Clone (Clean)",
  "behavior": "create",
  "noteContentFormat": "{{fullHtml|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "created",
      "value": "{{date}}",
      "type": "date"
    },
    {
      "name": "description",
      "value": "{{description}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, verbatim",
      "type": "multitext"
    }
  ],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Clippings"
}'''
    },
    {
        "name": "Custom Summary",
        "filename": "Custom_Summary.json",
        "subfolder": os.path.join("Clippings", "Summaries"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Custom Summary",
  "behavior": "create",
  "noteContentFormat": "## Summary\\n{{\\"Summarize the main points of this page in three bullet points.\\"|blockquote}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, summary",
      "type": "multitext"
    }
  ],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Summaries"
}'''
    },
    {
        "name": "Custom Research & AI Insights",
        "filename": "Custom_Research_AI_Insights.json",
        "subfolder": os.path.join("Clippings", "Research"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Custom Research & AI Insights",
  "behavior": "create",
  "noteContentFormat": "## Research Insights\\n{{\\"Extract key research and AI insights from this page concisely.\\"|blockquote}}\\n\\n---\\n**Captured on:** {{time}}\\n\\n## Full Content\\n{{fullHtml|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "created",
      "value": "{{date}}",
      "type": "date"
    },
    {
      "name": "tags",
      "value": "web-clip, research, AI",
      "type": "multitext"
    }
  ],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Research"
}'''
    },
    {
        "name": "Custom Translation",
        "filename": "Custom_Translation.json",
        "subfolder": os.path.join("Clippings", "Translations"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Custom Translation",
  "behavior": "create",
  "noteContentFormat": "## Original Content\\n{{fullHtml|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n## Translated Content\\n{{\\"Translate the above content into [Target Language] in clear, concise Markdown.\\"|blockquote}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, translation",
      "type": "multitext"
    }
  ],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Translations"
}'''
    },
    {
        "name": "Custom News/Blog Article",
        "filename": "Custom_News_Blog_Article.json",
        "subfolder": os.path.join("Clippings", "Articles"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Custom News/Blog Article",
  "behavior": "create",
  "noteContentFormat": "## Article Content\\n{{selectorHtml:article|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "tags",
      "value": "web-clip, news, blog",
      "type": "multitext"
    }
  ],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Articles"
}'''
    },
    {
        "name": "Custom Highlights Only",
        "filename": "Custom_Highlights_Only.json",
        "subfolder": os.path.join("Clippings", "Highlights"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Custom Highlights Only",
  "behavior": "create",
  "noteContentFormat": "{{highlights|map: item => item.text|join:\\"\\n\\n\\"}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, highlights",
      "type": "multitext"
    }
  ],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Highlights"
}'''
    },
    {
        "name": "GitHub Page",
        "filename": "GitHub_Page.json",
        "subfolder": os.path.join("Clippings", "GitHub"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "GitHub Page",
  "behavior": "create",
  "noteContentFormat": "{{fullHtml|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "created",
      "value": "{{date}}",
      "type": "date"
    },
    {
      "name": "description",
      "value": "{{description}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, github",
      "type": "multitext"
    }
  ],
  "triggers": [
    "startsWith:https://github.com/"
  ],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/GitHub"
}'''
    },
    {
        "name": "Medium Article",
        "filename": "Medium_Article.json",
        "subfolder": os.path.join("Clippings", "Medium"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Medium Article",
  "behavior": "create",
  "noteContentFormat": "{{selectorHtml:article|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, medium",
      "type": "multitext"
    }
  ],
  "triggers": [
    "startsWith:https://medium.com/"
  ],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Medium"
}'''
    },
    {
        "name": "Research / Academic",
        "filename": "Research_Academic.json",
        "subfolder": os.path.join("Clippings", "Research"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Research / Academic",
  "behavior": "create",
  "noteContentFormat": "## Abstract\\n{{selectorHtml:#abstract|remove_html:(\\"header,footer,nav\\")|markdown}}\\n\\n---\\n## Full Content\\n{{fullHtml|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "created",
      "value": "{{date}}",
      "type": "date"
    },
    {
      "name": "tags",
      "value": "web-clip, research, academic",
      "type": "multitext"
    }
  ],
  "triggers": [
    "startsWith:https://arxiv.org/",
    "startsWith:https://www.researchgate.net/",
    "regex:/.*(research|journal|paper).*/i"
  ],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Research"
}'''
    },
    {
        "name": "Article / Blog",
        "filename": "Article_Blog.json",
        "subfolder": os.path.join("Clippings", "Articles"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Article / Blog",
  "behavior": "create",
  "noteContentFormat": "{{selectorHtml:article|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "tags",
      "value": "web-clip, article, blog",
      "type": "multitext"
    }
  ],
  "triggers": [
    "regex:/^https:\\/\\/(www\\.)?(nytimes|techcrunch|theverge|blogspot|medium)\\./i"
  ],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Articles"
}'''
    },
    {
        "name": "Generic Web Clip",
        "filename": "Generic_Web_Clip.json",
        "subfolder": os.path.join("Clippings", "Generic"),
        "content": '''{
  "schemaVersion": "0.1.0",
  "name": "Generic Web Clip",
  "behavior": "create",
  "noteContentFormat": "{{fullHtml|remove_html:(\\"header,footer,nav,aside,.ad,.advertisement\\")|markdown}}\\n\\n---\\n**Captured on:** {{time}}",
  "properties": [
    {
      "name": "title",
      "value": "{{title}}",
      "type": "text"
    },
    {
      "name": "source",
      "value": "{{url}}",
      "type": "text"
    },
    {
      "name": "author",
      "value": "{{author|split:\", \"|wikilink|join}}",
      "type": "multitext"
    },
    {
      "name": "published",
      "value": "{{published}}",
      "type": "date"
    },
    {
      "name": "created",
      "value": "{{date}}",
      "type": "date"
    },
    {
      "name": "description",
      "value": "{{description}}",
      "type": "text"
    },
    {
      "name": "tags",
      "value": "web-clip, generic",
      "type": "multitext"
    }
  ],
  "triggers": [
    "default"
  ],
  "noteNameFormat": "{{title}}",
  "path": "Clippings/Generic"
}'''
    }
]

# Documentation text for importing templates into Obsidian WebClipper
IMPORT_GUIDANCE = '''Obsidian WebClipper Template Import Guidance
=============================================

The following steps will help you import the JSON templates into Obsidian WebClipper:

4. Open your Obsidian Vault in your file explorer. The vault root is the folder you specified when running this script.
5. Within the vault, you will see a “Clippings” folder (with sub-folders such as Summaries, Research, Translations, Articles, Highlights, GitHub, Medium, and Generic).
6. In your web browser (Chrome or compatible), open the Obsidian WebClipper extension settings.
7. Look for the option to “Import Templates” (or similar).
8. When prompted, navigate to the vault root and then drill down to the appropriate subfolder to select the JSON template file(s) you wish to import.
9. Follow any on-screen instructions to complete the import.
10. Once imported, these templates will be available within the WebClipper for creating new notes directly in your Obsidian Vault.

For any questions or troubleshooting, consult the Obsidian WebClipper documentation or support resources.
'''

def main():
    try:
        # Prompt user for vault root path
        vault_root = input("Enter the VAULT-ROOT-PATH where templates should be generated: ").strip()
        if not vault_root:
            print("Error: No path provided. Exiting.")
            sys.exit(1)
        if not os.path.isdir(vault_root):
            create = input(f"Directory '{vault_root}' does not exist. Create it? (y/n): ").strip().lower()
            if create == 'y':
                os.makedirs(vault_root, exist_ok=True)
                print(f"Created directory: {vault_root}")
            else:
                print("Aborted by user.")
                sys.exit(1)
        
        # Process each template
        for tpl in TEMPLATES:
            target_dir = os.path.join(vault_root, tpl["subfolder"])
            os.makedirs(target_dir, exist_ok=True)
            file_path = os.path.join(target_dir, tpl["filename"])
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(tpl["content"])
            print(f"Created template '{tpl['name']}' at: {file_path}")
        
        # Write the import guidance documentation at the vault root
        guidance_path = os.path.join(vault_root, "README_IMPORT_GUIDANCE.txt")
        with open(guidance_path, "w", encoding="utf-8") as f:
            f.write(IMPORT_GUIDANCE)
        print(f"\nCreated import guidance documentation at: {guidance_path}")
        print("\nAll templates generated successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
