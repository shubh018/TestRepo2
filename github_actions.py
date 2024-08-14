import re
import sys

from spellchecker import SpellChecker
import os

# List of common built-in Python functions and keywords
BUILT_IN_FUNCTIONS = {'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'break', 'bytearray', 'bytes',
                      'callable', 'chr', 'classmethod', 'compile', 'complex', 'delattr', 'dict',
                      'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float',
                      'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help',
                      'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len',
                      'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object',
                      'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
                      'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
                      'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'}


def get_file_changes():
    """
    Get the list of files that have been modified in the PR.
    This function assumes you have already checked out the PR branch.
    """
    files = os.popen('git diff --name-only').read().splitlines()
    print(f"Files changed: {files}")
    return files


def extract_text_from_file(file_path):
    """
    Extract plain text from the file, ignoring variables, function names, and string literals.
    """
    with open(file_path, 'r') as file:
        content = file.read()

        # Remove comments and string literals
        content = re.sub(r'#.*', '', content)  # For Python comments
        content = re.sub(r'""".*?"""', '', content, flags=re.DOTALL)  # Triple quotes (Python docstrings)
        # content = re.sub(r"'.*?'", '', content)  # Single-line string literals
        # content = re.sub(r'".*?"', '', content)  # Double-line string literals

        # Remove function definitions and variable assignments
        content = re.sub(r'\bdef\b\s+\w+\s*\(.*?\)\s*:', '', content)  # Function definitions
        content = re.sub(r'\bclass\b\s+\w+\s*:', '', content)  # Class definitions
        content = re.sub(r'\b\w+\s*=\s*.*', '', content)  # Variable assignments

        # Remove built-in function calls and their variables
        for function in BUILT_IN_FUNCTIONS:
            pattern = rf'\b{function}\b\s*\(\s*\w*\s*\)'
            content = re.sub(pattern, '', content)

        return content


def check_spelling_in_file(file_path):
    """
    Check spelling in the file's plain text, excluding variables, function names, and strings.
    """
    spell = SpellChecker()
    errors = []

    print(f"Checking file: {file_path}")
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return errors

    content = extract_text_from_file(file_path)
    words = re.findall(r'\b\w+\b', content)

    for word in words:
        if word.lower() not in spell:
            errors.append(word)

    return errors


def run_spelling_checks():
    files = get_file_changes()
    all_errors = {}

    for file in files:
        errors = check_spelling_in_file(file)
        if errors:
            all_errors[file] = errors

    return all_errors

def is_integer(word):
    try:
        int(word)
        return True
    except ValueError:
        return False

def main():
    errors = run_spelling_checks()
    if not errors:
        print("No spelling errors found.")
        sys.exit(0)
    else:
        for file, issues in errors.items():
            print(f"File: {file}")
            for word in issues:
                if not is_integer(word):
                    print(f"Spelling error in {file}: '{word}'")
            sys.exit(1)


if __name__ == "__main__":
    main()
