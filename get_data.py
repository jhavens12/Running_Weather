import credentials
import requests
from pprint import pprint
import datetime

wu_key = credentials.wu_key
my_lat = credentials.my_lat
my_long = credentials.my_long

UTC_adjust = datetime.timedelta(hours=4)

def format_time(date_input,UTC_adjust,time):
    temp_date = date_input+" "+time
    datetime_object = datetime.datetime.strptime(temp_date, "%Y-%m-%d %I:%M:%S %p")
    return datetime_object - UTC_adjust

def twilight(date_input):
    sunrise_dict = {}
    url = "https://api.sunrise-sunset.org/json?lat="+my_lat+"&lng="+my_long+"&date="+date_input
    try:
        sunrise_data = requests.get(url).json()
    except:
        print("error getting astro data")
    sunrise_dict['astronomical_twilight_begin'] = format_time(date_input,UTC_adjust,sunrise_data['results']['astronomical_twilight_begin'])
    sunrise_dict['nautical_twilight_begin'] = format_time(date_input,UTC_adjust,sunrise_data['results']['nautical_twilight_begin'])
    sunrise_dict['civil_twilight_begin'] = format_time(date_input,UTC_adjust,sunrise_data['results']['civil_twilight_begin'])
    sunrise_dict['sunrise'] = format_time(date_input,UTC_adjust,sunrise_data['results']['sunrise'])
    return sunrise_dict

def forecast_me():
    forecast_dict = {}
    term = 'hourly10day'
    url = "http://api.wunderground.com/api/"+wu_key+"/"+term+"/q/VT/Essex.json"
    try:
        hforecast = requests.get(url).json()
    except:
        print("error getting weather data")

    for hour in hforecast['hourly_forecast']:
        if hour['FCTTIME']['hour_padded'] == '05':# or hour['FCTTIME']['hour_padded'] == '17':
            if hour['FCTTIME']['weekday_name'] == 'Tuesday' or hour['FCTTIME']['weekday_name'] == 'Thursday':

                temp_date = hour['FCTTIME']['year'] +"-"+ hour['FCTTIME']['mon'] +"-"+ hour['FCTTIME']['mday']
                temp_time = hour['FCTTIME']['hour_padded'] +":"+ hour['FCTTIME']['min']+":"+"00"
                date_key = datetime.datetime.strptime(temp_date+" "+temp_time, '%Y-%m-%d %H:%M:%S')

                forecast_dict[date_key] = {}
                forecast_dict[date_key]['twilight'] = twilight(temp_date)
                forecast_dict[date_key]['time'] = hour['FCTTIME']
                del forecast_dict[date_key]['time']['UTCDATE']
                forecast_dict[date_key]['weather'] = hour
                del forecast_dict[date_key]['weather']['FCTTIME']

    return forecast_dict
