#!/usr/bin/env python

import os
import shutil
import ast

# Step 1: Create a directory called 'foo_boo' in the project root
import os

import os
import argparse
import ast

# Step 2: Parse the target file for imported packages
parser = argparse.ArgumentParser(description='Copy Python packages and their documentation to a new directory.')
parser.add_argument('code_file', type=str, help='Path to the Python file or Jupyter Notebook')
args = parser.parse_args()

# Get the path to the target file
code_file = args.code_file

# Check if the path is relative or absolute
if not os.path.isabs(code_file):
  # If the path is relative, make it absolute by joining it with the current working directory
  code_file = os.path.join(os.getcwd(), code_file)

# Check if the target file exists
if not os.path.exists(code_file):
  print("File does not exist. Please provide a valid path.")
  exit()

# Parse the target file for imported packages
with open(code_file) as f:
  tree = ast.parse(f.read())

# Step 3: Get a list of all installed Python packages and their corresponding source directories
packages = []

for node in ast.walk(tree):
  if isinstance(node, ast.Import):
    packages.extend([alias.name for alias in node.names])
  elif isinstance(node, ast.ImportFrom):
    if node.module:
      packages.append(node.module)

packages = list(set(packages))  # Remove duplicates

# Step 4: Create subdirectories for each package in the 'foo_boo' directory
for package in packages:
  os.makedirs(f'foo_boo/{package}', exist_ok=True)

# Step 5: Copy the source code of each package to its respective subdirectory in 'foo_boo'
for package in packages:
  try:
    package_path = __import__(package).__path__[0]
    shutil.copytree(package_path, f'foo_boo/{package}')
  except (ImportError, AttributeError):
    print(f"Unable to find source code for package: {package}")

# Step 6: Generate documentation for each package (if available) and copy it to the respective subdirectory in 'foo_boo'
for package in packages:
  try:
    os.system(f"pydoc -w {package}")
    shutil.move(f"{package}.html", f"foo_boo/{package}/{package}.html")
  except Exception as e:
    print(f"Unable to generate documentation for package: {package}\nError: {e}")

# Step 7: Check if the directory already exists
if not os.path.exists('/docs/references/packages'):
  print("Directory does not exist. Please create it manually.")
  exit()

# Check if the virtual environment is activated
if not os.environ.get('VIRTUAL_ENV'):
  print("Virtual environment is not activated. Please activate it and try again.")
  exit()

for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        packages.extend([alias.name for alias in node.names])
    elif isinstance(node, ast.ImportFrom):
        if node.module:
            packages.append(node.module)

packages = list(set(packages))  # Remove duplicates

# Step 4: Create subdirectories for each package in the 'foo_boo' directory
for package in packages:
    os.makedirs(f'foo_boo/{package}', exist_ok=True)

# Step 5: Copy the source code of each package to its respective subdirectory in 'foo_boo'
for package in packages:
    try:
        package_path = __import__(package).__path__[0]
        shutil.copytree(package_path, f'foo_boo/{package}')
    except (ImportError, AttributeError):
        print(f"Unable to find source code for package: {package}")

# Step 6: Generate documentation for each package (if available) and copy it to the respective subdirectory in 'foo_boo'
for package in packages:
    try:
        os.system(f"pydoc -w {package}")
        shutil.move(f"{package}.html", f"foo_boo/{package}/{package}.html")
    except Exception as e:
        print(f"Unable to generate documentation for package: {package}\nError: {e}")
