import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.join(working_directory, file_path)
        full_path = os.path.abspath(full_path)
        working_abs = os.path.abspath(working_directory)
        root, ext = os.path.splitext(file_path)


        if not full_path.startswith(working_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_path):
            return f'Error: File "{file_path}" not found.'
        if ext != ".py":
            f'Error: "{file_path}" is not a Python file.'
    
        result = subprocess.run(
            [ "python3" , file_path, *args],
            cwd=working_directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30
        )

        out = result.stdout or ""
        err = result.stderr or ""

        parts = []
        if out:
            parts.append(f"STDOUT:{out}")
        if err:
            parts.append(f"STDERR:{err}")
        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")
        if not parts:
            return "No output produced"
        return "\n".join(parts).rstrip()

    except Exception as e:
        return f"Error: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)