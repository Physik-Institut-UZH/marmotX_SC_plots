from iotpy.Device import Device, addDevice
import os
import sys
import glob

class MarmotDeviceTSV4(Device):

	def __init__(self,name,path):
		# You need to call constructor of Device
		Device.__init__(self,name)
		
		# adding a variables to the system
		self.addVariable("TempA", "Temp A")
		self.addVariable("TempB", "Temp B")
		self.addVariable("Heater", "Heater")

		# call loop every 2 minutes
		self.poll_loop_ms = 120*1000

		self.path = path
		if not os.path.isdir(self.path):
			print("Filepath " + self.path +" doesn't exist. Exiting")
			sys.exit()

	def loop(self):
		
		list_of_files = glob.glob(self.path+"/*")
		path_to_recent_file = max(list_of_files, key=os.path.getctime)
		
		_var1 = -999
		_var2 = -999
		_var3 = -999
		
		with open(path_to_recent_file) as f:
			reader = f.readlines()
			try:
				txt = reader[-1].replace('  ',' ')
				_var1 = float(txt.split(' ')[1])
				_var2 = float(txt.split(' ')[2])
				_var3 = float(txt.split(' ')[3])
			except Exception as e:
				print(e)
				print("Couldn't parse this time, passing. Are you giving me the right folder?")
				pass
			finally:
				f.close()

		self.setVariableValue("TempA", _var1)
		self.setVariableValue("TempB", _var2)
		self.setVariableValue("Heater", _var3)
 
	
	def write(self, name, val):
		return True

	def cleanup(self):
		pass



#IMPORTANT: You must create and add the device to the list
addDevice( MarmotDeviceTSV4("cryocon", "/Data/tdata") )

