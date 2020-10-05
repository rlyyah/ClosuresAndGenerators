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
'''

# print(plural("fly"))

def match_sxz(noun):
    return re.search('[sxz]$', noun)

def apply_sxz(noun):
    return re.sub('$', 'es', noun)

def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub('$', 'es', noun)

def match_y(noun):
    return re.search('[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + "s"

rules = ((match_sxz, apply_sxz), 
        (match_h, apply_h), 
        (match_y, apply_y),
        (match_default, apply_default))

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

print(plural('fly'))

'''
Function that builds other function dynamically
Technique of using the values of outside parameters within 
a dynamic function is called 'closures'
'''

def build_match_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = \
    (
        ('[sxz]$', '$', 'es'),
        ('[^aeioudgkprt]h$', '$', 'es'),
        ('(qu|[^aeiou]y$)', 'y$', 'ies'),
        ('$', '$', 's')
    )
rules = [build_match_apply_functions(pattern, search, replace) for
        (pattern, search, replace) in patterns]

def make_word_plural(word):
    for matches_rule, apply_rule in rules:
        if matches_rule(word):
            return apply_rule(word)

some_non_plural_words = ['fly', 'dog', 'cat', 'car', 'hero', 'sex']

for word in some_non_plural_words:
    print(word, ' -> ', make_word_plural(word))

def build_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

rules = []

with open('plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 2)
        rules.append(build_and_apply_functions(pattern, search, replace))

def make_word_plural_2(word):
    for matches_rule, apply_rule in rules:
        if matches_rule(word):
            return apply_rule(word)

print('\nWITHA  FILE\n')

for word in some_non_plural_words:
    print(word, ' -> ', make_word_plural_2(word))