import scheduling_module
import os


class Schedule:
    '''Principal Class'''

    def __init__(self):
        self.oSchedule = scheduling_module.Schedule_module()
        print('Schedule your appointments')
        while True: 
            option = input(
                'Enter:\n0: to go out\n1: to save a new appointment\n2: to load all appointments\n3: to delete\n')
            if option == '0':
                # if your system is windows will run 'cls' else will run 'clear'
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif option == '1':
                self.add()
            elif option == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                self.oSchedule.load()
            elif option == '3':
                self.delete()
            else:
                print('Option not accepted, enter again\n\n')
                continue

    def delete(self):
        option = input('Enter with id that you want to delete\n')
        self.oSchedule.delete(option)

    def add(self):
        date = input('\nEnter with the date of your appointment(MM/DD/YYYY): ')
        appoint = input('Enter your appointment: ')
        self.oSchedule.save(date, appoint)
        print(f'Appointment for {date} was saved successfully\n')


s = Schedule()
