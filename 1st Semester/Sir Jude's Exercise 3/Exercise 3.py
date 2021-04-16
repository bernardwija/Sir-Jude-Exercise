rint('Welcome to Atom Counter!')
print('Substance List: Gold, Carbon, Hydrogen')
a=input('Please Pick Which Substance You Would Like To Count: ')
b=float(input('Please Input The Amount of '+a+' in grams: '))
if a=='Gold':
    def num_atoms(b,w):
        m=b/w
        g=m*6.022*10**23
        print('The Amount of Atoms in Your '+a+' is:',g)
    num_atoms(b,196.97)
elif a=='Carbon':
    def num_atoms(b,w):
        m=b/w
        c=m*6.022*10**23
        print('The Amount of Atoms in Your '+a+' is:',c)
    num_atoms(b,12.001)
else:
    def num_atoms(b,w):
        m=b/w
        h=m*6.022*10**23
        print('The Amount of Atoms in Your '+a+' is:',h)
    num_atoms(b,1.008)
