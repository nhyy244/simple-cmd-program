#!/usr/bin/env python3
import sys
from typing import Optional, Tuple

from src.app.flags import ascii_flag, default_behaviour, help_flag 
from src.app.flag import Flag

help_flag_class = Flag(help_flag,is_active=False)
ascii_flag_class = Flag(ascii_flag,is_active=True)

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
    
    if len(flags) == 0 and len(greetings) == 1: # sys.argv will always be populated with path of program.
        help_flag_class.fn()
        sys.exit()
    
    if len(flags) == 0:
        for greeting in greetings[1:]:
            default_behaviour(greeting)
        sys.exit()
    
    for flag in flags: 
        if flag not in flag_map:
                print(f"{flag} unknown. Type -h(--help) to see supported flags")
                sys.exit()
        if not flag_map[flag].is_active:
            flag_map[flag].fn()
            sys.exit()
            
    for flag in flags:
        for greeting in greetings[1:]:
            flag_map[flag].is_used = False
            if flag in flag_map:
                if not flag_map[flag].is_used: #only checking active flags now
                    greeting = flag_map[flag].fn(greeting)
                    flag_map[flag].is_used = True
    sys.exit()  
            
def main_thread():
    (greeting,flags) = extract_args(sys.argv)
    parse_args((greeting,flags))

    
