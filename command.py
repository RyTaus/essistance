"""A command wraps a user made plugin by baking it with extra functionality"""
class Command(object):
    def __init__(self, plugin):
        self.plugin = plugin

    def match(self, text):
        """Returns how good of a match a given text is"""
        pass

    def run(self):
        """Run the function contained in the plugin"""
