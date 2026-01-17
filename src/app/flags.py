import art 

def default_behaviour(message: str):
    print(f"hello {message}")

def ascii_flag(greeting: str) -> str:
    art.tprint(f"hello {greeting}", font = "random")

def help_flag() -> None:
    print(
"""Usage: greeting [OPTION]... [ARG]

Print a greeting.

If ARG is provided, prints "greeting ARG".
If no ARG is given, desiplay --help text

Options:
  -h, --help              display this help and exit
  -a, --ascii string      displays the greeting in a cool way
""")

