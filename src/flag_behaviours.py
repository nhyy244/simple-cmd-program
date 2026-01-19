import art 

def default_behaviour(message: str):
    print(f"hello {message}")

def ascii_flag_fn(greeting: str) -> str:
    art.tprint(f"hello {greeting}", font = "random")

def ascii_flag_description() -> str:
    return""" 
-a(--ascii) string 
Takes a string and transforms it into ascii art
    """

def help_flag_fn() -> None:
    help_description = """Usage: greeting [OPTION]... [ARG]

Print a greeting.

If ARG is provided, prints "greeting ARG".
If no ARG is given, desiplay --help text

Options:
  -h, --help              display this help and exit
  -a, --ascii string      displays the greeting in a cool way
"""
    print(help_description)
    

def help_flag_description() -> str:
    return """
Usage: greeting [OPTION]... [ARG]

Print a greeting.

If ARG is provided, prints "greeting ARG".
If no ARG is given, desiplay --help text

Options:
  -h, --help              display this help and exit
  -a, --ascii string      displays the greeting in a cool way
"""


