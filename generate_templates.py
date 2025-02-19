#!/usr/bin/env python3

r"""
§ - "meRead" - as a 'mini-Readme,' in the script itself - §

# Header Metadata

**Script Name**: Obsidian WebClipper Template Generator  
**Author**: David Youngblood  
**Creation Date**: 2025-02-18  
**Last Modified Date**: 2025-02-19  
**Version**: 1.2.1  
**Dependencies**:
- Python 3.7 or higher

## **CHANGELOG:**
- **v1.2.1:**
  - Added functionality to clone each generated JSON template into a centralized repository at `{VAULT-ROOT}/Clippings/TEMPLATES` for unified management.
  - Updated the "meRead" section to include a sterilized example of the expected terminal output.
  - Enhanced user guidance and overall script robustness.

**Description**:  
This script automates the creation of JSON template files for Obsidian WebClipper. It prompts the user for a VAULT-ROOT-PATH and recursively generates the required directory structure along with all the JSON templates in their respective subdirectories. Additionally, it produces a `README_IMPORT_GUIDANCE.txt` file with detailed instructions on how to import these templates into the Obsidian WebClipper Chrome extension.

Moreover, after generating each template in its designated folder, the script also clones every template into a centralized repository located at:

  **{VAULT-ROOT}/Clippings/TEMPLATES**

This repository is intended for managing all templates in one place.

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
   After the script finishes, navigate to the specified vault root. Review the generated `README_IMPORT_GUIDANCE.txt` for step‑by‑step instructions on importing the JSON templates into Obsidian WebClipper.

**Expected Terminal Output (Sterilized Example)**:

```shell
PS C:\Vaults\ExampleVault> python generate_templates.py
Enter the VAULT-ROOT-PATH where templates should be generated: C:\Vaults\ExampleVault
Created template 'Custom Default - Verbatim Clone (Clean)' at: C:\Vaults\ExampleVault\Clippings\Custom_Default_Verbatim_Clone_Clean.json
Cloned template 'Custom Default - Verbatim Clone (Clean)' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Custom_Default_Verbatim_Clone_Clean.json
Created template 'Custom Summary' at: C:\Vaults\ExampleVault\Clippings\Summaries\Custom_Summary.json
Cloned template 'Custom Summary' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Custom_Summary.json
Created template 'Custom Research & AI Insights' at: C:\Vaults\ExampleVault\Clippings\Research\Custom_Research_AI_Insights.json
Cloned template 'Custom Research & AI Insights' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Custom_Research_AI_Insights.json
Created template 'Custom Translation' at: C:\Vaults\ExampleVault\Clippings\Translations\Custom_Translation.json
Cloned template 'Custom Translation' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Custom_Translation.json
Created template 'Custom News/Blog Article' at: C:\Vaults\ExampleVault\Clippings\Articles\Custom_News_Blog_Article.json
Cloned template 'Custom News/Blog Article' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Custom_News_Blog_Article.json
Created template 'Custom Highlights Only' at: C:\Vaults\ExampleVault\Clippings\Highlights\Custom_Highlights_Only.json
Cloned template 'Custom Highlights Only' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Custom_Highlights_Only.json
Created template 'GitHub Page' at: C:\Vaults\ExampleVault\Clippings\GitHub\GitHub_Page.json
Cloned template 'GitHub Page' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\GitHub_Page.json
Created template 'Medium Article' at: C:\Vaults\ExampleVault\Clippings\Medium\Medium_Article.json
Cloned template 'Medium Article' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Medium_Article.json
Created template 'Research / Academic' at: C:\Vaults\ExampleVault\Clippings\Research\Research_Academic.json
Cloned template 'Research / Academic' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Research_Academic.json
Created template 'Article / Blog' at: C:\Vaults\ExampleVault\Clippings\Articles\Article_Blog.json
Cloned template 'Article / Blog' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Article_Blog.json
Created template 'Generic Web Clip' at: C:\Vaults\ExampleVault\Clippings\Generic\Generic_Web_Clip.json
Cloned template 'Generic Web Clip' into repository at: C:\Vaults\ExampleVault\Clippings\TEMPLATES\Generic_Web_Clip.json

Created import guidance documentation at: C:\Vaults\ExampleVault\README_IMPORT_GUIDANCE.txt

All templates generated and cloned successfully.
PS C:\Vaults\ExampleVault\Clippings>
```

> MONO-SCRIPT to generate Obsidian WebClipper JSON template files

This script:
  1. Prompts for a VAULT-ROOT-PATH.
  2. Creates the necessary subdirectories for each template.
  3. Writes each JSON template (using json.dumps from a Python dictionary) into its designated folder.
  4. Clones all generated templates into the central repository at `{VAULT-ROOT}/Clippings/TEMPLATES`.
  5. Creates a supporting documentation file with guidance for importing these templates into the Obsidian WebClipper browser extension.
"""
# BEGIN SCRIPT EXECUTION

