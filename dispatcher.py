"""Dynamically dispatces the given string to the best matched command"""
import logging

from speech_recognition import UnknownValueError


class Dispatcher(object):
    def __init__(self, commands):
        self.commands = commands

    def subscribe(self, command):
        """Add a command as a candidate to be called"""
        pass

    def dispatch(self, recognizer, audio):
        """Dispatch an event to the best subscriber"""
        text = self.recognize(recognizer, audio)
        if text is None:
            return
        for command in self.commands:
            if command.matches(text.strip()):
                command.run()

    def recognize(self, recognizer, audio):
        try:
            return recognizer.recognize_sphinx(audio)
        except UnknownValueError:
            return None
