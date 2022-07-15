with open('HenryV.txt') as file_handle:
    file_data = file_handle.read()
file_data = file_data + '\nHenry V, William Shakespeare'
with open('HenryV.txt', 'w') as file_handle:
    file_handle.write(file_data)
with open('HenryV.txt') as file_handle:
    print(file_handle.read())