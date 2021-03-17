from iotpy.Device import Device, addDevice
import os
import sys
import glob

class testDevice(Device):

    def __init__(self,name):
        # You need to call constructor of Device
        Device.__init__(self,name)
	filepath = sys.argv[1]
	var1 = sys.argv[2]
	var2 = sys.argv[3]

        # adding a variables to the system
        self.addVariable(var1, "time in unix time")
        self.addVariable(var2, "Pressure inside the cryostat")
        self.addVariable("alwais_fail")

        # call loop every 2 minutes
        self.poll_loop_ms = 120*1000


	if not os.path.isfile(filepath):
		print("Filepath doesn't exist. Exiting".format(filepath))
		sys.exit()

    def loop(self):

		list_of_files = glob.glob(filepath)
		path_to_recent_file = max(list_of_files, key=os.path.getctime)

		with open(path_to_recent_file) as f:
			reader = f.readlines()
			try:
				_var1 = float(reader[-1].split(' ')[0])
				_var2 = float(reader[-1].split(' ')[1])
			except:
				print("Couldn't parse this time, passing. Are you giving me the right folder?")
				pass
			f.close()
		
        self.setVariableValue(var1, _var1)
        self.setVariableValue(var2, _var2)
 
        # status 0 and 1 are reserved, you can use status > 2
        self.setVariableStatus("alwais_fail", 2,"UKNOWN FAILURE")
        
    def write(self, name, val):
        return True

    def cleanup(self):
	pass



#IMPORTANT: You must create and add the device to the list
addDevice( testDevice("test") )

