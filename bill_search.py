import re

words = ["United States Code", "Federal Register", "U.S.C.",
         "Public Law", "Private Law"]

def get_matches(words, text):
    return re.findall(r'title \d+, United States Code', text)

def count_matches(words, text):
    return sum(len(m) for m in (re.findall(w, text) for w in words))

test = '''

[Congressional Bills 113th Congress]
[From the U.S. Government Printing Office]
[H.R. 2327 Introduced in House (IH)]

113th CONGRESS
  1st Session
                                H. R. 2327

 To amend title 38, United States Code, to establish in the Department 
of Veterans Affairs a Veterans Economic Opportunity Administration, and 
                          for other purposes.
'''

print(get_matches([], test))
print(count_matches(words, test))
