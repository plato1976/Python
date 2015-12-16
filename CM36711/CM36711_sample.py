#coding: utf-8
import smbus
import time

# CM36711 command code
ALS_CONF = 0x00
ALS_THDH = 0x01
ALS_THDL = 0x02
PS_CONF1 = 0x03
PS_CONF3 = 0x04
PS_THD = 0x06
PS_DATA = 0x08
ALS_DATA = 0x09
INT_FLAG = 0x0B

DelayTime = 0.1

#ALS_Buf_Data = []
#ALS_Value

bus_number = 1
CM36711_i2c_addr = 0x60
CM36771_i2c_slave_addr = 0xC0 >> 1

bus = smbus.SMBus(bus_number)

print "hex:0x%x" % (CM36771_i2c_slave_addr)

print "Shut down ALS and disable ALS INT function."
bus.write_byte_data(CM36771_i2c_slave_addr, ALS_CONF, 0x4500) #0045

#temp =[0x45, 0x00]
#bus.write_i2c_block_data(CM36771_i2c_slave_addr, ALS_CONF, temp)

#print "Shut down PS and disable PS INT function."
time.sleep(DelayTime)
bus.write_byte_data(CM36771_i2c_slave_addr, PS_CONF1, 0x71E0) #71E0
#temp = [0x71, 0xE0]
#bus.write_i2c_block_data(CM36771_i2c_slave_addr, PS_CONF1, temp)

print "Enable ALS."
time.sleep(DelayTime)
bus.write_byte_data(CM36771_i2c_slave_addr, ALS_CONF, 0x4400) #4400
#temp = [0x00, 0x44]
#bus.write_i2c_block_data(CM36771_i2c_slave_addr, ALS_CONF, temp)

print "read ALS data"
#ALS_Buf_Data = bus.read_byte_data(CM36771_i2c_slave_addr, 0x09)
ALS_Buf_Data = bus.read_i2c_block_data(CM36771_i2c_slave_addr, 0x09, 2)
#test = bus.read_i2c_block_data(CM36771_i2c_slave_addr, 0xC1, 2)
LSB = ALS_Buf_Data[0] << 8
MSB = ALS_Buf_Data[1]
#ALS_VAL = LSB | MSB
print "LSB:0x%.4x" % LSB
print "MSB:0x%.4x" % MSB
#print "ALS_VAL:0x%.4x" % ALS_VAL
print  ALS_Buf_Data

#print "Set ALS int threshold"
#threshold_high = ALS_VAL + (ALS_VAL / 20)
#print threshold_high

#if threshold_high > 65535:
#  threshold_high = 65535

#LSB = threshold_high & 0xFF
#MSB = threshold_high >> 8
#ALS_VAL = LSB | MSB

#bus.write_byte_data(CM36771_i2c_slave_addr, ALS_THDH, ALS_VAL)

#threshold_high = ALS_VAL - (ALS_VAL / 20)
#print threshold_high

#LSB = threshold_high & 0xFF
#MSB = threshold_high >> 8
#ALS_VAL = LSB | MSB

#bus.write_byte_data(CM36771_i2c_slave_addr, ALS_THDL, ALS_VAL)  

#print "read ALS data"
#ALS_Buf_Data = bus.read_byte_data(CM36771_i2c_slave_addr, 0x08)
#ALS_Buf_Data = bus.read_i2c_block_data(CM36771_i2c_slave_addr, 0x09, 2)
#LSB = ALS_Buf_Data[0] << 8
#MSB = ALS_Buf_Data[1]
#ALS_VAL = LSB | MSB
#print "LSB:0x%.4x" % LSB
#print "MSB:0x%.4x" % MSB
#print "ALS_VAL:0x%.4x" % ALS_VAL
