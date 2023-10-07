import pandas as pd

# Replace 'input_file.txt' with the path to your input text file
input_file = '/Users/keithstateson/BLS Bureau Labor Stats/CUUR0000SA0.txt'

# Read the tab-separated text file into a DataFrame
df = pd.read_csv(input_file, sep='\t')

# Replace 'output_file.xlsx' with the desired output Excel file name
output_file = 'output_file.xlsx'

# Save the DataFrame to an Excel file
df.to_excel(output_file, index=False)
