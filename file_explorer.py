import os
import sys
import mimetypes

def size_types(size):
    """ Determines the size of a file and assigns a label """

    if size < 1024:
        return f"{size}B"

    elif size < 1024**2:
        return f"{size/1024:.1f}KB"

    elif size < 1024**3:
        return f"{size/1024**2:.1f}MB"

    elif size < 1024**4:
        return f"{size/1024**3:.1f}GB"

    else:
        return f"{size/1024**4:.1f}TB"


directory = sys.argv[1]

for item in os.listdir(directory):
    path = os.path.join(directory, item)
    full_path = os.path.abspath(path)

    if os.path.isfile(path):
        size = os.path.getsize(path)
        mime_type, _ = mimetypes.guess_type(path)

        if mime_type is None:
            mime_type = "Unknown"

        item_type = "file"

        size_format = size_types(size)

    else:
        size = "0B"
        item_type = "dir" 

    print(f"{full_path} [{item_type}] {size_format} {mime_type}")
