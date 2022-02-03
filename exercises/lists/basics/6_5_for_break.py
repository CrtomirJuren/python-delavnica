""" sprehodi se čez celotno ime in stopi iz for zanke, ko dosežeš črko 'u' """

ime = 'Tom Cruise'

for crka in ime:
    print(crka)
    if crka == 'u':
        print('pred break')
        break
        print('za break')

print(2*'\n')

for crka in ime:
    print(crka)
    if crka == 'u':
        print('pred continue')
        continue        
        print('za continue')