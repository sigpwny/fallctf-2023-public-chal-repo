from jinja2 import Environment
from random import choice

class NinjaTemplate:

    def __init__(self, jinja_env: Environment, content: str):
        # setting up jinja stuff - nothing to see here
        self.env: Environment = jinja_env
        # example custom function that can be called in the template
        def get_ninja_name():
            names = ['Lloyd', 'Garmadon', 'Jay', 'Kai', 'Master Wu', 'Nya', 'Harumi', 
                     'Cole', 'Morro', 'P.I.X.A.L', 'Skylor']
            print('getting ninja name')
            return choice(names)
        # oh wait, what's this? why are we adding a function to open files to
        # the jinja environment?
        self.env.globals.update({ 'get_ninja_name': get_ninja_name, 'open': open })
        self.content: str = content

    def render(self, **kwargs):
        # let's render the template by directly substituting the variables!
        # what could go wrong?
        template = self.env.from_string(self.content.format_map(kwargs))
        return template.render()
    
