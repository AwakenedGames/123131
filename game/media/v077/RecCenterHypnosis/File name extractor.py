import os

# Get the directory path of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Obtain the list of .webp file names in the current directory
webp_file_names = [item for item in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, item)) and item.lower().endswith('.webp')]

# Display the .webp file names with custom formatting and paragraph spacing
print("List of .webp file names:")
for index, webp_file_name in enumerate(webp_file_names, start=1):
    print(f"image {webp_file_name[:-5]}:")
    print(f"    {os.path.basename(current_directory)} + '{webp_file_name}'")
    print(f"    zoom .6")
    print()  # Adding a blank line for paragraph spacing
