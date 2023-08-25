import os
import fnmatch
from tqdm import tqdm
from bs4 import BeautifulSoup

def search_files_batch(root, pattern, content, folders=None, batch_size=100):
    matches = []

    total_files = 0
    processed_files = 0

    # Count the total number of relevant files
    for path, dirs, files in os.walk(root):
        if folders is None or any(folder in path for folder in folders):
            for filename in fnmatch.filter(files, pattern):
                total_files += 1

    # Split the content input into individual search terms
    search_terms = [term.strip().lower() for term in content.split(',')]

    # Process files in batches
    with tqdm(total=total_files, unit='file') as pbar:
        batch = []
        for path, dirs, files in os.walk(root):
            if folders is None or any(folder in path for folder in folders):
                for filename in fnmatch.filter(files, pattern):
                    file_path = os.path.join(path, filename)
                    batch.append(file_path)

                    if len(batch) >= batch_size:
                        matches.extend(process_batch(batch, search_terms))
                        batch = []

                    processed_files += 1
                    pbar.update(1)

        if batch:
            matches.extend(process_batch(batch, search_terms))

    return matches

def process_batch(batch, search_terms):
    batch_matches = []
    for file_path in batch:
        if any(term in file_path.lower() for term in search_terms) or contains_content(file_path, search_terms):
            batch_matches.append(file_path)
            print(file_path)
            print("\nMatched files found so far:")
            for i, matched_file in enumerate(batch_matches, 1):
                print(f"{i}. {matched_file}")
            print("=" * 50)
    return batch_matches

def contains_content(file_path, search_terms):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    with open(file_path, 'r') as file:
        file_content = file.read().lower()

        if file_extension == '.html':
            soup = BeautifulSoup(file_content, 'html.parser')
            file_content = soup.get_text()

        if any(term in file_content for term in search_terms):
            return True
    return False

print("""\n
========================NOTICE==========================
THIS IS A TOOL FOR SEARCHING FILES WITH PARAMETERS.

INTENDED FOR SPECIFIC-USE ONLY.
(Such as: Documents with specific file names or content)
========================NOTICE==========================
""")

# Prompt user for directory
directory = input("Enter the directory to search in: ")

# Prompt user for file pattern
file_pattern = input("Enter the file pattern or extension (e.g., *.txt, *.html): ")

# Prompt user for folder names to search in
folder_input = input("Enter the folder names to search in (separated by commas) or leave empty to search in all folders: ")
folders = [folder.strip() for folder in folder_input.split(',')] if folder_input else None

# Prompt user for batch size
batch_size = int(input("Enter the batch size (number of files per batch): "))

# Example usage
search_content = input("Enter the content you want to search for (separated by commas): ")

results = search_files_batch(directory, file_pattern, search_content, folders, batch_size=batch_size)

if results:
    print("\n[!] Search completed. Documents containing the specified content or matching file name:")
    for file_path in results:
        print(file_path)
else:
    print("\nNo matching documents found.")

# Save results to a text file in the same directory as the program
output_file = os.path.join(os.getcwd(), "search_results.txt")
with open(output_file, 'w') as file:
    if results:
        file.write(f"Search results ({search_content}, {file_pattern}):\n")
        for file_path in results:
            file.write(file_path + "\n")
    else:
        file.write(f"No matching documents found ({search_content}, {file_pattern}).")

print(f"\nSearch results saved to {output_file}")
print(f"Output file directory: {os.path.dirname(os.path.abspath(output_file))}")

# Prompt user to press any key to continue
input("Press any key to continue...")