import os
import sys
import json

# Each template is now defined as a Python dictionary under the key "content_dict".
TEMPLATES = [
  {
    "name": "Custom Default - Verbatim Clone (Clean)",
    "filename": "Custom_Default_Verbatim_Clone_Clean.json",
    "subfolder": os.path.join("Clippings"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Custom Default - Verbatim Clone (Clean)",
      "behavior": "create",
      "noteContentFormat": '{{fullHtml|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "created", "value": "{{date}}", "type": "date"},
        {"name": "description", "value": "{{description}}", "type": "text"},
        {"name": "tags", "value": "web-clip, verbatim", "type": "multitext"}
      ],
      "triggers": [],
      "noteNameFormat": "{{title}}",
      "path": "Clippings"
    }
  },
  {
    "name": "Custom Summary",
    "filename": "Custom_Summary.json",
    "subfolder": os.path.join("Clippings", "Summaries"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Custom Summary",
      "behavior": "create",
      "noteContentFormat": '## Summary\n{{"Summarize the main points of this page in three bullet points."|blockquote}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "tags", "value": "web-clip, summary", "type": "multitext"}
      ],
      "triggers": [],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Summaries"
    }
  },
  {
    "name": "Custom Research & AI Insights",
    "filename": "Custom_Research_AI_Insights.json",
    "subfolder": os.path.join("Clippings", "Research"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Custom Research & AI Insights",
      "behavior": "create",
      "noteContentFormat": '## Research Insights\n{{"Extract key research and AI insights from this page concisely."|blockquote}}\n\n---\n**Captured on:** {{time}}\n\n## Full Content\n{{fullHtml|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "created", "value": "{{date}}", "type": "date"},
        {"name": "tags", "value": "web-clip, research, AI", "type": "multitext"}
      ],
      "triggers": [],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Research"
    }
  },
  {
    "name": "Custom Translation",
    "filename": "Custom_Translation.json",
    "subfolder": os.path.join("Clippings", "Translations"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Custom Translation",
      "behavior": "create",
      "noteContentFormat": '## Original Content\n{{fullHtml|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n## Translated Content\n{{"Translate the above content into [Target Language] in clear, concise Markdown."|blockquote}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "tags", "value": "web-clip, translation", "type": "multitext"}
      ],
      "triggers": [],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Translations"
    }
  },
  {
    "name": "Custom News/Blog Article",
    "filename": "Custom_News_Blog_Article.json",
    "subfolder": os.path.join("Clippings", "Articles"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Custom News/Blog Article",
      "behavior": "create",
      "noteContentFormat": '## Article Content\n{{selectorHtml:article|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "tags", "value": "web-clip, news, blog", "type": "multitext"}
      ],
      "triggers": [],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Articles"
    }
  },
  {
    "name": "Custom Highlights Only",
    "filename": "Custom_Highlights_Only.json",
    "subfolder": os.path.join("Clippings", "Highlights"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Custom Highlights Only",
      "behavior": "create",
      "noteContentFormat": '{{highlights|map: item => item.text|join:"\\n\\n"}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "tags", "value": "web-clip, highlights", "type": "multitext"}
      ],
      "triggers": [],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Highlights"
    }
  },
  {
    "name": "GitHub Page",
    "filename": "GitHub_Page.json",
    "subfolder": os.path.join("Clippings", "GitHub"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "GitHub Page",
      "behavior": "create",
      "noteContentFormat": '{{fullHtml|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "created", "value": "{{date}}", "type": "date"},
        {"name": "description", "value": "{{description}}", "type": "text"},
        {"name": "tags", "value": "web-clip, github", "type": "multitext"}
      ],
      "triggers": [
        "startsWith:https://github.com/"
      ],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/GitHub"
    }
  },
  {
    "name": "Medium Article",
    "filename": "Medium_Article.json",
    "subfolder": os.path.join("Clippings", "Medium"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Medium Article",
      "behavior": "create",
      "noteContentFormat": '{{selectorHtml:article|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "tags", "value": "web-clip, medium", "type": "multitext"}
      ],
      "triggers": [
        "startsWith:https://medium.com/"
      ],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Medium"
    }
  },
  {
    "name": "Research / Academic",
    "filename": "Research_Academic.json",
    "subfolder": os.path.join("Clippings", "Research"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Research / Academic",
      "behavior": "create",
      "noteContentFormat": '## Abstract\n{{selectorHtml:#abstract|remove_html:("header,footer,nav")|markdown}}\n\n---\n## Full Content\n{{fullHtml|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "created", "value": "{{date}}", "type": "date"},
        {"name": "tags", "value": "web-clip, research, academic", "type": "multitext"}
      ],
      "triggers": [
        "startsWith:https://arxiv.org/",
        "startsWith:https://www.researchgate.net/",
        "regex:/.*(research|journal|paper).*/i"
      ],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Research"
    }
  },
  {
    "name": "Article / Blog",
    "filename": "Article_Blog.json",
    "subfolder": os.path.join("Clippings", "Articles"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Article / Blog",
      "behavior": "create",
      "noteContentFormat": '{{selectorHtml:article|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "tags", "value": "web-clip, article, blog", "type": "multitext"}
      ],
      "triggers": [
        "regex:/^https:\\/\\/(www\\.)?(nytimes|techcrunch|theverge|blogspot|medium)\\./i"
      ],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Articles"
    }
  },
  {
    "name": "Generic Web Clip",
    "filename": "Generic_Web_Clip.json",
    "subfolder": os.path.join("Clippings", "Generic"),
    "content_dict": {
      "schemaVersion": "0.1.0",
      "name": "Generic Web Clip",
      "behavior": "create",
      "noteContentFormat": '{{fullHtml|remove_html:("header,footer,nav,aside,.ad,.advertisement")|markdown}}\n\n---\n**Captured on:** {{time}}',
      "properties": [
        {"name": "title", "value": "{{title}}", "type": "text"},
        {"name": "source", "value": "{{url}}", "type": "text"},
        {"name": "author", "value": '{{author|split:", "|wikilink|join}}', "type": "multitext"},
        {"name": "published", "value": "{{published}}", "type": "date"},
        {"name": "created", "value": "{{date}}", "type": "date"},
        {"name": "description", "value": "{{description}}", "type": "text"},
        {"name": "tags", "value": "web-clip, generic", "type": "multitext"}
      ],
      "triggers": [
        "default"
      ],
      "noteNameFormat": "{{title}}",
      "path": "Clippings/Generic"
    }
  }
]

