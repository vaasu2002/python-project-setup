import os
from pathlib import Path # make application IS independent
import logging

logging.basicConfig( # helps in debugging
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# list of files:
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    'setup.cfg',
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "": # if the file directory doesnt exist 
        os.makedirs(filedir, exist_ok=True) # we create the directory
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # file doesn't exists or file path is zero
        with open(filepath, "w") as f: # we create empty file
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else: # so we wont override the existing file
        logging.info(f"file is already present at: {filepath}") 