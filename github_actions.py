from spellchecker import SpellChecker
import os

def get_file_changes():
    """
    Get the list of files that have been modified in the PR.
    This function assumes you have already checked out the PR branch.
    """
    files = os.popen('git diff --name-only origin/main...HEAD').read().splitlines()
    print(f"Files changed: {files}")
    return files

def check_spelling_in_file(file_path):
    """
    Check spelling in a given file. Only checks code lines.
    """
    spell = SpellChecker()
    errors = []

    print(f"Checking file: {file_path}")
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return errors

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.split()
            for word in words:
                # Remove non-alphabetic characters
                clean_word = ''.join(filter(str.isalpha, word))
                if clean_word and clean_word not in spell:
                    errors.append((line_number, word))

    return errors

def run_spelling_checks():
    files = get_file_changes()
    all_errors = {}

    for file in files:
        errors = check_spelling_in_file(file)
        if errors:
            all_errors[file] = errors

    return all_errors

def main():
    errors = run_spelling_checks()
    if not errors:
        print("No spelling errors found.")
    else:
        for file, issues in errors.items():
            print(f"File: {file}")
            for line, word in issues:
                print(f"Spelling error in {file} at line {line}: '{word}'")

if __name__ == "__main__":
    main()