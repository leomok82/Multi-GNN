import pandas as pd
import os
import sys
"""
Combines multiple csv files into one csv file. Usage:
python combine_csv.py /Users/leo/Desktop/AML/data/combined_csv.csv /Users/leo/Desktop/AML/data/LI-Small_Trans.csv /Users/leo/Desktop/AML/data/HI-Small_Trans.csv
"""
if __name__ in "__main__":
    n = len(sys.argv)

    if n == 1:
        print("No input path")
        sys.exit()

    out_path = sys.argv[1]

    paths = sys.argv[2:]
    dfls = []
    for path in paths:
        dfls.append(pd.read_csv(path))
    print(f"Read {len(dfls)} files")

    df3 = pd.concat(dfls)

    df3.reset_index(drop=True,inplace=True)
    df3.to_csv(out_path, index=False)
    num_paths = len(paths)

    print(f"Combined {num_paths} files with {df3.shape[0]} rows")