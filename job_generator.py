#!/usr/local/bin/python3

filename = "classroom"

start = 0
end = 14
skip = 10
url = "http://100.25.247.222/uploads/classroom4k.zip"
blend_file = "classroom/classroom.blend"
for i in range (start, end):
	range_in = i*skip+1
	range_out = (i+1)*skip
	f = open("classroom_"+str(range_in)+"_"+str(range_out)+".txt", "w")
	f.write(url+"\n")
	f.write(blend_file+"\n")
	f.write(str(range_in)+"\n")
	f.write(str(range_out)+"\n")
	f.close()



