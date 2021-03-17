from iotpy.Device import Device, addDevice
import os
import sys
import glob

class MarmotDeviceTSV2(Device):

	def __init__(self,name,path, var_name):
		# You need to call constructor of Device
		Device.__init__(self,name)
		
		# adding a variables to the system
		self.addVariable(var_name, "Pressure inside the cryostat")
		self.var_name = var_name

		# call loop every 2 minutes
		self.poll_loop_ms = 120*1000

		self.path = path
		if not os.path.isdir(self.path):
			print("Filepath " + self.path +" doesn't exist. Exiting")
			sys.exit()

	def loop(self):
		
		list_of_files = glob.glob(self.path+"/*")
		path_to_recent_file = max(list_of_files, key=os.path.getctime)
		
		_var2 = -999
		
		with open(path_to_recent_file) as f:
			reader = f.readlines()
			try:
				txt = reader[-1].replace('  ',' ')
				_var2 = float(txt.split(' ')[1])
			except Exception as e:
				print(e)
				print("Couldn't parse this time, passing. Are you giving me the right folder?")
				pass
			finally:
				f.close()

		self.setVariableValue(self.var_name, _var2)
 
	
	def write(self, name, val):
		return True

	def cleanup(self):
		pass



#IMPORTANT: You must create and add the device to the list
addDevice( MarmotDeviceTSV2("pressure", "/Data/pdata","pressure") )
addDevice( MarmotDeviceTSV2("vacuum_pressure", "/Data/vdata","vacuum_pressure") )

