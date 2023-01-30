# https://github.com/ycaty/python-socket-server-example
import socket
import json


class boiler_client_code():
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 64433


    def fetch_fkey(self,d):
        'fetches first key ina dict'
        return [a for a in d.keys()][0]

    def send_data(self,letter ):
        '''
        letter is letter sent
        ret_data is calledback from server
        :param letter:
        :return:
        '''
        try:

            # json.dumps(letter) => makes dict_letter into str_letter
            # .encode() => makes str_letter into _bytes_letter
            letter = json.dumps(letter).encode()
            print ('client boiler letter -> ',letter)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.HOST, self.PORT))
                s.send(letter)
                ret_data = s.recv(1024)
                ret_data = json.loads(ret_data)

            return ret_data
        except Exception as e:
            print('error client_boiler', e)

        return 0