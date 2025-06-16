# scripts/prepare_modeling_data.py

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

def load_data(path='../data/insurance_data.csv'):
    """Loads the dataset from the specified path."""
    print("Loading dataset...")
    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return None

def create_features(df):
    """Creates new features for modeling."""
    print("Creating new features...")
    df['TransactionDate'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    df['VehicleAge'] = df['TransactionDate'].dt.year - df['RegistrationYear']
    df['HasClaim'] = (df['TotalClaims'] > 0).astype(int)
    df.dropna(subset=['TransactionDate', 'VehicleAge'], inplace=True)
    print("New features 'VehicleAge' and 'HasClaim' created.")
    return df

def clean_and_select_features(df):
    """Cleans data and selects relevant features for modeling."""
    print("Cleaning data and selecting features...")
    
    # Identify high-cardinality columns to drop BEFORE encoding
    high_cardinality_cols = ['PostalCode', 'mmcode', 'Model', 'SubCrestaZone', 'MainCrestaZone']
    print(f"Dropping high-cardinality columns: {high_cardinality_cols}")
    
    # Identify columns with too many missing values
    high_missing_cols = [col for col in df.columns if df[col].isnull().mean() > 0.4]
    print(f"Dropping high-missing columns: {high_missing_cols}")

    # Combine all columns to drop
    cols_to_drop = [
        'UnderwrittenCoverID', 'PolicyID', 'TransactionMonth', 'TransactionDate', 'RegistrationYear'
    ]
    cols_to_drop.extend(high_cardinality_cols)
    cols_to_drop.extend(high_missing_cols)
    
    # Use a set to handle potential duplicates in the drop list
    cols_to_drop = list(set(cols_to_drop))
    
    df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    
    print(f"Dropped {len(cols_to_drop)} columns.")
    return df

def handle_missing_values(df):
    """Imputes missing values."""
    print("Handling missing values...")
    numeric_cols = df.select_dtypes(include=np.number).columns
    categorical_cols = df.select_dtypes(exclude=np.number).columns
    
    for col in numeric_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)
            
    for col in categorical_cols:
        if df[col].isnull().any():
            df[col].fillna(df[col].mode()[0], inplace=True)
            
    print("Missing values handled.")
    return df

def encode_categorical_features(df, top_n=10):
    """
    Encodes categorical features using a memory-efficient strategy.
    Only the top_n most frequent categories are one-hot encoded, the rest are grouped into 'Other'.
    """
    print("Encoding categorical features (memory-efficiently)...")
    
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    for col in categorical_cols:
        # Find the top N most frequent categories
        top_categories = df[col].value_counts().nlargest(top_n).index
        
        # Group all other categories into 'Other'
        df[col] = np.where(df[col].isin(top_categories), df[col], 'Other')

    # Now perform one-hot encoding on the transformed columns
    # Using uint8 is much more memory efficient for 0s and 1s
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True, dtype=np.uint8)
    
    print(f"DataFrame transformed from {df.shape[1]} to {df_encoded.shape[1]} columns after encoding.")
    return df_encoded

def main():
    """Main function to run the data preparation pipeline."""
    df = load_data('../data/insurance_data.csv')
    if df is not None:
        df = create_features(df)
        df = clean_and_select_features(df)
        df = handle_missing_values(df)
        # We pass a limit (e.g., top 10) to the encoding function now
        df_model_ready = encode_categorical_features(df, top_n=10)
        
        output_path = '../data/processed/modeling_data.csv'
        df_model_ready.to_csv(output_path, index=False)
        print(f"\nModel-ready data saved successfully to {output_path}")
        print(f"Final dataset shape: {df_model_ready.shape}")

if __name__ == "__main__":
    main()