import sys
import os

def check_input_file(input_file: str) -> None:
    """Check if the input file exists and is readable."""

    if not os.path.isfile(input_file):
        sys.stdout.write(f"Error: Input file '{input_file}' does not exist.\n")
        sys.exit(1)
    if not os.access(input_file, os.R_OK):
        sys.stdout.write(f"Error: Input file '{input_file}' is not readable.\n")
        sys.exit(1)
    if not input_file.lower().endswith(".txt"):
        sys.stdout.write("Error: Input file must be a .txt file.\n")
        sys.exit(1)