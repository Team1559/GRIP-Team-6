import smbus
import thread


#add encode method to encode data to UTF-8 string so the arduino can read it???????
#necessary to encode if it goes right to the roborio


class I2C(object):

	def __init__(self):

	    print "init"

	    self.address = 0x08
	    self.bus = smbus.SMBus(1)


	def write(self, x):

	    data = x
	    #print x

	    try:
		#print "werk"
	    	self.bus.write_byte_data(self.address, 0, int(data))
	    except:
		pass
		#i2c gets i/o errors a lot


	def fixData(self, x):

		#method to make data a 6 byte string
		data = x
		#print x

		if data > 0:
			#data is postive

			if data < 10.00:
				#data is 4 characters
				data = str(data)
				data = data + "00"
				return data

			elif data > 10.00:
				#data is 5 characters
				data = str(data)
				data = data + "0"
				return data

			else:
				print "something went wrong with your data"
				#raise dataError

		elif data < 0:
			#data is negative

			if data < 10.00:
				#data is 5 characters
				data = str(data)
				data = data + "0"
				return data

			elif data > 10.00:
				#data is already 6 characters
				data = str(data)
				return data

			else:
				print "something went wrong with your data"
				#raise dataError

		elif data == -1000:
			#no angle is found and angle already has 6 digits
			data = str(data)
			return data

		else:
			print "something with your data is seriously messed up"
			#raise dataError



	def encode(data):

	    x = data

	    #make UNICODE string ASCII using UTF-8 string encoding

	    return data




def startServer():

	putData(-1000)

	global i2c
	i2c = I2C()

	thread.start_new_thread(run, ())
	print "server started"



def run():

	while(1):

		fixedData = i2c.fixData(angle)
		#print fixedData
		i2c.write(fixedData)



def putData(x):

	global angle

	angle = x


