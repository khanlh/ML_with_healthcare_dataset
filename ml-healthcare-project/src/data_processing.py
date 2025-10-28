def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df.fillna(method='ffill', inplace=True)
    
    # Convert data types if necessary
    # Example: df['Age'] = df['Age'].astype(int)
    
    return df

def transform_data(df):
    # Example transformation: create a new column
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 18, 35, 50, 65, 100], 
                             labels=['0-18', '19-35', '36-50', '51-65', '66+'])
    return df

def save_processed_data(df, output_path):
    df.to_csv(output_path, index=False)