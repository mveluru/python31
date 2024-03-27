#venv/example.txt

base_path = r"/Users/mveluru/IdeaProjects/python312/venv/example.txt"
file_name = "example.tx"

file_path = base_path+"/"+file_name
with open(file_path, w)as file:
    file.write("Hello, This is an example file")
print("Task completed successfully")