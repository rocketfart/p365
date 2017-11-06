import json
import httplib2

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

weather_client_id = "099cea65dd1709abe579314abfb87316"

def findweather(city, his=''):
    url=''
    if not his:
        #http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1
        url = ('http://api.openweathermap.org/data/2.5/weather?q=%s,uk&appid=%s' % (city, weather_client_id))

        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])

        if result:
            weather_description=result['weather'][0]['description']
            temp = result['main']['temp']
            pressure = result['main']['pressure']
            humidity = result['main']['humidity']

            weatherInfo = {'description':weather_description, 'temperature':temp, 'pressure':pressure, 'humidity':humidity}
            print 'description: %s' % weather_description
            print 'temperature: %s' % temp
            print 'pressure: %s' % pressure
            print 'humidity: %s' % humidity
            return weatherInfo
        else:
            print 'No Weather Found for %s' % city
            return 'No Weather Found for %s' % city

    elif his=='his' or 'His' or 'HIS':
        #http://www.convert-unix-time.com/api?date=2011-02-01 08:23:33&timezone=vienna
        #http: // samples.openweathermap.org / data / 2.5 / history / city?q = London, UK & appid = b1b15e88fa797225412429c1c50c122a1

        url = ('http://samples.openweathermap.org/data/2.5/history/city?q=%s,UK&appid=b1b15e88fa797225412429c1c50c122a1' % city)

        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])
        weatherInfo=['3 HOURS HISTROY:']

        if result:
            for i in result['list']:
                weather_description = i['weather'][0]['description']
                temp = i['main']['temp']
                pressure = i['main']['pressure']
                humidity = i['main']['humidity']

                weatherInfo.append({'Description': weather_description, 'Temperature': temp, 'Pressure': pressure, 'Humidity': humidity})
            print weatherInfo
            return weatherInfo

        else:
            print 'No Weather History Found for %s' % city
            return 'No Weather History Found for %s' % city

    else:
        print 'Wrong Input'
        return 'Wrong Input'


if __name__ == '__main__':
    findweather('seattle')
    #findweather('seattle')
    #findweather('redmond')





