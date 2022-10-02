def average(list):
    '''Find average of a list of numbers'''
    return sum(list) / float(len(list))

class FilterModule(object):
    '''Query filter'''

    def filters(self):
        return {
            'average': average
        }

