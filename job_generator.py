#!/usr/local/bin/python3

start = 0
end = 10
skip = 1
job_name = "classroom_sample/job_"

#url = "http://100.25.247.222/uploads/classroom4k.zip"
url = "http://100.25.247.222/uploads/classroom_720.zip"

blend_file = "classroom/classroom.blend"
#upload_web = "http://100.25.247.222/uploads/upload_images.php"
upload_web = "" 

for i in range (start, end):
	range_in = i*skip+1
	range_out = (i+1)*skip
	f = open(job_name+str(range_in)+"_"+str(range_out)+".txt", "w")
        print("File written: "+job_name+str(range_in)+"_"+str(range_out)+".txt")
	f.write(url+"\n")
	f.write(blend_file+"\n")
	f.write(str(range_in)+"\n")
	f.write(str(range_out)+"\n")
	f.write(str(upload_web)+"\n")
	f.close()

