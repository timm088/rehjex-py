# might be able to make this better by auto matching file names and directories


import re
import ntpath
import os.path

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def replaceIdsInFiles(originalFilePath, targetFileFolder):
    with open(originalFilePath) as originalFile:
        originalFileContents = originalFile.read()

    pattern = re.compile(r'(................................)_se')
    originalMatches = pattern.findall(originalFileContents)

    counter = 0

    def replaceId(match):
        global counter
        value = match.group()
        newValue = originalMatches[counter]+'_se'
        print counter, '=> replacing', value, 'with', newValue
        counter = counter + 1
        return newValue

    with open(os.path.join(targetFileFolder, path_leaf(originalFilePath))) as targetFile:
        targetFileContents = targetFile.read()

    changedTargetFileContents = pattern.sub(replaceId, targetFileContents)

    print changedTargetFileContents


replaceIdsInFiles("./filea.html", "./de")
