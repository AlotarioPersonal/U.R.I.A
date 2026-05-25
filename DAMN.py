'''

   D.A.M.N (Docked Application MaNager)

   Version 0.1, 2026-5-24

   Secondary silent partner system to URIA, focused on numpad input commands over claps. Used to activate specific plugins by number, modulation the plugin system of URIA to individual scripts.
   Whereas URIA will load a set list of plugins automatically in one big giant list, DAMN will load individual plugins in the order you punch them in.
   

   REQUIRED PACKAGES:

'''

print("""D.A.M.N SYSTEM""")

import os
commandstr = ""


while True:
	try:
		xrequire = input("DAMN ~$:")
		if xrequire=="0":
			exit()
		else:
			commandstr = ("python plugins/" + str(xrequire) + ".py")
			os.system(f"x-terminal-emulator -e '{str(commandstr)}'")
	finally:
		print('TASK COMPLETE')
