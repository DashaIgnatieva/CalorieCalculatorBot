import sys
import os

def add_address_in_sys_path():
    # This function add an address of current working directory
    sys.path.insert(0 ,os.getcwd())