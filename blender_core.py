#!/usr/local/bin/python3
import sys
import os
import requests
import pathlib

ROOT_DIR = '/local'
OUT_DIR = './run-result'

def send_data_to_server(image_path):
    image_filename = os.path.basename(image_path)
    url_post = 'http://100.25.247.222/uploads/upload_images.php'
    multipart_form_data = {
        'userfile': (image_filename, open(image_path, 'rb'))
    }
    response = requests.post(url_post,
                             files=multipart_form_data)
    print(response)

def run_blender(blender_file, range_in, range_out):
    out_path = OUT_DIR+"/frame_#####"
    #we supports Blender 2.81
    command = "/bin/blender-2.81-linux-glibc217-x86_64/blender -b --verbose 0 "+ "./tmp/"+ blender_file + \
    " -x 1 -o "+ out_path + " -f " + range_in + ".." + range_out + " > nul 2>&1"
    
    #run the blender command
    print(command)
    os.system(command)

    #upload results to the web (optional)
    cur_dir = pathlib.Path('./run-result')
    cur_pattern = "*.*"
    for cur_file in cur_dir.glob(cur_pattern):
        print("Uploading to Server..."+str(cur_file)+"\n")
        send_data_to_server(cur_file)


def parse_args():
    in_file = None
    try:
        in_file = sys.argv[1]
    except IndexError:
        pass

    print(f"{in_file}")
    return in_file

# main
def main():
    in_file = parse_args()

    if in_file is None:
        print("please provide a blender batch script file to start")
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

    with open(in_file) as fp:
        URL_blender = fp.readline().rstrip('\n')
        blender_file = fp.readline().rstrip('\n')
        range_in = fp.readline().rstrip('\n')
        range_out = fp.readline().rstrip('\n')
    fp.close()

    print ("Processing "+URL_blender)
    os.system("wget -q -O tmp.zip "+URL_blender)
    os.system("unzip tmp.zip -d ./tmp")
    
    run_blender(blender_file, range_in, range_out)
    
    print ("Blender Processing Completed")

if __name__ == "__main__":
    main()
