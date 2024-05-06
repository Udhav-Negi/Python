import re
pattern = r"[A-Z]+yclone"
text = '''
    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi archiwastecto beatae vitae dicta sunt explicabo. Nemo enim ipsam volwasuptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magnCyclonei dolores eos qui ratione Dyclone
'''

# match = re.search(pattern, text)
matches = re.finditer(pattern, text)
for match in matches:
    print(type(match.span()))