
import TeelSys_SHT.SHT21 as SHT21

with SHT21.SHT21(1) as sht21:
    print "Temperature: %s"%sht21.read_temperature()
    print "Humidity: %s"%sht21.read_humidity()