# Python-Ransomware-POC
A simple python Proof of Concept Ransomeware built using Fernet documentation and some extra spice.

**THIS IS FOR EDUCATIONAL PURPOSES ONLY**

This is a Proof of Concept (POC) ransomeware built using Python and the Fernet library. I will be updating this periodically when I can think of how to make it better. This is meant for educational purposes and my own understanding of how ransomeware works. I am open to any and all feedback :). Please be safe while you use this and use at your own risk. 

For safe use you can use the main.py to directly interface with the scripts.
For un-safe use you can simply run the encrypt script to generate a new key using Fernet and encrypt all files with the file extensions listed in main_functions.py os_crawler function.

Please keep in mind, if you do run this, that I am not responsible if your data becomes unrecoverable this is a simple Proof of Concept.
Also note not to delete the .key file that is generated until AFTER you decrypt the directory. I am adding functionality to clean up the .key files at a later date. 
