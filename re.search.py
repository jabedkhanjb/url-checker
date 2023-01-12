import re
url = input("URL: ").strip()
 
if match := re.search(r"^(?:https?://)?(?:www\.)?(?:twitter|github|hackerrank|linkedin|instagram|snapchat|soundcloud|youtube|facebook|replit|)\.(?:com|org|net)/(?:in/)?([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: ", match.group(1).lower())
else:
    print("Invalid URL")
  
# note of regular expressions, from CS50P course with David Malan

# reference to character classes
# \d  decimal digit 
# \D  not a decimal digit
# \s  whitespace characters 
# \S  not a whitespace character
# \w  word character ... as well as numebers and the underscore 
# \W  not a word character 


# """
# 1) .    any character except a new line
# 2) *    0 or more repetitions
# 3) +    1 or more repetitions
# 4) ?    0 or 1 repetition
# 5) {m}  m repetitions
# 6) {m,n}    m-n repetitions
# """
# """
# ^ matchs the start of the string
# $ matches the end of the string or just before the newline
#   at the end of the string

# """
# r"" The r means that the string is to be treated as a raw string,
#  which means all escape codes will be ignored. 
#  For an example: '\n' will be treated as a newline character, 
#  while r'\n' will be treated as the characters \ followed by n

#  A|B  either A or B 
#  (...)  a group 
#  (?:...)  non-capturing version

# []  set of characters
# [^] complementing the set 


# brief definiton:
# ^   means "start matching at the beginning of the string"
# w   means "any word character"
# +   means "one or more"
