import os
import ast

def find_functions_in_file(file_path):
    """
    Parse a Python file and return:
      - total number of functions
      - list of functions without docstrings
    """
    total_functions = 0
    missing_docstrings = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            tree = ast.parse(content)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                total_functions += 1

                # Check if docstring exists
                if not ast.get_docstring(node):
                    missing_docstrings.append({
                        "name": node.name,
                        "file": file_path,
                        "line": node.lineno
                    })

    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"⚠️ Error reading {file_path}: {e}")

    return total_functions, missing_docstrings


def scan_project(directory):
    """
    Scan all Python files in the given directory.
    Return total function count and list of missing docstrings.
    """
    total_functions = 0
    missing_docstrings = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_total, file_missing = find_functions_in_file(file_path)

                total_functions += file_total
                missing_docstrings.extend(file_missing)

    return total_functions, missing_docstrings


if __name__ == "__main__":
    project_directory = r"C:\Users\sayabane\Downloads\ann-lib-ads"  # change path if needed

    if not os.path.exists(project_directory):
        print(f"❌ Directory {project_directory} does not exist.")
        exit(1)

    total, missing = scan_project(project_directory)

    print("\n" + "="*60)
    print(f"📊 TOTAL FUNCTIONS IN PROJECT: {total}")
    print(f"⚠️ FUNCTIONS MISSING DOCSTRINGS: {len(missing)}")
    print("="*60)

    if missing:
        print("\nDetails of functions missing docstrings:")
        for fn in missing:
            print(f" - {fn['file']}:{fn['line']} -> {fn['name']}")
