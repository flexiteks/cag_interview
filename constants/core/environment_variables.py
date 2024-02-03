from os import environ

############################
#     Flask debug mode     #
############################
debug_mode = environ.get('DEBUG_MODE')

if debug_mode == 'True':
    debug_mode = True
else:
    debug_mode = False

