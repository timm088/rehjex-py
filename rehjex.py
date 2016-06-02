# The aim is to take regex that matches data-tx-text="(.*?)"> from file en.html and
# 1. find the first occurrence of that regex in de.html
# 2. then, copy the found occurrence from en.html to the location in de.html

import re

with open('filea.html') as originalFile:
    originalFileContents = originalFile.read()

pattern = re.compile(r'(................................)_se')
originalMatches = pattern.findall(originalFileContents)

counter = 0

def replaceId(match):
    global counter
    value = match.group()
    newValue = originalMatches[counter] + '_se'
    print counter, '=> replacing', value, 'with', newValue
    counter = counter + 1
    return newValue

with open('fileb.html') as targetFile:
    targetFileContents = targetFile.read()

changedTargetFileContents = pattern.sub(replaceId, targetFileContents)

print changedTargetFileContents
