import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try: 
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(full_path)
        working_abs = os.path.abspath(working_directory)
        if not full_path.startswith(working_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f:
            content = f.read()
            f.close()
        if len(content) > MAX_CHARS:
            cap_content = content[:MAX_CHARS + 1]
            return cap_content + f'[...File "{file_path}" truncated at 10000 characters]'
        return content

    except Exception as e:
        return f"Error: {e}"