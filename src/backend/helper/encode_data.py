def encode_and_clean(df_final):
    """
    Convert 'win' column to integers and remove the 'matchid' column.

    Parameters:
    df_final (DataFrame): DataFrame to be transformed.

    Returns:
    DataFrame: The transformed DataFrame.
    """
    try:
        df_final['win'] = df_final['win'].apply(int)
        del df_final['matchid']
        return df_final
    except KeyError as e:
        print(f"Column not found in DataFrame: {e}")
        return df_final
    except ValueError as e:
        print(f"Value error during conversion: {e}")
        return df_final
    except Exception as e:
        print(f"An error occurred during encoding and cleaning: {e}")
        return df_final
