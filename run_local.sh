#generate the jobs
python3 job_generator.py
#run one job locally - this will repeat exactly on disco server
docker run -it -v `pwd`:/local raymondlo84/disco_blender /local/blender_core.py /local/classroom_sample/job_1_1.txt

