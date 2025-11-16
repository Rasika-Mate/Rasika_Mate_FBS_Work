# 2. Create a function that extracts all the dates from a given text using regular expressions. Dates can be in various formats like MM/DD/YYYY, DD-MM-YYYY, or written out like January 1, 2023. Extract all such date occurrences.

import re

def extract_dates(text):
    pattern = r'''
        (                           # Group start
        \b\d{2}/\d{2}/\d{4}\b       # Format: MM/DD/YYYY
        |                           # OR
        \b\d{2}-\d{2}-\d{4}\b       # Format: DD-MM-YYYY
        |                           # OR
        \b(?:January|February|March|April|May|June|
           July|August|September|October|November|December)
           \s\d{1,2},\s\d{4}\b      # Format: Month 1, 2023
        )                           # Group end
    '''

    dates = re.findall(pattern, text, flags=re.VERBOSE) # find all matches (re.VERBOSE allows multiline readable regex)
    return dates

text = """
Important dates: 16/11/2025, 01-01-2024,
and also November 16, 2025 is a holiday.
"""
print(extract_dates(text))