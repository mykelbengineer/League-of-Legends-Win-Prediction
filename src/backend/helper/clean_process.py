def clean_and_process_data(df_clean, df_stats):
    """
    Clean and process data by dropping specific columns, filling missing values, 
    and joining two DataFrames.

    Parameters:
    df_clean (DataFrame): DataFrame corresponding to the cleaned data.
    df_stats (DataFrame): DataFrame corresponding to the merged stats data.

    Returns:
    DataFrame: The final cleaned and processed DataFrame, or None if an error occurs.
    """
    try:
        # Dropping the 'Unnamed: 0' column from df_clean
        df_clean.drop('Unnamed: 0', inplace=True, axis=1)

        # Dropping columns from df_stats starting from the third column onwards
        drop_cols = list(df_stats.columns)[2:]
        df_stats.drop(drop_cols, inplace=True, axis=1)

        # Filling missing values in df_clean with 'UN'
        df_clean.fillna('UN', inplace=True)

        # Joining df_clean with df_stats
        df_final = df_clean.set_index('matchid').join(df_stats.set_index('id'), how='left')

        # Resetting the index and dropping any rows with missing values
        df_final.reset_index(inplace=True)
        df_final.dropna(inplace=True)
        df_final.reset_index(drop=True, inplace=True)

        return df_final
    except Exception as e:
        print(f"Error occurred during data cleaning and processing: {e}")
        return None

