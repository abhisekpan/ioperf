#!/usr/bin/env python                                                                                                                                                                                                                                                      
"""Script to run Bonnie++, a file-system benchmarking tool, in different configurations .                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                
Usage: ./run_bonnie.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                
Purpose: Script to run Bonnie++, a file-system benchmarking tool, in different configurations   
                                                                                                                                                                                                                                                                    
Created on Jul 2, 2012

@author: apan                                                                                                                                                                                                                 
"""
import subprocess

def main():
    
    """See file description"""
    
    # Run Bonnie++
    subprocess.call(['./bonnie.sh'])
#===end main===    

if __name__ == '__main__':
    main()