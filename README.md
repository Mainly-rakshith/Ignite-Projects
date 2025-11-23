# Ignite Projects

## Overview
This repository contains all programming assignments completed for PROG1003.  
Each homework focuses on a different Python concept, including loops, functions, input handling, file processing, CSV reading, and text parsing.

## Project List

### Homework 2 – Making Change
This assignment takes an amount between 0 and 99 cents and calculates the fewest number of coins needed.  
It uses integer division and modulo to compute quarters, dimes, nickels, and pennies.  
The program also supports repeated runs using a simple input prompt.

### Homework 3 – Making Change Enhanced
An improved and more organized version of Homework 2.  
The coin breakdown is placed into a function, making the structure easier to understand and maintain.  
The output format is clearer and the logic is more modular.

### Homework 4 – GeoPin
This project converts latitude and longitude into a GeoPin barcode format.  
The program validates coordinate ranges, normalizes values, and encodes them using a provided algorithm.  
The logic is split across two files, `barcode.py` and `main.py`.

### Homework 5 – Tic-Tac-Toe Game
This assignment implements a fully playable 2-player Tic-Tac-Toe game in the console.
The board updates after each move, user input is validated, and win conditions are checked for rows, columns, and diagonals.
The program detects ties when the board is full.

### Homework 6 – How Far
This assignment reads city information from a CSV file and computes the closest cities to any city the user enters.  
It uses the great-circle distance formula, sorts results, and displays the 13 nearest cities.  
The program uses lists and dictionaries and matches the required output exactly.

### Homework 7 – Spelling Checker
This project checks every word in a text file against a dictionary file.  
It cleans punctuation, counts correct words, and records misspelled words.  
Results are written to `correct_words.txt` and `misspelled_words.txt`.

## Folder Structure

```
Ignite Technology Projects/
│
├── Homework 2/
├── Homework 3/
├── Homework 4/
├── Homework 5/
├── Homework 6/
└── Homework 7/
```

## How to Run a Project
Use the terminal to run any assignment:

```
python3 <folder>/main.py
```

Examples:
```
python3 "Homework 4"/main.py
python3 "Homework 7"/main.py
```

## Skills Learned
- Loops and conditionals
- Functions and modular code
- File reading and writing
- CSV parsing
- String cleanup and text processing
- Sorting and searching data
- Code organization and testing
