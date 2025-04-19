'''Class to manipulate the json file.
    This class there are functions to load the json record, manipulate and save. 
'''

import json
import os

class Schedule_module:
    def __init__(self):
        self.name_file = 'schedule.json'
        
    def load(self):
        if self.is_empty():
            return print('No appointments saved yet.\n')
        try:
            with open(self.name_file, encoding='utf-8') as opened:
                json_file = json.load(opened)
                print('Your appointments saved are:')
                for id, appointments in json_file.items():
                    print(f'id : {id}, day: {appointments[0]}, appointment: {appointments[1]}')
                print()
        except Exception as err:
                print(f'Unexpected {err=}, {type(err)=}')
        else:
            return json_file

    def save(self, date = str, appointments = str):
        with open(self.name_file, encoding='utf-8') as opened:
            if self.is_empty():
                file = {1: [date, appointments]}
            else:
                file = json.load(opened)
                new_file = {len(file)+1: [date, appointments]}
                file.update(new_file)
        with open(self.name_file, 'w', encoding='utf-8') as opened:
            json.dump(file, opened, indent=4)

    def delete(self, id):
        try:
            with open(self.name_file, encoding='utf-8') as opened:
                file = json.load(opened)
                deleted_file = file[id]
                del file[id]
            with open(self.name_file, 'w', encoding='utf-8') as opened:
                json.dump(file, opened, indent=4)
                print(f'File {deleted_file} deleted!')
        except KeyError:
            print('id entered doesn\'t exits!')

    def is_empty(self):
        with open(self.name_file, encoding='utf-8') as opened:
            file = json.load(opened)
            if file == {}:
                return True
        # os.path.isfile(self.name_file)
        return os.path.getsize(self.name_file) == 0
