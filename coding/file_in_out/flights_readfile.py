"""
Functions:
- Take each line as a list, which contains words separated from each other. 
"""
with open("flights.txt", 'r') as file:
    for line in file:
        print(line.split())