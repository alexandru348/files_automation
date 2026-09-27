from pathlib import Path

# V1 flow in main.py:

# 1. Get the folder path and validate it.

folder_path = input("Folder path: ")
print(folder_path)

folder_exists = Path(folder_path).is_dir()
print(folder_exists)

# 2. Scan the files directly inside the folder.
# 3. Build the organization plan and show the preview.
# 4. Ask for the user's confirmation.
# 5. If the user confirms, start organizing the files.
# 6. Show the final report: found, moved, skipped, errors.

# Subfolders are ignored druing scanning, and the tool's Python files are protected.
# organizer.py handles name conflicts and errors during file moves.
