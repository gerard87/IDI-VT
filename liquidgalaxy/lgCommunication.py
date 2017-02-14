import os
import time
from IDIVT.settings import BASE_DIR
import subprocess
from os.path import isfile,join

def get_galaxy_ip():
    return '10.160.100.154'

def get_password():
    return 'lqgalaxy'

def flyto(localization):
    message = "echo 'search={localization}' > /tmp/query.txt".format(localization=localization)
    comunicate(message)

def comunicate(message):
    print message
    print get_galaxy_ip()
    print ("sshpass -p '{lg_pass}' ssh lg@{lg_ip} \"{message}\"".format(message=message, lg_ip=get_galaxy_ip(), lg_pass=get_password()))

    os.system("sshpass -p '{lg_pass}' ssh lg@{lg_ip} \"{message}\"".format(message=message, lg_ip=get_galaxy_ip(), lg_pass=get_password()))

def get_server_ip():
    p = subprocess.Popen(
    	"hostname -I | rev | cut -c 2- | rev",
        shell=True,
        stdout=subprocess.PIPE)
    ip_server = p.communicate()[0]
    return ip_server

def send_single_kml(kmlFile):
    ip_server = get_server_ip()
    os.system("touch kmls.txt")
    file = open("kmls.txt", 'a')
    file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/"+ kmlFile + "\n")
    file.close()
    send_galaxy()

def write_kml(kmlFolder, tool, filename, visibility):
    print(kmlFolder)
    print(BASE_DIR)

    ip_server = get_server_ip()
    #os.system("touch kmls.txt")
    if os.path.exists("kmls.txt"):
        os.system("rm kmls.txt")
    os.system("touch kmls.txt")
    if visibility:
        file = open("kmls.txt", 'w')
        file.write("http://" + str(ip_server)[0:(len(ip_server) - 1)] +":8000/static/kml/" + filename + "\n")
        file.close()
    send_galaxy()

def send_galaxy():
    file_path = "kmls.txt"
    server_path = "/var/www/html"
    print("sshpass -p '"+ get_password() +"' scp " + file_path + " lg@" + get_galaxy_ip() +":" + server_path)
    os.system("sshpass -p '"+ get_password() +"' scp " + file_path + " lg@" + get_galaxy_ip() +":" + server_path)

def start_tour():
    message = "echo 'playtour=line' > /tmp/query.txt"
    comunicate(message)

def exit_tour():
    message = "echo 'exittour=line' > /tmp/query.txt"
    comunicate(message)
