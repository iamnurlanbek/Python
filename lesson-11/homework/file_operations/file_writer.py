def write_file(file_path, content):
    try:
        with open(f"{file_path}", 'a') as file:
          file.write(content)
          print('FIle muvaffaqiyatli yozildi')
    except Exception as e:
        print(f"Error: {e}")
        
write_file('book.txt', 'salom')