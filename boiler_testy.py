# https://github.com/ycaty/python-socket-server-example
from boiler_client_code import boiler_client_code




client = boiler_client_code()

# must be dict
letter = {'task':'sample_task_name',
          'data':{'username':'ycaty'}
           }

letter_back = client.send_data(letter)
print (letter_back)


