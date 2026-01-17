#!/usr/bin/env python3
import sys
from typing import Optional, Tuple

from src.app.flags import ascii_flag, ascii_flag_description, help_flag_description,default_behaviour, help_flag 
from src.app.flag import Flag

help_flag_class = Flag(help_flag,"help",takes_argument=False)
ascii_flag_class = Flag(ascii_flag,"ascii",takes_argument=True)
help_flag_class.set_help_description(help_flag_description)
ascii_flag_class.set_help_description(ascii_flag_description())

flag_map = {
    "-h" : help_flag_class,
    "--help": help_flag_class,
    "-a": ascii_flag_class,
    "--ascii": ascii_flag_class
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
        help_flag_class.fn()
        sys.exit()
    
    if len(flags) == 0:
        for greeting in greetings[1:]: # sys.argv will always be populated with path of program.
            default_behaviour(greeting)
        sys.exit()
    for flag in flags:
        if not flag_map[flag].takes_argument: 
            flag_map[flag].fn()
            sys.exit()
        if flag not in flag_map:
                print(f"{flag} unknown. Type -h(--help) to see supported flags")
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

    
