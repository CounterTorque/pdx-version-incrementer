import sys
import argparse
 
class PDXFile:
    def __init__(self):
        self.name = ""
        self.author = ""
        self.description = ""
        self.bundleID = ""
        self.version = ""
        self.buildNumber = 0
        self.imagePath = ""
        self.launchSoundPath = ""



def read_pdx_file(file_path: str) -> PDXFile:
    pdx_file = PDXFile()

    print("Opening: " + file_path)
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'buildNumber':
                value = int(value)
            setattr(pdx_file, key, value)

    return pdx_file


def write_pdx_file(file_path: str, pdx_file: PDXFile) -> None:
    with open(file_path, 'w') as file:
        for key, value in pdx_file.__dict__.items():
            file.write(f"{key}={value}\n")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Increment a PDX version number.")
    
    parser.add_argument("-i","--input_file", help="Input file name", nargs='?')
    
    args = parser.parse_args()
    
    
    if (args.input_file == None):
        print("Please specify an input file.")
        sys.exit(1)
    
    print(args.input_file)
    pdxFile = read_pdx_file(args.input_file)
    assert(pdxFile != None)

    pdxFile.buildNumber += 1

    print("Build Number: " + str(pdxFile.buildNumber))

    write_pdx_file(args.input_file, pdxFile)

