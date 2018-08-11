"""A command wraps a user made plugin by baking it with extra functionality"""
class Command(object):
    def __init__(self, plugin):
        self.name = plugin.name()
        self.command = plugin.command()
        self.run = plugin.run

    def matches(self, text):
        """Returns how good of a match a given text is"""
        return text == self.command

    def run(self):
        """Run the function contained in the plugin"""
        self.run()
