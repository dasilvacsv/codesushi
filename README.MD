# CodeSushi 🍱

Roll up your codebase into a delicious markdown roll! 

CodeSushi is your code's favorite restaurant - it takes your raw files and serves them up as a perfectly formatted markdown document. Just like a sushi chef carefully prepares each roll, CodeSushi processes your code with precision and style.

## Why CodeSushi? 🤔

Ever needed to share your code in a clean, digestible format? CodeSushi takes your raw ingredients (files) and turns them into a perfectly plated dish (markdown document). Perfect for:

- 🍱 Rolling up codebase documentation
- 🥢 Serving code snippets to AI tools
- 🍶 Sharing code with perfect presentation
- 🍣 Preparing project documentation
- 🍙 Archiving code in style

## The Menu (Features) 

- 🎨 **Master Chef's Selection** (Syntax Highlighting)
  - Auto-detects file types
  - Applies beautiful syntax highlighting
  - Makes your code look delicious

- 🚫 **Quality Control** (Smart Ignore)
  - Filters out unwanted ingredients (.git, __pycache__, etc.)
  - Keeps your roll clean and fresh
  - Customizable filtering

- 📝 **Perfect Plating** (Markdown Output)
  - Beautifully formatted markdown
  - Clean code blocks
  - Consistent styling

- 🎯 **Custom Orders** (Customization)
  - Choose your ingredients (files)
  - Customize your roll (output)
  - Special requests welcome

- 🔄 **Multiple Locations** (Cross-Platform)
  - Serves Windows
  - Serves macOS
  - Serves Linux

- 🛡️ **Food Safety** (Error Handling)
  - Graceful error handling
  - Safe file processing
  - Clean error reporting

## Quick Start 🚀

```bash
# Take a seat at the counter
git clone https://github.com/yourusername/codesushi.git
cd codesushi

# Place your order
python codesushi.py

# Special requests welcome
python codesushi.py /path/to/kitchen      # Process specific directory
python codesushi.py -i .sushignore        # Custom ignore file
python codesushi.py -o fancy-roll.md      # Custom output file
python codesushi.py --no-header           # Skip the menu description
```

## Daily Special (.sushignore) 🎋

Create a `.sushignore` file to tell our chef what to leave out:

```plaintext
# Kitchen cleanup
*.pyc
__pycache__/
.git/
.env

# No leftovers
build/
dist/
*.log

# Chef's private recipes
.vscode/
.idea/
```

## How We Roll 🔄

The output is served in this format:

```markdown
# Today's Special

Fresh code, served with care.

## Roll: src/main.py
```python
# Your delicious code here
```

## Roll: config/settings.json
```json
// Perfectly seasoned settings
```
```

## À La Carte (Supported Languages) 🍽️

Our kitchen specializes in:

🍣 **Main Course**
- Python (.py)
- JavaScript (.js, .jsx)
- TypeScript (.ts, .tsx)
- HTML, CSS, SQL

🍤 **Side Dishes**
- JSON, YAML, TOML
- XML, INI, ENV

🍜 **Specials**
- Markdown (.md)
- LaTeX (.tex)
- Shell scripts

## Catering Service (Module Usage) 👨‍🍳

Want to run your own kitchen? Use our recipes:

```python
from context import ContextBuilder

def example():
    builder = ContextBuilder()
    
    # Add custom ignore patterns if needed
    builder.ignore_patterns.extend([
        '*.custom',
        'specific_dir/*'
    ])
    
    # Process directory
    with open('output.md', 'w', encoding='utf-8') as f:
        content = builder.process_directory('./src')
        f.write(content)
```

## TODO (Kitchen Improvements) 🎯

1. **New Location** 🏯
   - Opening Node.js branch
   - Setting up TypeScript kitchen
   - Training new chefs (CLI tools)

2. **Menu Expansion** 📜
   - Adding new file type specials
   - Improving plating techniques
   - Enhancing error handling recipes

3. **Quality Control** ✨
   - Implementing master chef reviews
   - Adding freshness checks
   - Improving serving speed

4. **Special Menu** 🌟
   - Adding custom plating options
   - Creating party platters (batch processing)
   - Developing vegetarian options (lightweight mode)

5. **Customer Service** 📋
   - Improving documentation
   - Adding usage examples
   - Creating chef's recommendations

## Contributing 🤝

Want to join our kitchen crew? We're always looking for new chefs! Feel free to:
- Submit new recipes (Pull Requests)
- Suggest menu items (Features)
- Report food quality issues (Bugs)
