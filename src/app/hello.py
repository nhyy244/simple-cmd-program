#!/usr/bin/python3
from enum import Enum
import sys
from typing import Optional, Tuple 
print(f"Importing {__name__}")
def greetings(message: str):
    print(f"greeting {message}")

def help_flag() -> None:
    print(
"""Usage: greeting [OPTION]... [ARG]

Print a greeting.

If ARG is provided, prints "greeting ARG".
If no ARG is given, prints a default greeting.

Options:
  -h, --help     display this help and exit
""")

def ascii_flag(greeting: str) -> str:
    print(f"ASCII GRETTING: {greeting}")
    
def extract_args(sys_args: Optional[list[str]] = []) -> Tuple[str,list[str]]:
    greeting:list[str] = []
    args:list[str] = []
    for arg in sys_args:
        if not arg.startswith("-"):
            args.append(arg)
        else:
            greeting.append(arg)
    if len(greeting) > 1:
        raise Exception("Only one greeting allowed")
    else:
        greeting = greeting[0] if len(greeting) != 0 else ""
    return (greeting,args)
    
def parse_args(args: Tuple[str,list[str]]):
    greeting = args[0]
    flags = args[1]
    if greeting == "":
        greetings("from python. -h for help")
        sys.exit() 
    if "-h" in flags or "--help" in flags:
        help_flag()
        sys.exit()
    elif "-a" in flags or "-ascii" in flags:
        ascii_flag(greeting)
        sys.exit()

def main_thread():
    if len(sys.argv) > 1:
        greetings(sys.argv[1])
    else:
        greetings("from python. -h for help")

    
        
         