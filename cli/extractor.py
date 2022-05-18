#!/usr/bin/env python3

# Libraries
##############################################################################
from argparse import ArgumentParser
##############################################################################

# Global Values
##############################################################################
DESC = "This project was created to extract links in a given file"
##############################################################################

# Functions
##############################################################################

##############################################################################

# Main
##############################################################################
def main():
    parser = ArgumentParser(description=DESC) # Arg Parser has been created
    
    # filename argument has been added
    parser.add_argument(
        "-f",
        "--filename", 
        type=str, 
        help="Name of file", 
        required=True
    )
    args = parser.parse_args()

if __name__ == "__main__":
    main()
##############################################################################