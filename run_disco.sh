#show the start time
echo "Start time"
date

#install the latest disco
pip3 install disco --upgrade

#generate the jobs
python job_generator.py

#run on AWS
disco job create -n "blender_720_disco_10" -cit l -s "blender_core.py" -i "classroom_sample/job_*" -r 

#run on packet
#disco job create -n "blender_720_10" -cid 5dd58cd71bc491000d3ea2be -cit l -s "blender_core.py" -i "classroom_sample/job_*" -r

echo "End time"
date
