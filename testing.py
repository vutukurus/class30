#Unit testing file.
import jj

#crt input --> crt oupts
#wrong input --< wrin outpt
#strings.it should give error r test case failre


pass_input =  [1,2,3,4,5,6,7,8,9,10]
out_pass_list = [2,4,6,8,10]

get_new_list = jj.prime_generator(pass_input)
#Pass case.
if get_new_list == out_pass_list:
	print "Test1 passed"
else:
	print "Test1 Failed"

#Failure case:
pass_input =  [3,7,9]
out_pass_list = []
get_new_list = jj.prime_generator(pass_input)

if get_new_list == out_pass_list:
	print "Test2 passed"
else:
	print "Test2 Failed"
	
#worst case
pass_input =  ["3","6","9"]
out_pass_list = "donotpassstring"
get_new_list = jj.prime_generator(pass_input)
if get_new_list == out_pass_list:
	print "Test3 passeed"
else:
	print "Test3 failed"
	




