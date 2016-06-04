# The aim is to take regex that matches data-tx-text="(.*?)"> from file en.html and
# 1. find the first occurrence of that regex in de.html
# 2. then, copy the found occurrence from en.html to the location in de.html

import re

with open('filea.html') as originalFile:
    originalFileContents = originalFile.read()

pattern = re.compile(r'[0-9a-f]{32}_se')
originalMatches = pattern.findall(originalFileContents)

counter = 0

def replaceId(match):
    global counter
    value = match.group()
    newValue = originalMatches[counter]
    print counter, '=> replacing', value, 'with', newValue
    counter = counter + 1
    return newValue

with open('fileb.html') as targetFile:
    targetFileContents = targetFile.read()

changedTargetFileContents = pattern.sub(replaceId, targetFileContents)

new_file = open("Output.html", "w")
new_file.write(changedTargetFileContents)
new_file.close()

print 'replace complete'
