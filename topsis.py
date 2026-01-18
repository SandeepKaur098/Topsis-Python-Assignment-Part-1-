import sys
import pandas as pd
import numpy as np

def topsis():
    # 1. Check if the user provided the right number of arguments
    # Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
    if len(sys.argv) != 5:
        print("Error: Wrong number of parameters.")
        print("Usage: python topsis.py data.csv '1,1,1,1' '+,+,-,+' result.csv")
        return

    # Assign variables to the arguments for better readability
    input_filename = sys.argv[1]
    weights_string = sys.argv[2]
    impacts_string = sys.argv[3]
    output_filename = sys.argv[4]

    # 2. Try to read the file
    try:
        dataset = pd.read_csv(input_filename)
    except FileNotFoundError:
        print("Error: File not found. Please check the path.")
        return

    # 3. Check if file has enough columns (minimum 3)
    if dataset.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        return

    # 4. Handle non-numeric values
    # We only need the numeric part (from 2nd column to the end)
    temp_dataset = dataset.iloc[:, 1:].values
    
    # Check if all values are actually numbers
    if not np.issubdtype(temp_dataset.dtype, np.number):
        print("Error: From 2nd to last columns must contain numeric values only.")
        return

    # 5. Process Weights and Impacts
    # Convert "1,1,1" string into a list of numbers
    try:
        weights = [float(w) for w in weights_string.split(',')]
    except ValueError:
        print("Error: Weights must be numeric separated by commas.")
        return

    impacts = impacts_string.split(',')

    # Check if the number of weights/impacts matches the number of columns
    num_cols = temp_dataset.shape[1]
    
    if len(weights) != num_cols or len(impacts) != num_cols:
        print("Error: Number of weights, impacts, and columns must be the same.")
        return

    # Check if impacts are valid (+ or -)
    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be either '+' or '-'.")
        return

    # --- TOPSIS ALGORITHM START ---

    # Step 1: Normalize the matrix
    # Divide each value by the square root of sum of squares of that column
    rss = np.sqrt(np.sum(temp_dataset**2, axis=0))
    normalized_data = temp_dataset / rss

    # Step 2: Multiply by weights
    weighted_data = normalized_data * weights

    # Step 3: Find Ideal Best and Ideal Worst
    ideal_best = []
    ideal_worst = []

    for i in range(num_cols):
        if impacts[i] == '+':
            ideal_best.append(max(weighted_data[:, i]))
            ideal_worst.append(min(weighted_data[:, i]))
        else:
            ideal_best.append(min(weighted_data[:, i]))
            ideal_worst.append(max(weighted_data[:, i]))

    # Step 4: Calculate Euclidean Distance from Best and Worst
    # Formula: sqrt(sum((value - ideal)^2))
    dist_best = np.sqrt(np.sum((weighted_data - ideal_best)**2, axis=1))
    dist_worst = np.sqrt(np.sum((weighted_data - ideal_worst)**2, axis=1))

    # Step 5: Calculate Score
    score = dist_worst / (dist_best + dist_worst)

    # --- OUTPUT ---

    # Add the new columns to the original dataset
    dataset['Topsis Score'] = score
    
    # Rank them (higher score = rank 1)
    dataset['Rank'] = dataset['Topsis Score'].rank(ascending=False).astype(int)

    # Save to CSV
    dataset.to_csv(output_filename, index=False)
    print(f"Success: Result saved to {output_filename}")

if __name__ == "__main__":
    topsis()
