
import TeelSys_SHT.SHT31 as SHT31

with SHT31.SHT31() as sht31:
    # print sht31.check_heater_status()
    # sht31.turn_heater_on()
    # print sht31.check_heater_status()
    # sht31.turn_heater_off()
    # print sht31.check_heater_status()
    # temperature, humidity = sht31.get_temp_and_humidity()
    # print "Temperature: %s" % temperature
    # print "Humidity: %s" % humidity
    print("Temperature: %s"%sht31.read_temperature())
    print("Humidity: %s"%sht31.read_humidity())