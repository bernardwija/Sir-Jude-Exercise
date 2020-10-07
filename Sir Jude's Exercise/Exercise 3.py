print('Welcome to Atom Counter!')
print('Substance List: Gold, Carbon, Hydrogen')
a=input('Please Pick Which Substance You Would Like To Count: ')
b=float(input('Please Input The Amount of '+a+' in grams: '))
if a=='Gold':
    def num_atoms():
        g=b/196.97*6.022*10**23
        return g
    print('The Amount of Atoms in Your '+a+' is:',num_atoms())
elif a=='Carbon':
    def num_atoms():
        g=b/12.001*6.022*10**23
        return g
    print('The Amount of Atoms in Your '+a+' is:',num_atoms())
else:
    def num_atoms():
        g=b/1.008*6.022*10**23
        return g
    print('The Amount of Atoms in Your '+a+' is:',num_atoms())


