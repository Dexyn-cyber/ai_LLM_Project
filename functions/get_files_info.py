import os
from google.genai import types
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def get_files_info(working_directory, directory="."):

    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        working_abs = os.path.abspath(working_directory)
        if not full_path.startswith(working_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        lst_files = os.listdir(full_path)
        gathered = []
        for item in lst_files:
            current_item_full_path = os.path.join(full_path, item)
            if os.path.isfile(current_item_full_path):
                gathered.append(f"- {item}: file_size={os.path.getsize(current_item_full_path)} bytes, is_dir={os.path.isdir(current_item_full_path)}")
            else:
                gathered.append(f"- {item}: is_dir={os.path.isdir(current_item_full_path)}")

        output = "\n".join(gathered)
        return output
    except Exception as e:
        return f"Error: {e}"