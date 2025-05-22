def read_file(file_path):
    try:
        with open(f"{file_path}", 'r') as file:
            print(file.read())
    except Exception as e:
        return (f"Error: {e}")
        
print(read_file('text.txt'))
        
        
        