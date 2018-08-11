"""
Entry point of the application. Loads the plugins and start the listening
background thread.
"""
import os
import importlib
import logging
import time

import speech_recognition as sr

from dispatcher import Dispatcher
from command import Command


def is_plugin(module):
    INTERFACE = ['name', 'command', 'run']
    for function in INTERFACE:
        if not hasattr(module, function):
            return False
    return True


def load_plugins(path):
    """Load plugin files into Commands"""
    commands = []
    for filename in os.listdir(path):
        if not filename.endswith('.py'):
            continue

        importname = '{}.{}'.format(path, filename[:-3])
        plugin = importlib.import_module(importname, __file__)
        if is_plugin(plugin):
            commands.append(Command(plugin))
    return Dispatcher(commands)


def start(dispatcher):
    """Spin up the listening thread and run speach into dispatcher"""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
    
    recognizer.listen_in_background(microphone, dispatcher.dispatch)


def end():
    """Join up all the threads and flush everything"""
    pass


def hang():
    """Don't exit python"""
    for _ in range(100):
        time.sleep(.5)
    # input('Press Enter to Exit')


def main():
    dispatcher = load_plugins('plugins')
    start(dispatcher)
    hang()
    end()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
