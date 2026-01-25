from typing import Callable


class Flag: 
    def __init__(self, fn: Callable, description: str, takes_argument:bool): 
        self.fn = fn
        self.takes_argument = takes_argument
        self.description =description
        self.is_used = False
