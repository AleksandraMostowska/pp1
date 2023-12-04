# 10.	Find any JSON file on the Internet and download it to your computer. Open the file in any character editor 
# and read its contents. Then, write a program that displays the contents of the JSON file. Sample result:
# import json

# with open("filename.json") as file:
#     data = json.load(file)

# for key,value in data.items():
#     print(f"{key} : {value}")

import json

with open("filename.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")
