#!/usr/bin/env python3
from enum import Enum
import sys
from art import *  
from typing import Optional, Tuple 


def greetings(message: str):
    print(f"hello {message}")
    

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

def ascii_flag(greeting: str) -> str:
    tprint(f"hello {greeting}", font = "random")
    
def extract_args(sys_args: Optional[list[str]] = []) -> Tuple[list[str]]:
    greeting:list[str] = []
    flags:list[str] = []
    for arg in sys_args:
        if arg.startswith("-"):
            flags.append(arg)
        else:
            greeting.append(arg)
    print (greeting)
    return (greeting,flags)
    
def parse_args(args: Tuple[list[str]]): #TODO refactor
    greeting = args[0]
    flags = args[1]
    if len(greeting) > 2:
        print("Only one greeting allowed")
        sys.exit()
    if "-h" in flags or "--help" in flags or len(greeting) == 1 :
        help_flag()
        sys.exit()
    if "-a" in flags or "--ascii" in flags:
        ascii_flag(greeting[1])
        sys.exit()
    if len(greeting) == 2:
        greetings(greeting[1])
        sys.exit()
        
def main_thread():
    (greeting,flags) = extract_args(sys.argv)
    parse_args((greeting,flags))

    
