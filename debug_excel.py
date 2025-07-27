import pandas as pd

# Read and display Excel file contents
try:
    df = pd.read_excel("emails.xlsx")
    print("Excel file loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst few rows:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    
    # Check filtering conditions
    print(f"\n=== FILTER ANALYSIS ===")
    print(f"Total rows: {len(df)}")
    
    # Check Subject filter
    python_workshop_rows = df[df['Subject'] == "Python Workshop"] if 'Subject' in df.columns else pd.DataFrame()
    print(f"Rows with Subject = 'Python Workshop': {len(python_workshop_rows)}")
    
    # Check Send? column
    if 'Send?' in df.columns:
        send_y_rows = df[df['Send?'] == "Y"]
        print(f"Rows with Send? = 'Y': {len(send_y_rows)}")
        print(f"Unique values in Send? column: {df['Send?'].unique()}")
    else:
        print("No 'Send?' column found")
        
except Exception as e:
    print(f"Error reading Excel file: {e}")
