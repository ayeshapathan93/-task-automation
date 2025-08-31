import os
import shutil
import re
import requests

# ---------- Option 1: Move all .jpg files ----------
def move_jpg_files(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file in os.listdir(src_folder):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(src_folder, file), os.path.join(dest_folder, file))
    print("✅ All .jpg files moved successfully!")


# ---------- Option 2: Extract emails from .txt ----------
def extract_emails(input_file, output_file):
    with open(input_file, "r") as f:
        text = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)

    with open(output_file, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print("✅ Emails extracted and saved to", output_file)


# ---------- Option 3: Scrape webpage title ----------
def scrape_webpage_title(url, output_file):
    response = requests.get(url)
    title = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE).group(1)

    with open(output_file, "w") as f:
        f.write("Webpage Title: " + title)

    print("✅ Title saved to", output_file)


# ---------- Run any one ----------
# Example usage:
# move_jpg_files("source_folder", "destination_folder")
# extract_emails("input.txt", "emails.txt")
# scrape_webpage_title("https://www.python.org", "title.txt")
