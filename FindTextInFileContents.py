import sys
import os

def findfiles(location, text):
    foundFiles = []

    for path, dirs, files in os.walk(location):                
        if files:
            for filename in files:                
                file = open(os.path.join(path, filename), 'r', encoding='UTF-8')
                if isTextInContents(file.readlines(), text):
                    foundFiles.append(filename) 

    return foundFiles

def isTextInContents(lines, text):
    for line in lines:
        if text in line:
            return True

    return False

#location = 'C:/Users/mufin02/Desktop/디에셋/SCHEMAS'
#text = '통계일'
if __name__ == '__main__':
    location = sys.argv[1]
    text = sys.argv[2]

    foundFiles = findfiles(location, text)
    print(foundFiles)
