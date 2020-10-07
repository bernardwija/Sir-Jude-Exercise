print('Welcome to Fahrenheit Converter')
print(' ')
def convert_temp():
    global a
    a=float(input('Please Input Degrees in Fahrenheit: '))
    return a
print('The temperature in Farenheit is:',convert_temp())

def convert_to_celcius():
    global c
    c= 5/9*(a-32)
    return c
print('The temperature in Celsius is:',convert_to_celcius())

def convert_to_kelvin():
    k= c + 273.15
    return k
print('The temperature in Kelvin is:',convert_to_kelvin())
print('Thankyou For Using Our Service!')



