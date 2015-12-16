import smbus

i2c = smbus.SMBus(1)
addr = 0x60
reg = 0x01
val = 0x11
i2c.write_byte_data(addr, reg, val)
print i2c.read_byte_data(addr,reg)
