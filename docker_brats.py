#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    Master Script for all Tumor segmentation tasks in Docker
    Should work on Unix operating systems, not yet tested on Win.
    Produces a new subfolder for every dataset which contains the
    segmented volume(s) and is named after the docker container that
    created the segmented volume(s).
"""
__version__ = '0.1'
__author__ = 'Christoph Berger'

import os
import errno
import subprocess
import argparse
#import time

#Specify title and commands for the container
#TODO: add list of all available containers
arguments = ['/runTumorSegm', '--flair', 'subject/fla.nii', '--t1c', 'subject/t1c.nii', '--t2', 'subject/t2.nii', '--t1', 'subject/t1.nii', '--o', 'subject/results', '--threads', '8']
container = 'mikaelagn/magnrbm'

#parse arguments for input, output directories and flags
parser = argparse.ArgumentParser()
parser.add_argument('directory', help='Run all available containers with the this base directory', action='store')
args = parser.parse_args()

#Arranging paths
directory = os.path.abspath(args.directory)


def rename_folder(name, folder):
    """Renames the results folder to the name of the docker container used to create it"""
    name.replace('/', '-')
    name.replace('\\', '-')
    os.renames(os.path.join(folder, 'results'), os.path.join(folder, name))

def run_container(name, command_args, folder):
    """Runs the specified image (name) using a call to shell with docker with the passed command arguments"""
    try:
        os.makedirs(os.path.join(folder, 'results'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    print('Calling Container: ', name)
    #start = time.time()
    subprocess.call(['docker', 'run', '-v', folder + ':/subject', '-i', '-t', name]+command_args)
    #end = time.time()
    print('Container run successful')
    #print 'This run took', (end-start), 'seconds.'
    rename_folder(name, folder)

#looks for subfolders containing "brats" and passes them to the run-container function
#TODO: Implement checks to ensure file format conformity 
print('Looking for BRATS data directories..')
for fn in os.listdir(directory):
    if not os.path.isdir(os.path.join(directory, fn)):
        continue # Not a directory
    if 'brats' in fn:
        print('Found pat data: ', fn)
        #TODO: add loop here to run all available containers
        run_container(container, arguments, os.path.join(directory, fn))   # Call container and pass patient directory
