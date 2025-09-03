from functions.run_python_file import run_python_file

calc = "calculator"
print(run_python_file(calc, "main.py"))
print(run_python_file(calc, "main.py", ["3 + 5"]))
print(run_python_file(calc, "test.py"))
print(run_python_file(calc, "../main.py"))
print(run_python_file(calc, "nonexistent.py"))