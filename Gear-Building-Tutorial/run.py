#!/usr/bin python3
# The Shebang tell the computer what to call the file with when it runs.
# For more info:https://bash.cyberciti.biz/guide/Shebang

# import sys
# import zipfile
# from pathlib import Path
# import shutil

# import flywheel_gear_toolkit
# from flywheel_gear_toolkit.interfaces.command_line import exec_command
# from flywheel_gear_toolkit.utils.zip_tools import unzip_archive, zip_output

import flywheel
import shutil
import os
import sys
from utils.singularity import mount_gear_home_to_tmp

from utils.singularity import (
    check_for_singularity,
    log_singularity_details,
    unlink_gear_mounts,
)



# globals will be set in __main__
# FLYWHEEL_BASE = Path("/flywheel/v0")
# OUTPUT_DIR = Path(FLYWHEEL_BASE / "output")
# INPUT_DIR = Path(FLYWHEEL_BASE / "input")

def main(gtk_context):

    import flywheel

#    context = flywheel.GearContext()  # Get the gear context
#    config = context.config           # from the gear context, get the config settings
    config=gtk_context.config

    ## Load in values from the gear configuration
    my_name = config['my_name']
    num_rep = config['num_rep']

    ## Load in paths to input files for the gear
    message_file = gtk_context.get_input_path('message_file')

    while (num_rep > 0):                      # While the num_rep variable is greater than zero:

        print("Hello, {}!".format(my_name))   # Print "Hello Name!" every loop
        num_rep -= 1                          # Decrease the num_rep variable by one

    # Now read the custom message:
    message_file = open(message_file,'r')   # Open the file with the intent to read
    print('\n')                               # Print a blank line to separate the message from the "hello's"
    print(message_file.read())                # Read and print the file
    
    


if __name__ == "__main__":
    #always run in a newly created "scratch" directory in /tmp/...
    scratch_dir = mount_gear_home_to_tmp()
    config_path = scratch_dir / 'config.json'
    
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

#    with flywheel_gear_toolkit.GearToolkitContext(config_path='/flywheel/v0/config.json') as gtk_context:
 #       return_code = main(gtk_context)
    
    with flywheel.GearContext() as gtk_context:
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
    
