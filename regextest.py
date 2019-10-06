import re
pattern=r'mazin'
sequence='mazin el khatib'
if re.match(pattern,sequence):
    print('match')
else:
    print('notmatch')
#****match
pattern=r'Mazin'
sequence='mazin el khatib'
if re.match(pattern,sequence):
    print('match')
else:
    print('notmatch')
#***nomatch 
result=re.match(r'AV','AV anlalyze pattern AV')
print(result)
print(result.group(0))
#*****re.Match object; span=(0, 2), match='AV'>
#****AV
result=re.match(r'analyze','AV analyze pattern AV')
print(result)
#****none
result=re.search(r'\d+','aaa1f 843hh')
print(result.group())
patterns = [ 'this', 'that' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text),end='@')

    if re.search(pattern,  text):
        print ('found a match!')
    else:
        print( 'no match')
result=re.findall(r'\b[ae^iouAEIOU]\w+','AV is largest Analytics community  amor of India')
print(result)