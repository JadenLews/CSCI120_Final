import csv

def __init__(self, name, dict=None):
        '''Creates profile handler.'''
        self.name = name
        self.age = dict['age']
        self.height = dict['height']
        self.weight = dict['weight']

def toCsv(self, name):
    '''Writes internal variables to CSV with a filename of the name of the profile's handler.'''
    name = name.lower()
    filename = f'{name}.csv'
    with open(filename, mode='w') as profile_file:
        profile_writer = csv.writer(profile_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Format: row is data name followed by data
        profile_writer.writerow(['age', self.age])
        #in inches
        profile_writer.writerow(['height', self.height])
        #in lbs
        profile_writer.writerow(['weight', self.weight])

    


def fromCsv(self, name):
    '''Gets dictionary containing values from CSV file and returns it.'''
    name = name.lower()
    filename = f'{name}.csv'

    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=['age','height','weight'])
    
    return csv_reader

