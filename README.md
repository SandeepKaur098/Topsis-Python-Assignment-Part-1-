# TOPSIS-Python

## Project Overview
This project implements the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) algorithm. It is a multi-criteria decision analysis method used to rank a finite number of alternatives based on their distance from the "ideal best" and "ideal worst" solutions.

This package provides a command-line tool to perform the analysis on any CSV dataset containing numerical data.

## Installation & Prerequisites
To run this project, you need **Python** installed along with the following libraries:
* pandas
* numpy
* matplotlib (for generating graphs)

You can install the dependencies using:
```bash
pip install pandas numpy matplotlib


Methodology
The algorithm follows these standard steps:
Data Validation: Checks for missing values and ensures all input columns are numeric.
Vector Normalization: Reduces all criteria to the same scale.
Weighting: Multiplies the normalized matrix by the user-assigned weights.
Ideal Best & Worst: Identifies the ideal best and ideal worst values for each criterion (considering impacts + or -).
Euclidean Distance: Calculates the distance of each alternative from the best and worst solutions.
Performance Score: Calculates a score (0 to 1) and ranks the alternatives (Higher Score = Better Rank).

Usage
The script is designed to be run from the command line.
python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>

Parameters
InputDataFile: Path to the input CSV file. The first column should be the object name (e.g., Fund Name).
Weights: Comma-separated numbers representing the importance of each criterion (e.g., 1,1,1,1).
Impacts: Comma-separated signs (+ or -).
+ : Higher value is better (e.g., Profit, Accuracy).

- : Lower value is better (e.g., Cost, Error).
ResultFileName: Name of the output CSV file to save the results.

Example Execution
Below is a demonstration of the tool using the sample data provided in this assignment (data.csv).
1. Input Data (data.csv)
The input file contains data for 8 funds with 5 different parameters.
2. Command Used
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,-" result.csv

3. Output Results
The program calculates the TOPSIS Score and Rank for each fund. A higher score indicates a better rank.
| Fund Name | Topsis Score | Rank |
| :---      | :---         | :--- |
| M1        | 0.4435       | 6    |
| M2        | 0.4851       | 5    |
| M3        | 0.2834       | 7    |
| M4        | 0.5362       | 3    |
| M5        | 0.2281       | 8    |
| M6        | 0.6973       | 1    |
| M7        | 0.5891       | 2    |
| M8        | 0.5342       | 4    |
(Note: The values below are from a sample run. Please verify with your generated result.csv)

4. Visual Analysis
The following bar chart compares the performance of different funds based on their TOPSIS score.
![TOPSIS Result Graph](graph.png)

License

This project is open-source and available for educational purposes.
