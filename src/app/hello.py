#!/usr/bin/env python3
import sys
from typing import Optional, Tuple

from src.app.flags import ascii_flag_fn, ascii_flag_description, help_flag_description,default_behaviour, help_flag_fn 
from src.app.flag import Flag

help_flag = Flag(help_flag_fn,"help",takes_argument=False)
ascii_flag = Flag(ascii_flag_fn,"ascii",takes_argument=True)
help_flag.set_help_description(help_flag_description)
ascii_flag.set_help_description(ascii_flag_description())

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
    
    if len(flags) == 0 and len(greetings) < 2: 
        help_flag.fn()
        sys.exit()
    
    if len(flags) == 0:
        for greeting in greetings[1:]: # sys.argv will always be populated with path of program.
            default_behaviour(greeting)
        sys.exit()
    
    for flag in flags:
        if flag not in flag_map:
                print(f"{flag} unknown. Type -h(--help) to see supported flags")
                sys.exit()
        if not flag_map[flag].takes_argument: 
            flag_map[flag].fn()
            sys.exit()

        #TODO: when writing flag_name --help (or -h) print flag_description
        #TODO: 
        if len(greetings) < 2:
                print(flag_map[flag].get_help_description())
        
        for greeting in greetings[1:]:
            if not flag_map[flag].is_used: 
                greeting = flag_map[flag].fn(greeting)
                flag_map[flag].is_used = True 
    sys.exit()  
            
def main_thread():
    (greeting,flags) = extract_args(sys.argv)
    parse_args((greeting,flags))

    
