import csv
# Function to read and display the contents of a CSV file
def read_csv(file_path):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Read the header
            print(f"{' | '.join(header)}")  # Print the header
            print('-' * 40)
            for row in csv_reader:
                print(f"{' | '.join(row)}")   # Print each row
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your CSV file
file_path = 'C:/Users/manis/OneDrive/Desktop/DANLC/Example.csv'

read_csv(file_path)
"""Output:
Day | Number
----------------------------------------
Monday | 1
Tuesday | 2
Wednesday | 3
Friday | 4
Saturday | 5
"""
