# 4. Write a function that extracts all the URLs from a given text using regular expressions. Return a list of URLs found in the input text.

import re

def extract_urls(text):
    pattern = r'(https?://[^\s]+|www\.[^\s]+)'  # Regex pattern to find URLs (http, https, www)
    urls = re.findall(pattern, text)
    return urls

text = """
Visit https://www.google.com for search.
Check www.github.com for code.
Our site: http://example.org/home/page.html
"""
print(extract_urls(text))