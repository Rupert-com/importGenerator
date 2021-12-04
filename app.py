import os
import sys

# import <filename> from "./../@static/media/<filename>.<extension>"

try:
    sys.argv[3] == ""
except IndexError:
    print(
        f"""
        please use as following:
        app.py [directory] "[extension's]" "[printFormat]"
        
        directory: Folders directory
        
        extension's: one or more file extension seperated by comma `,`
        
        printFormat: something like `import <filename> from "./../@static/media/<filename>.<extension>"` where <filename> and <extension> are replaced properly
        """
    )

directory = sys.argv[1]
includeExtensions = sys.argv[2].split(",")
outputFormat = sys.argv[3]

output = "\n"
for file in os.listdir(directory):
    extension = file.split(".")[-1]
    filename = file[: (len(file) - len(extension) - 1)]
    if extension in includeExtensions:
        coutput = outputFormat.replace("<filename>", filename).replace(
            "<extension>", extension
        )
        output += coutput + "\n"
    else:
        continue

print(output)
