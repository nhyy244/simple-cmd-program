#!/usr/bin/env python3
import sys
from typing import Optional, Tuple
from src.flag_behaviours import ascii_flag_fn, default_behaviour, help_flag_fn 
from src.flag_descriptions import help_description, ascii_description
from src.flag import Flag

help_flag: Flag = Flag(help_flag_fn,"help",takes_argument=False)
ascii_flag: Flag  = Flag(ascii_flag_fn,"ascii",takes_argument=True)
help_flag.set_description(help_description)
ascii_flag.set_description(ascii_description)

flag_map = {
    "-h" : help_flag,
    "--help": help_flag,
    "-a": ascii_flag,
    "--ascii": ascii_flag
}

def extract_args(sys_args: Optional[list[str]] = []) -> Tuple[list[str]]:
    greetings:list[str] = []
    flags:list[str] = []
    for arg in sys_args:
        if arg.startswith("-"):
            flags.append(arg)
        else:
            greetings.append(arg)
    return (greetings,flags)

def parse_args(args: Tuple[list[str]]):
    greetings = args[0]
    flags = args[1]
    no_greetings = len(greetings) < 2
    
    if len(flags) == 0 and no_greetings:
        help_flag.fn()
        sys.exit()
        
    if len(flags) == 0:
        for greeting in greetings[1:]: # sys.argv will always be populated with path of program.
            default_behaviour(greeting)
        sys.exit()
    
    for flag in flags: #error checking loop
        if flag not in flag_map:
            print(f"{flag} unknown. Use -h(--help) to see supported flags")
            sys.exit()
            
        if no_greetings:
            print(flag_map[flag].description)
            sys.exit()
                
        if not flag_map[flag].takes_argument:
            flag_map[flag].fn()
            sys.exit()

    for flag in flags:
        if flag_map[flag].is_used:
            continue
        for greeting in greetings[1:]: 
            greeting = flag_map[flag].fn(greeting)
        flag_map[flag].is_used= True
    sys.exit()  
            
def main_thread():
    (greeting,flags) = extract_args(sys.argv)
    parse_args((greeting,flags))

    
