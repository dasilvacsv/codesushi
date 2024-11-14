#!/usr/bin/env python3

import argparse
import os
import fnmatch
from typing import List, Set, Dict
import sys

class ContextBuilder:
    def __init__(self, ignore_patterns: List[str] = None):
        self.ignore_patterns = ignore_patterns or []
        self.processed_files: Set[str] = set()
        # Mapping of file extensions to markdown language identifiers
        self.language_map: Dict[str, str] = {
            # Programming Languages
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'jsx',
            '.tsx': 'tsx',
            '.html': 'html',
            '.css': 'css',
            '.scss': 'scss',
            '.sql': 'sql',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.cs': 'csharp',
            '.go': 'go',
            '.rs': 'rust',
            '.rb': 'ruby',
            '.php': 'php',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.r': 'r',
            '.sh': 'bash',
            '.bat': 'batch',
            '.ps1': 'powershell',
            
            # Config & Data
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.xml': 'xml',
            '.toml': 'toml',
            '.ini': 'ini',
            '.env': 'plaintext',
            
            # Documentation
            '.md': 'markdown',
            '.tex': 'latex',
            '.rst': 'rst',
            
            # Default for unknown extensions
            '': 'plaintext'
        }
        
    def get_language_identifier(self, file_path: str) -> str:
        """Determine the language identifier for markdown code blocks based on file extension."""
        _, ext = os.path.splitext(file_path)
        return self.language_map.get(ext.lower(), 'plaintext')

    def should_ignore(self, file_path: str) -> bool:
        """Check if a file should be ignored based on patterns."""
        normalized_path = file_path.replace('\\', '/')
        
        default_ignores = [
            '*.pyc', '__pycache__/*', '.git/*', '.DS_Store',
            '*.log', '*.tmp', '*.swp', '*.swo', 'node_modules/*',
            '*.exe', '*.dll', '*.so', '*.dylib', # Binaries
            '*.zip', '*.tar', '*.gz', '*.rar', # Archives
            '*.jpg', '*.jpeg', '*.png', '*.gif', '*.ico', # Images
            '*.pdf', '*.doc', '*.docx', # Documents
            '.env', '.env.*', # Environment files
            '.vscode/*', '.idea/*', # IDE files
        ]
        
        all_patterns = default_ignores + self.ignore_patterns
        return any(fnmatch.fnmatch(normalized_path, pattern) 
                  for pattern in all_patterns)

    def read_ignore_file(self, ignore_file_path: str) -> None:
        """Read ignore patterns from a file."""
        try:
            with open(ignore_file_path, 'r', encoding='utf-8') as f:
                patterns = [line.strip() for line in f if line.strip() 
                          and not line.startswith('#')]
                self.ignore_patterns.extend(patterns)
        except FileNotFoundError:
            print(f"Warning: Ignore file {ignore_file_path} not found.")

    def process_file(self, file_path: str, relative_path: str) -> str:
        """Process a single file and return its formatted markdown content."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().strip()
                language = self.get_language_identifier(file_path)
                return (f"## File: {relative_path}\n\n"
                       f"```{language}\n"
                       f"{content}\n"
                       f"```\n\n")
        except Exception as e:
            return (f"## File: {relative_path}\n\n"
                   f"```plaintext\n"
                   f"Error reading file: {str(e)}\n"
                   f"```\n\n")

    def process_directory(self, directory_path: str) -> str:
        """Process all files in a directory and its subdirectories."""
        output = []
        
        for root, dirs, files in os.walk(directory_path):
            # Sort directories and files for consistent output
            dirs.sort()
            files.sort()
            
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, directory_path)
                
                if not self.should_ignore(relative_path):
                    output.append(self.process_file(full_path, relative_path))
        
        return ''.join(output)

def main():
    parser = argparse.ArgumentParser(
        description="Build a context file from directory contents with Markdown formatting"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to process (default: current directory)"
    )
    parser.add_argument(
        "-i", "--ignore-file",
        help="Path to ignore file (similar to .gitignore)",
        default=".sushignore"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path",
        default="context_output.md"
    )
    parser.add_argument(
        "--no-header",
        action="store_true",
        help="Skip adding the header explanation"
    )
    
    args = parser.parse_args()
    
    builder = ContextBuilder()
    
    if os.path.exists(args.ignore_file):
        builder.read_ignore_file(args.ignore_file)
    
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            if not args.no_header:
                f.write(
                    "# Directory Context\n\n"
                    "This document contains the contents of the processed directory structure.\n"
                    "Each file is presented with its relative path and contents in a code block\n"
                    "with appropriate syntax highlighting based on the file type.\n\n"
                    "---\n\n"
                )
            
            content = builder.process_directory(args.directory)
            f.write(content)
        
        print(f"Markdown context file created successfully: {args.output}")
        
    except Exception as e:
        print(f"Error creating context file: {str(e)}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())