"""Dynamically dispatces the given string to the best matched command"""
class Dispatcher(object):
    def __init__(self, commands):
        pass

    def subscribe(self, command):
        """Add a command as a candidate to be called"""
        pass

    def dispatch(self, text):
        """Dispatch an event to the best subscriber"""
        pass
