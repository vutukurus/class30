import os
import subprocess


#subprocess..
print "=======================\n"
a= subprocess.call("dir",shell=True)
print a

#subprocess with status code..
a= subprocess.check_call(["dir"],shell=True)
if a != 0:
	print "Command did not executed sucesfult"
else:
	print "scuess"
	
#subprocess with output capture
b = subprocess.check_output("dir",shell=True)
print b


f= open("dump.txt","w")
f.write(b)
f.close()














