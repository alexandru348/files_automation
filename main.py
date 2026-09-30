from pathlib import Path

# V1 flow in main.py:

# 1. Get the folder path and validate it.

folder_path = input("Folder path: ")
print(folder_path)

folder_exists = Path(folder_path).is_dir()
print(folder_exists)

if not folder_exists:
    raise SystemExit("Path must point to an existing folder.")

# 2. Scan the files directly inside the folder.

files = []
found = 0
skipped = 0

for item in Path(folder_path).iterdir():
    if item.is_file():
        found = found + 1
        if item.name in ("main.py", "organizer.py"):
            skipped = skipped + 1
        else:
            files.append(item)

print("Found:", found)
print("Skipped:", skipped)

if files:
    print("Files in folder:")
    for item in files:
        print(item.name)

# 3. Build the organization plan and show the preview.

plan = []

for item in files:
    extension = item.suffix.lower()
    if extension in (".txt", ".md", ".pdf", ".docx", ".xlsx", ".pptx"):
        category = "Documents"
    elif extension in (".jpg", ".jpeg", ".png", ".gif", "webp"):
        category = "Images"
    elif extension in (".zip", ".rar", ".7z"):
        category = "Archives"
    elif extension in (".py", ".cpp", ".h", ".html", ".css", ".js"):
        category = "Code"
    elif extension in (".mp3", ".wav"):
        category = "Audio"
    elif extension in (".mp4", ".mov", ".mkv"):
        category = "Video"
    else:
        category = "Other"

    plan.append((item, category))

if plan:
    print("Preview:")
    for item, category in plan:
        print(item.name, "->", category)
else:
    print("No files to organize.")
    raise SystemExit

# 4. Ask for the user's confirmation.

confirmation = input("Organize these files? (y/n): ").lower()

if confirmation != "y":
    print("Organization cancelled.")
    raise SystemExit

# 5. If the user confirms, start organizing the files.

for item, category in plan:
    destination_folder = Path(folder_path) / category
    destination_folder.mkdir(exist_ok=True)
    destination = destination_folder / item.name
    print(item.name, "->", destination)

# 6. Show the final report: found, moved, skipped, errors.

# Subfolders are ignored druing scanning, and the tool's Python files are protected.
# organizer.py handles name conflicts and errors during file moves.
