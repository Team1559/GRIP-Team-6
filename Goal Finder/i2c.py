import smbus


class I2C(object):

	def __init__(self):

	    self.address = 0x5
	    self.bus = smbus.SMBus(1)


	def write(self, data):

	    data = ord(data)

	    self.bus.write_byte_data(address, data, 0)
