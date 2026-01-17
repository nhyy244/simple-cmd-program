class Flag: 
    def __init__(self, fn: callable, name: str, takes_argument:bool): 
        self.fn = fn
        self.takes_argument = takes_argument
        self.is_used = False
        self.name = name
        self.description =""
        
    def set_help_description(self,description):
        self.description = description
        
    def get_help_description(self):
        return self.description