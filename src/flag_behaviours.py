import art 
from src.flag_descriptions import help_description

def default_behaviour(message: str):
    print(f"hello {message}")

def ascii_flag_fn(greeting: str) -> str:
    art.tprint(f"hello {greeting}", font = "random")

def help_flag_fn() -> None:
    print(help_description)
    


