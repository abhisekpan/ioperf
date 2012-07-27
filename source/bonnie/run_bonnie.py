#!/usr/bin/env python                                                                                                                                                                                                                                                      
"""Script to run Bonnie++, a file-system benchmarking tool, in different 
configurations.                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                
Usage: ./run_bonnie.py <config file name>                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                
Purpose: Script to run Bonnie++, a file-system benchmarking tool, in different 
configurations.   
                                                                                                                                                                                                                                                                    
Created on Jul 2, 2012
@author: apan                                                                                                                                                                                                                 
"""
import subprocess
import sys
import warnings

def main():
    """See file description"""
    #===command line processing===                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    if len(sys.argv) != 2:
        sys.stdout.write("Incorrect number of arguments. Program description:\n"
                         + __doc__)
        exit(1)
    config_file = sys.argv[1]
    #===Parsing functions===
    IsDefault = lambda line: line.startswith("defaults:")
    IsRunConfig = lambda line: line.startswith("run")
    IsEnd = lambda line: line.startswith("===")
    #===Initialize===
    MB_to_KB = 1024
    run_count = 0
    default_count = 0
    entry_type = None
    valid_params = dict([('mount_dir', '-d'), 
                        ('file_size', '-s'), 
                        ('num_files', '-n'), 
                        ('output_file', ' '), 
                        ('output_label', '-m'), 
                        ('ram_size', '-r'), 
                        ('num_processes', '-p'),
                        ('buffered_io', '-b')])
    # populate the mount directory, which is essential sort of
    default_params = dict([('mount_dir', '/mnt/nfs')])
    # try to get the system ram
    try:
        meminfo = subprocess.Popen("cat /proc/meminfo | grep MemTotal", 
                                   shell=True, executable="/bin/bash", 
                                   stdout=subprocess.PIPE)
        ram_size = int(meminfo.communicate()[0].split(':')[1].split()[0]) / MB_to_KB
    except:
        pass
    else:
        sys.stderr.write("Memory size in MB: %d\n" % ram_size)
        default_params["ram_size"]=ram_size   
    run_params = default_params.copy()    
    #===Read file===
    sys.stderr.write("reading configuration file: %s\n" % config_file)
    with open(config_file, 'r') as src:
        for line in src:
            if IsDefault(line):
                entry_type = "default"
                default_count = default_count + 1
                if default_count >=2:
                    warnings.warn("Defaults declared more than once")
            elif IsRunConfig(line):      
                    entry_type="run"
                    run_count = run_count + 1
                    run_params = default_params.copy()       
            elif IsEnd(line):    
                if entry_type == "run":
                    #Run bonnie++
                    sys.stderr.write("Running Bonnie++, run count: %d\n" % 
                                     run_count)
                    run_list = ['./bonnie.sh -q']
                    outfile = None
                    try:
                        for key in run_params:
                            if key == 'output_label':
                                run_params[key] = (run_params[key] + '_' + 
                                str(run_count))
                            elif key == "buffered_io":
                                if int(run_params[key]) != 0:
                                    run_list.append(valid_params[key])
                                continue  
                            elif key == 'output_file':
                                outfile = run_params[key]
                                continue                   
                            run_list.extend([valid_params[key], run_params[key]])
                    except KeyError:
                        sys.stderr.write("Aborting run %d, invalid configuration \
                        parameter %s" %run_count %key)
                    else:        
                        if outfile:
                            run_list.extend([' >> ', outfile])
                        subprocess.call(''.join(run_list), shell=True)
            else:
                tokens = line.split('=')
                if tokens[0] not in valid_params:
                    sys.stderr.write("Invalid parameter name %s in config file"
                                 %tokens[0])
                else:
                    if entry_type=="default":
                        default_params[tokens[0].strip()] = tokens[1].strip()
                    else:    
                        run_params[tokens[0].strip()] = tokens[1].strip()                                                                                                        
#===end main===    

if __name__ == '__main__':
    main()
    
    