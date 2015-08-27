'''
enhanced_unit_converter.py

Unit converter: 

Miles and Kilometers
Kilograms and Pounds
Celsius and Fahrenheit

'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kg = float(input('Enter weight in kilograms: '))
    pounds = kg * 2.205

    print('Weight in pounds: {0}'.format(pounds))

def pounds_kg():
    pounds = float(input('Enter weight in pounds: '))
    kg = pounds / 2.205

    print('Weight in kilograms: {0}'.format(kg))

def cel_fahren():
    celsius = float(input('Enter temperature in celsius: '))
    fahrenheit =  celsius* (9 / 5) + 32
    print('Temperature in fahrenheit: {0}'.format(fahrenheit))

def fahren_cel():
    fahrenheit = float(input('Enter temperature in fahrenheit: '))
    celsius = (fahrenheit - 32)*(5/9)
    print('Temperature in celsius: {0}'.format(celsius))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do? ')

    if choice == '1':
        km_miles()
    if choice == '2':
        miles_km()

    if choice == '3':
        kg_pounds()
    if choice == '4':
        pounds_kg()
        
    if choice == '5':
        cel_fahren()
    if choice == '6':
        fahren_cel()
