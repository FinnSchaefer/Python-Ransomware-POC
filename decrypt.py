import main_functions as ed

filtered_list = list(filter(None, ed.os_crawler()))
final_list = ed.flatten(filtered_list)

for extension in range(len(final_list)):
    ed.decrypt(final_list[extension], ed.load_key())
    if extension < 1:
        print("1 file done.")
    else:
        print(extension+1, "files done.")