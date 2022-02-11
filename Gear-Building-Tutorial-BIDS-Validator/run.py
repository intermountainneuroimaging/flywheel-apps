#!/usr/bin python3
# The Shebang tell the computer what to call the file with when it runs.
# For more info:https://bash.cyberciti.biz/guide/Shebang


import flywheel_gear_toolkit
from flywheel_gear_toolkit.interfaces.command_line import exec_command
from flywheel_gear_toolkit.utils.zip_tools import unzip_archive, zip_output

# for bids pull
from flywheel import ApiException
from flywheel_bids.export_bids import download_bids_dir

import shutil
import os
import sys
from utils.singularity import mount_gear_home_to_tmp
from pathlib import Path
# import zipfile

from utils.singularity import (
    check_for_singularity,
    log_singularity_details,
    unlink_gear_mounts,
)

from utils.bids.run_level import get_run_level_and_hierarchy


# globals will be set in __main__
# FLYWHEEL_BASE = Path("/flywheel/v0")
# OUTPUT_DIR = Path(FLYWHEEL_BASE / "output")
# INPUT_DIR = Path(FLYWHEEL_BASE / "input")

def main(gtk_context):

    config=gtk_context.config
    
    #look for subject and session info...
    bids_dir = Path(FLYWHEEL_BASE / "work/bids")
    
    destination_id = gtk_context.destination["id"]
    hierarchy = get_run_level_and_hierarchy(gtk_context.client, destination_id)
    
    # download BIDS data...only download data for this session AND this subject
    bids_path = gtk_context.download_project_bids(
        target_dir=bids_dir,
        src_data=False,
        folders=['anat', 'func'],
        dry_run=False,
        subjects=[hierarchy["subject_label"]],
        sessions=[hierarchy["session_label"]],
    )
    
    # run bids validator
    # syntax: bids-validator <dataset_directory> [options]
    
    print(str(bids_path))
    os.system('ls -l '+str(bids_path))
    os.system('ls -l '+str(bids_path)+'/sub-*/*/*')
    
    from bids_validator import BIDSValidator
    
    bidsvalid = BIDSValidator().is_bids(str(bids_path))
    
    if bidsvalid:
        print('Valid BIDS format for subject "%s", session "%s"' % (hierarchy["subject_label"],hierarchy["session_label"]))
    else:
        print('Invalid BIDS format for subject "%s", session "%s"' % (hierarchy["subject_label"],hierarchy["session_label"]))
            

if __name__ == "__main__":
    #always run in a newly created "scratch" directory in /tmp/...
    scratch_dir = mount_gear_home_to_tmp()
    config_path = scratch_dir / 'config.json'
    
    os.system('whoami')
    os.system('echo '+str(scratch_dir))
    os.system('ls -l '+str(scratch_dir))

    # Decide which env is available
    use_singularity = check_for_singularity()

    # reset globals (poor form changing constants)
    global FLYWHEEL_BASE
    global OUTPUT_DIR
    global INPUT_DIR
    global SUBJECTS_DIR
    global LICENSE_FILE

    FLYWHEEL_BASE = scratch_dir
    OUTPUT_DIR = FLYWHEEL_BASE / "output"
    INPUT_DIR = FLYWHEEL_BASE / "input"

    
    with flywheel_gear_toolkit.GearToolkitContext() as gtk_context:
        return_code = main(gtk_context)

    # clean up (might be necessary when running in a shared computing environment)
    for thing in scratch_dir.glob("*"):
        if thing.is_symlink():
            thing.unlink()  # don't remove anything links point to
    shutil.rmtree(scratch_dir)
    # mkdir and removedirs is needed to not leave trailing tmp directories
    scratch_dir.mkdir()
    os.removedirs(scratch_dir)

    sys.exit(return_code)
   
