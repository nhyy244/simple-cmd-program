from typing import Callable


class Flag: 
    def __init__(self, fn: Callable, name: str, takes_argument:bool): 
        self.fn = fn
        self.takes_argument = takes_argument
        self.name = name
        self.description =""
        self.is_used = False
        
    def set_description(self,description):
        self.description = description