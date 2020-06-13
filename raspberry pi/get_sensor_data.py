import sys

args = list(sys.argv)


# Flags:
# -i interval_time
# -s {[g][a][m][t][p][h]}
#    gyroscope
#    accelerometer
#    magnetometer
#    temperature
#    barometric pressure
#    humidity

if((len(args)>1) and ((args[1] == '-h') or (args[1] == '-h') or (args[1] == '-help') or (args[1] == '--h') or (args[1] == '--help'))):
    print('-i time interval of getting data from sensors (in seconds) (default is 10 seconds)')
    print('-s {[g][a][m][t][p][h]}')
    print('   gyroscope')
    print('   accelerometer')
    print('   magnetometer')
    print('   temperature')
    print('   barometric pressure')
    print('   humidity')


else:

    import json
    import time
    from sense_hat import SenseHat

    time_interval = 10

    sensors = []

    args_num = len(args)

    i = 1

    # Reading arguments
    while(i<args_num):
        if(args[i]=='-i'):
            i+=1
            time_interval = int(args[i])
        elif(args[i]=='-s'):
            i+=1
            sensor_arg = args[i]
            if('g' in sensor_arg):
                sensors.append('g')
            if('a' in sensor_arg):
                sensors.append('a')
            if('m' in sensor_arg):
                sensors.append('m')
            if('t' in sensor_arg):
                sensors.append('t')
            if('p' in sensor_arg):
                sensors.append('p')
            if('h' in sensor_arg):
                sensors.append('h')
        i+=1

    #print(time_interval)
    #print(sensors)


    '''
    gyroscope
    accelerometer
    magnetometer
    temperature
    barometric pressure
    humidity
    '''


    sense = SenseHat()

    while True:
        data = {}
        if('g' in sensors):
            data['gyroscope'] = sense.get_orientation()
        if('a' in sensors):
            data['accelerometer'] = sense.get_accelerometer()
            data['accelerometer_raw'] = sense.get_accelerometer_raw()
        if('m' in sensors):
            data['magnetometer_compass'] = sense.get_compass()
            data['magnetometer_raw'] = sense.get_compass_raw()
        if('t' in sensors):
            data['temperature'] = sense.get_temperature()
        if('p' in sensors):
            data['pressure'] = sense.get_pressure()
        if('h' in sensors):
            data['humidity'] = sense.get_humidity()


        with open("data-out/sensor_data.json", "w", encoding="UTF-8") as outfile:
            json.dump(data, outfile)

        time.sleep(time_interval)


