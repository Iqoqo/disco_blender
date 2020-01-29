# Running Blender on Dis.co's Distributed Platform 

With over half a million downloads per month, Blender is one of the most popular, free and open-source 3D creation tools in the market today. In this sample code, we will focus on the integration of Cycles, a ray tracing based engine, on the [Dis.co](http://dis.co) and Packet platform. Dis.co is a parallelization platform that provides easy and flexible ways to scale your compute solutions by automatically offloading tasks onto servers on-demands. On the other hand, Packets is a bare-metal server solution for accessing high-performance computers in minutes. By combining the Dis.co and Packet platform, we are exploring the best of parallelization and best of high-performance bare-metal server configurations for maximal throughputs.

![Classroom Output](https://github.com/Iqoqo/disco_blender/blob/master/classroom_sample/classroom.gif "Classroom")

## A Blender-enabled Docker Image
To support Blender on Dis.co, a custom Docker image (with Blender 2.81a pre-installed) is created and linked to the dis.co account. You can preview the docker image by downloading it from the DockerHub. 

```
docker pull raymondlo84/disco_blender
```

And once completed, you can see the image with the docker command.

```
docker images

REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
raymondlo84/disco_blender   latest              a667592ba964        3 weeks ago         851MB

```
Alternatively, you can build your own with the build script inside the docker directory

```
cd docker
sh build.sh
```

## Blender Core Python Script
The core python script provides a wrapper to execute blender render program in parallel across all servers with dis.co platform. 

## Job Generator
We provide a simple script to generate a parallelized the blender rendering tasks. To run the job generator, we execute the python with your favourite IDE or at the terminal. 

```
python job_generator.py
```
By running the script, it will generate a set of data files in the classroom_sample directory.
```
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_1_1.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_2_2.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_3_3.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_4_4.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_5_5.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_6_6.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_7_7.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_8_8.txt
    8 -rw-r--r--   1 raymondlo84  staff       126 Jan 28 16:45 job_9_9.txt
    8 -rw-r--r--   1 raymondlo84  staff       128 Jan 28 16:45 job_10_10.txt
```

For example, if we look inside the job_1_1.txt, you will see 5 lines of information.

```
http://100.25.247.222/uploads/classroom_720.zip
classroom/classroom.blend
1
1
http://100.25.247.222/uploads/upload_images.php
```

The first line is the URL to the blender project, in a zip format. It is important that we package all dependencies and all other asset files inside that folder. This will be distributed across all servers in runtime. 
The second line is the path to the blender project.
The third and forth line define the range for the frames in and out. In example, job_1_1.txt will render frame 1 to 1 (yes 1 frame) from the blender project. Lastly, the last line is optional but allows user to upload the final image to a separate server. This would be useful if you want to automate or pipe information to another system. 

## How to Run (Locally)
We provided a run script that you can test the blender solution. You can test the solution by running the following script.
```
sh run_local.sh
```
This will execute the scripts on the Blender Docker image. 


## How to Run (CLI)
Once you have generated the tasks files (e.g., classroom_1_10.txt, classroom_11_20.txt, ... etc), we can now run a new job on the dis.co server with the command line interface.

1. Login with your username and password 

```
disco login 
```

2. Add and Run the job (also make note of the <job_id> for next step).

```
 disco job create -cit l -n "blender_example" -s blender_core.py -i "classroom_*.txt" -r
```

3. Monitor the job with the disco's view command: <job_id> 

```
disco job view <job_id> 
```

4. Download the results (once the job is completed)

```
disco job download-results <job_id> -d .
```

Alternatively, just execute the run script we have provided after login. 
```
sh run_disco.sh 
```

## How to Run (Dis.co Web UI)

Note: Please talk to our dis.co team and enable a dis.co account with the customized docker image.

1. Open <app.dis.co> in a Chrome browser (Currently we do not support other browsers)
2. Login to the dis.co account with your account username and password
3. Click "Create A Job" button (right corner)
4. Select (or drag and drop) the script file (e.g., **blender_core.py**)
5. Select (or drag and drop) a list of tasks (e.g., **classroom_1_10.txt**, **classroom_11_20.txt**,...)
6. Select "Large" as the Job Size from the drop down list
7. Check the "Autorun this job" checkbox
8. Click "Create Job" button


Once the job is completed, you can download individual results from the web interface. 



