#!/usr/local/bin/python3
import sys
import os
import requests
import pathlib
import time

ROOT_DIR = '/local'
OUT_DIR = './run-result'

#This function sends an image to a dedicated server
#The upload_images.php receives images from a POST HTTP. 
def send_data_to_server(url_post, image_path):
    image_filename = os.path.basename(image_path)
    multipart_form_data = {
        'userfile': (image_filename, open(image_path, 'rb'))
    }
    response = requests.post(url_post,
                             files=multipart_form_data)
    print(response)

#This function executes the Blender project
#range_in range_out are the first and end frame to be rendered
def run_blender(blender_file, range_in, range_out, upload_web):
    start_time = time.time()
    out_path = OUT_DIR+"/frame_#####"
    blender_exe_path = "/usr/bin/blender-2.81a-linux-glibc217-x86_64/blender"
    #we supports Blender 2.81
    command = blender_exe_path +" -b "+ "/tmp/"+ blender_file + \
    " -x 1 -o "+ out_path + " -f " + range_in + ".." + range_out + " > nul 2>&1"
    
    #run the blender command
    print(command)
    os.system(command)
    end_time = time.time()
    exec_time = end_time - start_time;
    print ("Execution Time: "+ str(exec_time))

    #exit if URL is not provided
    if upload_web == '':
        return
    #upload results to the web (optional)
    cur_dir = pathlib.Path('./run-result')
    cur_pattern = "*.*"
    for cur_file in cur_dir.glob(cur_pattern):
        print("Uploading to Server..."+str(cur_file)+"\n")
        send_data_to_server(upload_web, cur_file)


def parse_args():
    in_file = None
    try:
        in_file = sys.argv[1]
    except IndexError:
        pass

    print(f"{in_file}")
    return in_file

# main function that takes the input parameters and process the
# blender project file.
def main():
    in_file = parse_args()

    if in_file is None:
        sys.exit("please provide a Blender batch script file to start")
        return

    URL_blender = ""
    blender_file = ""
    range_in = 0
    range_out = 0

    #the batch file has to have 4 lines
    #URL to the blender project (in zip file with all dependencies)
    #name to the blender file
    #range in
    #range out
    #upload_web
    with open(in_file) as fp:
        URL_blender = fp.readline().rstrip('\n')
        blender_file = fp.readline().rstrip('\n')
        range_in = fp.readline().rstrip('\n')
        range_out = fp.readline().rstrip('\n')
        upload_web = fp.readline().rstrip('\n')
    fp.close()

    #fetch the content from the dedicated URL and extract the package
    print ("Processing "+URL_blender)
    os.system("wget -q -O /tmp/tmp.zip "+URL_blender)
    os.system("unzip /tmp/tmp.zip -d /tmp")
    
    run_blender(blender_file, range_in, range_out, upload_web)
    
    print ("Blender Processing Completed")

if __name__ == "__main__":
    main()
