import re

print("\nLet's get started!\n")

'''
REGULAR EXPRESSIONS DICTIONARY
"[xyz]" - match exactly one of these characters ~ x or y or z but only one of them
"[^xyz]" - any single character except x, y or z
'''

'''
REGULAR EXPRESSIONS METHODS
re.sub replaces all of the matches, not just the first one.
re.search
re.compile
re.
'''

def plural(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + "s"

print(plural("fly"))