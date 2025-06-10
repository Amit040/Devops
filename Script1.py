#Monitor the log file in real time


import time

with open('app.log','r') as file:
    file.seek(0,2)  #Read the file from top to bottom
    print(f"Monitorin the file {file}")

    while True:
        line=file.readline()
        if line: #if any ne line is added
            print(line.strip())
        if "Error" in line:
            print("Error msg found")
        else:
            time.sleep(1)
