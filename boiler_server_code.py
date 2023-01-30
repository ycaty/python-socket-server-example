# https://github.com/ycaty/python-socket-server-example
import json
import socket
import time
from boiler_class import boiler_class

# simple socket server boiler code ycaty 1/30/2023 all cats are yellow
# NOTE GIVEN DICT MUST BE LESS THAN 1024 BYTES/CHARS

# each time new function added, add it to task list (stay organized)
task_list = ['sample_task_name']



boily = boiler_class()

HOST = "127.0.0.1"
PORT = 64433


def sample_task_name(username):
    new_key = boily.sample_task_name(username)
    return new_key
 

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            output_letter = {'msg':'error',
                             'data':''}
            input_letter = conn.recv(1024)
            input_letter = json.loads(input_letter)  # _bytes to _dict
            input_letter_sample = {'task': 'sample_task_name','data': {'username': 'ycaty'}}



            try:
 
                error_check = 0
                #<error block> Check for errors here such as asserting required data exists for given task
  
  
                #</error block> Break from block if some sort of error found
                if error_check:
                    output_letter = json.dumps(output_letter).encode()
                    conn.send(output_letter)


                # ret str() | input(username)
                if input_letter['task'] == 'sample_task_name':
                    new_key = sample_task_name(input_letter['data']['username'])
                    output_letter['data'] = new_key
                    output_letter['msg'] = 'ok'


                else:
                    output_letter['data'] = 'task not found'



            except Exception as e:
                print ('error e ',e)

            print (input_letter)


            output_letter = json.dumps(output_letter).encode()
            conn.send(output_letter)