import os

def get_files_info(working_directory, directory="."):

    try:
        full_path = os.path.join(working_directory, directory)
        full_path = os.path.abspath(full_path)
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