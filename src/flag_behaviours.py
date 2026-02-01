import random
from typing import Optional
import art 
from src.flag_descriptions import help_flag_description
from src.pos_args_maps import arg_to_color_map


def default_behaviour(message: str):
    print(f"hello {message}")

def help_flag_fn() -> None:
    print(help_flag_description)

def ascii_flag_fn(argument: str, flag_argument:str = ""): 
    #print(f"argument in ascii_flag: {argument}")
    return art.text2art(f"hello {argument}", font = "random")

def color_flag_fn(argument: str, flag_argument:str = ""):
    #print(f"argument in color_flag: {argument}")
    return f"{arg_to_color_map[flag_argument]}{argument}{arg_to_color_map['default']}"



