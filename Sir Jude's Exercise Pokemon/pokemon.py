print('Welcome to Pokemon Name Chain!')
def pokemon(file):
    text = open(file, 'r')
    name= text.read()
    namelist = name.split()

    highest = []
    current = []

    def firstletter(lastletter, namelist):
        for index, name in enumerate(namelist):
            if name.startswith(lastletter):
                return index
        return False

    for i in namelist:
        currentname = i
        current.append(currentname)
        pokelist = namelist[:]
        pokelist.pop(pokelist.index(currentname))
        index = firstletter(currentname[-1], pokelist)

        while index is not False:
            currentname = pokelist[index]
            current.append(currentname)
            pokelist.pop(index)
            index = firstletter(currentname[-1], pokelist)

        if len(current) > len(highest):
            highest = current

        current = []
    print(highest)

pokemon('pokemon.txt')
print('Thankyou for using our service!')
