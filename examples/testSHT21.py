
import SHT.SHT21 as SHT21
import smbus
import fcntl

bus=smbus.SMBus(2)
with SHT21.SHT21(bus) as sht21:
    print ("Temperature: %s"%sht21.read_temperature())
    print ("Humidity: %s"%sht21.read_humidity())

