from typing import Callable


class Flag: 
    def __init__(self, fn: Callable, description: str, takes_arguments:bool): 
        self.fn = fn
        self.takes_arguments = takes_arguments
        self.positional_args = []
        self.description =description
        self.is_used = False
        self.pos_arg_map = {}
