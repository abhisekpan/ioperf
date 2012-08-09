#!/usr/bin/env python                                                                                                                                                                                                                                                      
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""Script to run Bonnie++, a file-system benchmarking tool, in different 
configurations.                                                                                                                                                                                                   
Usage: ./run_bonnie.py <config file name> <prefix for bonnie>                                                                                           
Purpose: Script to run Bonnie++, a file-system benchmarking tool, in different 
configurations. The configuration file should be a comma separated file in the
following format:
Access Mode, Run Directory, File Size(GB), Num Files, Block Size(KB), Runs
0, /tmp/bonnierun, 2, 10, 4, 20
,	,4	,10	,4	,20
1,	,2	,10	,1,

Any empty field is means that the values is same as the last given  value.   
The header is required.
Access mode: 0 = direct, anything else = buffered                                                                                                                                                                                                                                                                    
Created on Jul 2, 2012
@author: apan                                                                                                                                                                                                                 
"""
import csv
import os
import subprocess
import sys
import warnings

#constant
class MB_to_KB(int):
    def __new__(cls, *args, **kwargs):
        return  super(MB_to_KB, cls).__new__(cls, 1024)

def main():
    
    """See file description"""
    #===command line processing===
    if len(sys.argv) != 3:
        sys.stdout.write("Incorrect number of arguments. Program description:\n"
                         + __doc__)
        exit(1)
    config_file = sys.argv[1]
    bonnie_prefix = sys.argv[2]
    config_options = dict()
    #===Get system RAM info===
    try:
        meminfo = subprocess.Popen("cat /proc/meminfo | grep MemTotal",
                                   shell=True, executable="/bin/bash",
                                   stdout=subprocess.PIPE)
        ram_size = int(meminfo.communicate()[0].split(':')[1].split()[0]) / MB_to_KB()
    except:
        sys.exit("Can not read system RAM size. Exiting...")
    config_options["ram_size"]=ram_size
    bonnie = bonnie_prefix + '/sbin/bonnie++'
    outdir = '/tmp/bonnieout/'
    with open(config_file, 'rb') as f:
        reader = csv.reader(f)
        try:
            linect = 0
            for row in reader:
                linect = linect + 1
                if row[0].strip(): config_options["mode"]=row[0].strip()
                if row[1].strip(): config_options["run_dir"]=row[1].strip()
                if row[2].strip(): config_options["fsize"]=row[2].strip()
                if row[3].strip(): config_options["numf"]=row[3].strip()
                if row[4].strip(): config_options["bsize"]=row[4].strip()
                if row[5].strip(): config_options["numr"]=row[5].strip()

                if linect == 1: continue
                #===get file system
                fsinfo=subprocess.Popen(' '.join(['df -T', config_options["run_dir"]]),stdout=subprocess.PIPE,shell=True).communicate()[0]
                config_options["fs"]=fsinfo.split()[9]
                #===umount target for nfs
                if config_options["fs"] == 'nfs': 
                    if not os.geteuid()==0:
                        sys.exit("You need to be root to umount nfs target. Exiting...")   
                    else:
			mount_dir = fsinfo.split()[14]
			server_export = fsinfo.split()[8]
			if os.path.ismount(mount_dir):
			    unmount = subprocess.call(' '.join(['umount',mount_dir]), shell = True) 
			    if unmount != 0: sys.exit("Can not unmount " + mount_dir)
			mount = subprocess.call(' '.join(['mount -t nfs -o tcp', server_export, mount_dir]), shell=True)
			if mount != 0: sys.exit ("Can not mount nfs filesystem")
                        #subprocess.call('./mount_nfs.sh', shell=True)
                outfile = outdir + '_'.join([os.uname()[1],config_options["fs"],config_options["fsize"],config_options["bsize"],config_options["numf"],config_options["numr"],'.txt'])
		#===run bonnie++===
                run_list = [bonnie, '-q -f' ]
                if int(config_options["mode"]) == 0: run_list.append('-D')
                run_list.extend(['-d',config_options["run_dir"]])
                run_list.extend(['-s',''.join([config_options["fsize"],'g:',str(int(config_options["bsize"])* MB_to_KB())])])
                run_list.extend(['-n',config_options["numf"]])
                run_list.extend(['-x',config_options["numr"]])
                run_list.extend(['-m',os.uname()[1]])
                run_list.extend(['-u','apan:apan'])
                run_list.extend(['>',outfile])
                sys.stderr.write('run #'+str(linect) + ':' + ' '.join(run_list) + '\n')
                subprocess.call(' '.join(run_list), shell=True)
                #===parse output===
                subprocess.call(' '.join(['./format_out.py',outfile]), shell=True)
        except csv.Error, e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
                                                                                                       
#===end main===    

if __name__ == '__main__':
    main()
   
