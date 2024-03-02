# 1)
import re

pattern = r'ab*'

test_strings = ['ac', 'abc', 'abbc', 'a', 'abb']

for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f'"{test_string}" соответствует шаблону.')
    else:
        print(f'"{test_string}" не соответствует шаблону.')
# 2)
        import re

pattern = r'ab{2,3}'

test_strings = ['ac', 'abc', 'abbc', 'abbbc', 'a', 'abb']

for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f'"{test_string}" соответствует шаблону.')
    else:
        print(f'"{test_string}" не соответствует шаблону.')
# 3)
        import re

pattern = r'[a-z]+_[a-z]+'

test_string = "this_is_a_test_string"

matches = re.findall(pattern, test_string)
print(matches)

# 4) 
import re

pattern = r'[A-Z][a-z]+'

test_string = "This is a Test String"

matches = re.findall(pattern, test_string)
print(matches)

# 5)
import re

pattern = r'a.*b$'

test_strings = ['ac', 'abc', 'abbc', 'a', 'abb']

for test_string in test_strings:
    if re.fullmatch(pattern, test_string):
        print(f'"{test_string}" соответствует шаблону.')
    else:
        print(f'"{test_string}" не соответствует шаблону.')
# 6)
        import re

pattern = r'[ ,.]'
replacement = ':'

test_string = "This is, a test. String"

new_string = re.sub(pattern, replacement, test_string)
print(new_string)
# 7)
def snake_to_camel(snake_case_string):
    parts = snake_case_string.split('_')
    return ''.join([part.capitalize() for part in parts])

snake_case_string = "this_is_snake_case_string"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)
# 8)
import re

pattern = r'[A-Z][a-z]*'

test_string = "SplitThisStringByUppercaseLetters"
matches = re.findall(pattern, test_string)
print(matches)
# 9)
import re

pattern = r'([a-z])([A-Z])'
replacement = r'\1 \2'

test_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
new_string = re.sub(pattern, replacement, test_string)
print(new_string)
# 10)
import re

def camel_to_snake(camel_case_string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()

camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)

  