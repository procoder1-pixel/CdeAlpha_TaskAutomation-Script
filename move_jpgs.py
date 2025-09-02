import os
import shutil

def move_jpgs():
    print("⚙️ Task Automation: Move all .jpg files to a new folder (CodeAlpha Task 3)")
    folder = input("Enter the folder path to scan: ").strip()
    if not os.path.isdir(folder):
        print("❌ Folder not found.")
        return

    # Destination folder inside the given folder
    dest = os.path.join(folder, "JPG_Images")
    os.makedirs(dest, exist_ok=True)

    moved = 0
    for name in os.listdir(folder):
        src = os.path.join(folder, name)
        # Only move files with .jpg (and commonly .jpeg for practicality)
        if os.path.isfile(src) and (name.lower().endswith(".jpg") or name.lower().endswith(".jpeg")):
            shutil.move(src, os.path.join(dest, name))
            moved += 1

    print(f"✅ Moved {moved} file(s) to: {dest}")

if __name__ == "__main__":
    move_jpgs()
