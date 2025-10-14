import qrcode


# QR Code Generator Function

def QrCode(filePath):
    try:
        with open(filePath, "r") as file:
            lines = file.readlines()
        if len(lines) < 2:
            print("File must have minimum 2 lines where first one is url and second one is file name.")
            return
        
        url = lines[0].strip()          # Store the URL
        filename = lines[1].strip()     # Store the file name

        qrCode = qrcode.make(url)
        qrCode.save(filename)

        print("QR Code Generated Succesfully.")
    
    except FileNotFoundError:
        print("No file found with that name. Please Provide a valid File Path.")
    except Exception as e:
        print(f"Unexpected error : { e }.")

#  User input can be added here 
path = input("Enter the path to your input file: ")
QrCode(path)
