# https://github.com/ycaty/python-socket-server-example

# NOTE always update task_list in boiler_code when creating new functions (stay organized :) )
# This is where we write logic for the given task
# This script should be called from boiler_server_code.py
class boiler_class():
    def __init__(self):
        print ('simple sample boiler_class called from socket server')

    #input str() | output int()
    def sample_task_name(self,username):
        'returns length of given username'
        return len(username)