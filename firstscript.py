# This little script, demonstrates how to import modules into PYTHON.
# The syntax is 'import ' followed by the name of the module.
# This scxript imports two modules, sys and string.
# Copied this script from elvis.rowan.edu/~bps/import.py
#
import sys
import string

#
# sys.platform tells you what type of system (Windows, Linux, Mac, etc.)
# sys.version tells you what version of PYTHON you are using.
#

print sys.platform
print sys.version

# 
# The following line creates a variable called up2space and gives it the value of that portion
# of the string returned by sys.version upto the first space.
#

up2space = string.find(sys.version, ' ')

#
# We create another variable called ver and give it the value of up2space.
#

ver = sys.version[:up2space]

print 'I am running PYTHON version %s on a %s platform.' % (ver, sys.platform)

dummy=raw_input()
