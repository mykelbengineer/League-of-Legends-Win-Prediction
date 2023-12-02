import json
import pandas as pd

def process_data(df_final):
    """
    Apply a predefined mapping to transform specific tier columns.

    Parameters:
    df_final (DataFrame): DataFrame with the columns to be transformed.

    Returns:
    DataFrame: The DataFrame with the transformed columns.
    """
    tier_mapping = {
        'UN': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, 'S': 6, 'God': 7, 'None': 1, None: 1
    }

    tier_columns = [
        'TOP1Tier', 'TOP2Tier', 'JUNGLE1Tier', 'JUNGLE2Tier',
        'MID1Tier', 'MID2Tier', 'SUPPORT1Tier', 'SUPPORT2Tier',
        'CARRY1Tier', 'CARRY2Tier'
    ]

    for col in tier_columns:
        if col in df_final.columns:
            df_final[col] = df_final[col].apply(lambda x: tier_mapping.get(x, 1))  # Default to 1 if key is not found

    return df_final


def read_counters(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_and_clean_stats(filepath):
    stats = pd.read_csv(filepath, delimiter=';')
    stats = stats[['Name', 'Tier', 'Role']]
    stats['Name'] = stats['Name'].apply(lambda a: ''.join(c.lower() for c in a if c.isalpha() or c.isspace()))
    return stats

def filter_stats_by_counters(stats, counters):
    filtered_stats = pd.concat([stats[stats['Name'] == champ] for champ in counters.keys()])
    return filtered_stats.reset_index(drop=True)

import pandas as pd

def modify_records_based_on_counters(df, counters):
    """
    Modify the DataFrame to add columns indicating if champions in each role were countered.
    
    Parameters:
    df (DataFrame): DataFrame containing the champion matchups.
    counters (dict): Dictionary with champion counters.
    
    Returns:
    DataFrame: Modified DataFrame with additional columns for counters.
    """

    # Define the counter check functions
    def ctrjg2(x):
        p1 = x['JUNGLE1'].lower()
        p2 = x['JUNGLE2'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
        
    def ctrjg1(x):
        p1 = x['JUNGLE2'].lower()
        p2 = x['JUNGLE1'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
    def ctrtop2(x):
        p1 = x['TOP1'].lower()
        p2 = x['TOP2'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
    def ctrtop1(x):
        p1 = x['TOP2'].lower()
        p2 = x['TOP1'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0   
    def ctrmid2(x):
        p1 = x['MID1'].lower()
        p2 = x['MID2'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
    def ctrmid1(x):
        p1 = x['MID2'].lower()
        p2 = x['MID1'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
    def ctrcarry2(x):
        p1 = x['CARRY1'].lower()
        p2 = x['CARRY2'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
    def ctrcarry1(x):
        p1 = x['CARRY2'].lower()
        p2 = x['CARRY1'].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0

    # Apply the counter check functions to their respective columns
    df['jg2countered'] = df.apply(ctrjg2, axis=1)
    df['jg1countered'] = df.apply(ctrjg1, axis=1)
    df['top2countered'] = df.apply(ctrtop2, axis=1)
    df['top1countered'] = df.apply(ctrtop1, axis=1)
    df['mid2countered'] = df.apply(ctrmid2, axis=1)
    df['mid1countered'] = df.apply(ctrmid1, axis=1)
    df['carry2countered'] = df.apply(ctrcarry2, axis=1)
    df['carry1countered'] = df.apply(ctrcarry1, axis=1)

    return df

def expand_matchups(df, role, stats, support_dict):
    df_expanded = pd.DataFrame()
    for champ in stats[stats['Role'] == support_dict[role]]['Name'].unique():
        df_copy = df.copy()
        df_copy[role] = champ
        df_expanded = pd.concat([df_expanded, df_copy])
    return df_expanded

def ranks(df, stats):
    positions = ['JUNGLE1', 'JUNGLE2', 'TOP1', 'TOP2', 'MID1', 'SUPPORT2', 'MID2', 'SUPPORT1', 'CARRY1', 'CARRY2']
    d3 = {'UN':1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, 'S': 6, 'God': 7, 'None':1, None:1}

    for i in positions:
        posit = i.replace('CARRY','ADC')                         
        stats_filtered = stats[stats['Role'] == posit[:-1]]
        name_to_tier = dict(zip(stats_filtered['Name'],stats_filtered['Tier'])) 
        df[i+'Tier'] = df[i].map(lambda x: name_to_tier.get(x.lower(), None))
        df[i+'Tier'] = df[i+'Tier'].apply(lambda x: d3.get(x, 1)) # Default to 1 if not found in d3
    return df

def process_champion_data(df, stats_filepath, counters_filepath, role, support_dict):
    """
    Process champion data by reading and cleaning stats, applying counters, and expanding matchups.

    Parameters:
    df (DataFrame): Initial DataFrame with champion matchups.
    stats_filepath (str): File path to the champion stats CSV file.
    counters_filepath (str): File path to the JSON file containing champion counters.
    role (str): The role to expand in matchups (e.g., 'TOP1', 'JUNGLE1').

    Returns:
    DataFrame: Processed DataFrame with expanded matchups and counters.
    """

    counters = read_counters(counters_filepath)
    stats = read_and_clean_stats(stats_filepath)
    stats_filtered = filter_stats_by_counters(stats, counters)
    df_modified = modify_records_based_on_counters(df, counters)
    df_expanded = expand_matchups(df_modified, role, stats_filtered, support_dict)
    df_ranked = ranks(df_expanded, stats_filtered)

    return df_ranked

