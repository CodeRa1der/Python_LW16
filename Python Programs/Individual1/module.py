# Модуль main.py

def outer_function(type='max'):
    def inner_function(collection):
        if type == 'max':
            return max(collection)
        else:
            return min(collection)
    return inner_function