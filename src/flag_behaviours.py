import random
from typing import Optional
import art 
from src.flag_descriptions import help_description
from src.color_maps import arg_to_color_map


def default_behaviour(message: str):
    print(f"hello {message}")

def help_flag_fn() -> None:
    print(help_description)

def ascii_flag_fn(greeting: str, flag_arguments: list[str] = [] ): 
    return art.text2art(f"hello {greeting}", font = "random")

def color_flag_fn(greeting: str, flag_arguments: list[str] = [] ):
    return

    


