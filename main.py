import requests
import sys
import calendar

running = True

api_key = '301539f4a9f002b08bd4df659a6e96f6'
api_call = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key

print('5 day weather forecast application !')
print('')

name = input("What is your name? ")

city = input('Hi ' + name + '! Please input the city name: ')
api_call += '&q=' + city

# Stores the Json response
json_data = requests.get(api_call).json()

response = requests.get(api_call)

if response.status_code == 200:
    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }

    print('\n{city}, {country}'.format(**location_data))
    print('')

    current_date = ''

    # Iterates through the array of dictionaries named list in json_data
    for item in json_data['list']:
        time = item['dt_txt']
        next_date, hour = time.split(' ')

        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print('-----------------------------------')
            print('\n{m}/{d}/{y}'.format(**date))

            # Grabs the first 2 integers from our HH:MM:SS string to get the hours
        hour = int(hour[:2])

        # Sets the AM (ante meridiem) or PM (post meridiem) period
        if hour < 12:
            if hour == 0:
                hour = 12
                meridiem = 'Midnight'
                print('')

            else:
                meridiem = 'AM'

        else:
            if hour > 12:
                hour -= 12
                meridiem = 'PM'

            else:
                meridiem = 'Noon'

        print('\n-- %i:00 %s' % (hour, meridiem))
        # Temperature is measured in Kelvin
        temperature = item['main']['temp']
        humidity = str(item['main']['humidity'])
        pressure = str(item['main']['pressure'])

        # Weather condition
        description = item['weather'][0]['description'],

        # Prints the description as well as the temperature in Celcius and Farenheit
        print('Farenheit:   %.2f' % (temperature * 9 / 5 - 459.67))
        print('Celcius:     {:.2f}'.format(temperature - 273.15))
        print('Humidity:    ' + humidity)
        print('Pressure:    ' + pressure)
        print('Weather condition: %s' % description)

else:
    print('')
    print('City is not found!')
    print('')
    print('')
while True:
    print('')
    print('')
    running = input('Do you want to continue? ')
    if running.lower() == 'yes' or running.lower() == 'y':
        print('Great!')
        break
    elif running.lower() == 'no' or running.lower(
    ) == 'n' or running == 'exit':
        print('You have quit. Thank you for using the application! ')
        running = False
        break
