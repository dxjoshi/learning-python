import re


def Find(pattern, text):
    match = re.match(pattern, text)
    print(match.group())


Find(r'[\w.\d]+@[\w.]+', 'deepak.joshi92@gmail.com')
