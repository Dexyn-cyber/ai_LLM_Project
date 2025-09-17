import os
from google.genai import types

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
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)