import sys
import tensorflow
import keras
import tensorflow.keras
from tensorflow.python.client import device_lib
import platform

#reload(sanity_tests)
    
def tests(python = True, tensor = False, system = True, devices = False):
    if system:
        print("operating system is: {} {}".format(platform.linux_distribution()[0], platform.linux_distribution()[1]))
    if python:
        print("python version is {}.{}.{}".format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
    if tensor:
        print("tensorflow version is %s" % tensorflow.__version__)
        print("keras version is %s" % keras.__version__)
        print("in-built keras version is %s" % tensorflow.keras.__version__)
    if devices:
        print("available devices: %s" % ', '.join([dev.name for dev in device_lib.list_local_devices()]))
        
def baseline():
    tests(python = True, tensor = False, system = True, devices = False)

def full():
    tests(python = True, tensor = True, system = True, devices = True)