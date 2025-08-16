# # Week 3 Activity 3 - (lorenzoagaloos-270729354)
# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format. 
# Then, compute the maximum, minimum, average, and absolute values for each column in the dataset. 
# (see link to download a big numerical data in csv format from link: https://archive.ics.uci.edu/dataset/396/sales+transactions+dataset+weekly
# https://archive.ics.uci.edu/dataset/396/sales+transactions+dataset+weekly
# The dataset contains the sales volume data of over 800 items covering period of 52 weeks
# Dataset additional information: 52 columns for 52 weeks; normalised values of provided too

#
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
sales_transactions_weekly = fetch_ucirepo(id=396) 
  
# data (as pandas dataframes) 
X = sales_transactions_weekly.data.features 
y = sales_transactions_weekly.data.targets 
  
# metadata 
print(sales_transactions_weekly.metadata) 
  
# variable information 
print(sales_transactions_weekly.variables) 

from pathlib import Path
from pyarrow import Table, parquet

class ParquetConverter:

    # This class is responsible for converting a pandas DataFrame to Parquet format and saving it to a specified file path.
    def __init__(self, filename):

        # Determines the directory of the current script
        script_dir = Path(__file__).resolve().parent
        self.file_path = script_dir / filename

    # Convert a pandas DataFrame to Parquet format and save it to the specified file path    
    def convert_to_parquet(self, df): 
        table = Table.from_pandas(df)
        parquet.write_table(table, self.file_path)
        print(f"Data successfully converted to Parquet format and saved to {self.file_path}")

    # Compute statistics for each column in the DataFrame
    def compute_statistics(self, df):
        stats = {
            'max': df.max(),
            'min': df.min(),
            'mean': df.mean(),
            'abs': df.abs().max()
        }
        return stats

def main():
    import pandas as pd

    # Load the dataset into a pandas DataFrame
    df = pd.DataFrame(X)

    # Create an instance of ParquetConverter
    converter = ParquetConverter("sales_transactions_weekly.parquet")

    # Convert the DataFrame to Parquet format
    converter.convert_to_parquet(df)

    # Compute statistics for each column
    stats = converter.compute_statistics(df)
    
    # Print the computed statistics
    print("Computed Statistics:")
    for stat_name, values in stats.items():
        print(f"{stat_name.capitalize()}:")
        print(values)

    print("\nStatistics computed successfully.\n")

if __name__ == "__main__":
    main()