# Documentation text for importing templates into Obsidian WebClipper
IMPORT_GUIDANCE = '''Obsidian WebClipper Template Import Guidance
=============================================

The following steps will help you import the JSON templates into Obsidian WebClipper:

1. Open your Obsidian Vault in your file explorer. The vault root is the folder you specified when running this script.
2. Within the vault, you will see a “Clippings” folder with various sub-folders (e.g. Summaries, Research, Translations, Articles, Highlights, GitHub, Medium, and Generic) and a central repository folder at Clippings/TEMPLATES.
3. In your web browser (Chrome or compatible), open the Obsidian WebClipper extension settings.
4. Look for the option to “Import Templates” (or similar).
5. When prompted, navigate to the vault root and then drill down to the appropriate subfolder or to Clippings/TEMPLATES to select the JSON template file(s) you wish to import.
6. Follow any on‑screen instructions to complete the import.
7. Once imported, these templates will be available within the WebClipper for creating new notes directly in your Obsidian Vault.

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
        
        # Create central repository folder for cloning templates
        repo_folder = os.path.join(vault_root, "Clippings", "TEMPLATES")
        os.makedirs(repo_folder, exist_ok=True)
        
        # Process each template: write to designated folder and clone into repo_folder
        for tpl in TEMPLATES:
            target_dir = os.path.join(vault_root, tpl["subfolder"])
            os.makedirs(target_dir, exist_ok=True)
            file_path = os.path.join(target_dir, tpl["filename"])
            content_json = json.dumps(tpl["content_dict"], indent=2, ensure_ascii=False)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content_json)
            print(f"Created template '{tpl['name']}' at: {file_path}")
            
            # Clone into central repository
            clone_path = os.path.join(repo_folder, tpl["filename"])
            with open(clone_path, "w", encoding="utf-8") as f:
                f.write(content_json)
            print(f"Cloned template '{tpl['name']}' into repository at: {clone_path}")
        
        # Write the import guidance documentation at the vault root
        guidance_path = os.path.join(vault_root, "README_IMPORT_GUIDANCE.txt")
        with open(guidance_path, "w", encoding="utf-8") as f:
            f.write(IMPORT_GUIDANCE)
        print(f"\nCreated import guidance documentation at: {guidance_path}")
        print("\nAll templates generated and cloned successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
