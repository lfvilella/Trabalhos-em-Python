from datetime import datetime
import pprint

def convert_to_am_pm(time_24:str):
    return datetime.strptime(time_24, '%H:%M').strftime('%I:%M %p')

def start_code():
    flight = {}
    with open('flight_data.csv') as data:
        ignore = data.readline()
        for line in data:
            k, v = line.strip().split(',')
            flight[k] = v
    
    flight_convert = {}
    for dest in set(flight.values()):
        flight_convert[dest.title()] = [convert_to_am_pm(key) 
                                        for key,value in flight.items() 
                                        if value == dest]

    pprint.pprint(flight_convert)

if __name__ == '__main__':
    start_code()