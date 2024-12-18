import pandas as pd

def prueba():
    print("Hola")
    
def check_dataframes_consistency(dataframes):
    """
    Check if all dataframes have the same columns and data types
    
    Args:
        dataframes: List of dataframes to check
    
    Returns:
        bool: True if all dataframes are consistent
    """
    if not dataframes:
        return True
        
    # Get reference columns and types from first dataframe
    reference_columns = set(dataframes[0].columns)
    reference_types = dataframes[0].dtypes

    # Check each dataframe against the reference
    for df in dataframes[1:]:
        if set(df.columns) != reference_columns:
            return False
            
        if not (df.dtypes == reference_types).all():
            return False
            
    return True
