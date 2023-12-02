import pandas as pd
import json
import joblib

def load_model(file_path):
    model = joblib.load(file_path)
    return model

def read_counters(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def initialize_counters():
    counters = read_counters('EDA/counters.json')
    return counters

def create_counter_functions(counters):
    def ctr_func(x, role1, role2):
        p1 = x[role1].lower()
        p2 = x[role2].lower()
        if p1 in counters[p2]:
            return 1
        else: 
            return 0
    return ctr_func

def normit(a):
    s = ''
    for i in a:
        if i.isalpha() or i.isspace():
            s += i.lower()
    return s

def read_and_prepare_stats(file_path, counters):
    stats = pd.read_csv(file_path)
    stats = stats[['Name', 'Tier', 'Role']]
    stats['Name'] = stats['Name'].apply(normit)

    # Check if counters is empty
    if not counters:
        raise ValueError("Counters dictionary is empty.")

    # Filter and merge stats
    m = pd.DataFrame()
    for champion in counters.keys():
        b = stats[stats['Name'] == champion]
        m = pd.concat([m, b])

    return m



def mod(df1, ctr_func):
    for role_pair in [('TOP1', 'TOP2'), ('JUNGLE1', 'JUNGLE2'), ('MID1', 'MID2'), ('CARRY1', 'CARRY2')]:
        role1, role2 = role_pair
        df1[f'{role2}countered'] = df1.apply(lambda x: ctr_func(x, role1, role2), axis=1)
        df1[f'{role1}countered'] = df1.apply(lambda x: ctr_func(x, role2, role1), axis=1)
    return df1

dict2 = {'TOP1':'TOP', 'TOP2': 'TOP', 'JUNGLE1': 'JUNGLE', 'JUNGLE2': 'JUNGLE',
         'MID1': 'MID', 'MID2':'MID', 'SUPPORT1': 'SUPPORT', 'SUPPORT2': 'SUPPORT', 'CARRY1': 'ADC', 'CARRY2': 'ADC'}
def filler(df, role):
    df1 = pd.DataFrame(data = df, index = [0])
    for i in stats[stats['Role']==dict2[role]]['Name'].unique():
        df2 = pd.DataFrame(data = df, index = [0])
        df2[role] = i
        df1 = pd.concat([df1, df2])
    return df1, df1[role], df1[role].iloc[0]

positions = ['TOP1', 'TOP2','JUNGLE1', 'JUNGLE2', 'MID1','MID2', 'SUPPORT1', 'SUPPORT2', 'CARRY1', 'CARRY2']
d3 = {'UN':1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, 'S': 6, 'God': 7, 'None':1, None:1}

def ranks(df, stats):
    for i in positions:
        posit = i.replace('CARRY','ADC')                         
        stats_filtered = stats[stats['Role'] == posit[:-1]]
        name_to_tier = dict(zip(stats_filtered['Name'],stats_filtered['Tier'])) 
        df[i+'Tier'] = df[i].map(lambda x: name_to_tier.get(x.lower(), None))
    
    # Apply tier mappings
    for tier_col in ['TOP1Tier', 'TOP2Tier', 'JUNGLE1Tier', 'JUNGLE2Tier', 'MID1Tier', 'MID2Tier', 'SUPPORT1Tier', 'SUPPORT2Tier', 'CARRY1Tier', 'CARRY2Tier']:
        df[tier_col] = df[tier_col].apply(lambda x: d3[x])

    # Rename columns to lowercase to match training data feature names
    rename_dict = {
        'CARRY1countered': 'carry1countered',
        'CARRY2countered': 'carry2countered',
        'JUNGLE1countered': 'jg1countered',
        'JUNGLE2countered': 'jg2countered',
        'MID1countered': 'mid1countered',
        'MID2countered': 'mid2countered',
        'TOP1countered': 'top1countered',
        'TOP2countered': 'top2countered',
        'SUPPORT1countered': 'support1countered',
        'SUPPORT2countered': 'support2countered'
    }
    df.rename(columns=rename_dict, inplace=True)

    return df


def make_prediction(input_df, model, stats, counters, role):
    # Convert input data to DataFrame if it's a dictionary
    if isinstance(input_df, dict):
        input_df = pd.DataFrame([input_df])
    
    # Initialize counter functions
    ctr_func = create_counter_functions(counters)

    # Apply the mod function for counter logic
    input_df_modified = mod(input_df, ctr_func)

    # Apply the filler function and ranks function
    input_df_filled, filled_column, current_value = filler(input_df_modified, role)
    input_df_ranked = ranks(input_df_filled, stats)

    # Select only the columns present in df_final
    df_final_columns = ['top2countered', 'top1countered', 'jg2countered', 'jg1countered', 'mid2countered', 'mid1countered', 'carry2countered', 'carry1countered', 'TOP1Tier', 'TOP2Tier', 'JUNGLE1Tier', 'JUNGLE2Tier', 'MID1Tier', 'MID2Tier', 'SUPPORT1Tier', 'SUPPORT2Tier', 'CARRY1Tier', 'CARRY2Tier', 'win']
    input_df_ranked = input_df_ranked[df_final_columns[:-1]] # Exclude 'win' if it's not a feature in prediction

    # Make prediction
    preds = model.predict_proba(input_df_ranked)

    # Process the predictions to match the expected output format
    values = {}
    for i, key in enumerate(filled_column):
        values[key] = preds[i][0]  # Assuming class '0' is the target class
    sorted_vals = sorted(values.items(), key=lambda x: -x[1])

    # Extract the probability for the current configuration
    current_prob = values.get(current_value, None)

    return sorted_vals[:5], {'Current': current_prob}

# Example usage
model = load_model('EDA/lol_prediction_model.sav')
# Initialize counters before calling the function
counters = initialize_counters()

# Now call the function
stats = read_and_prepare_stats('EDA/League_of_Legends_Champion_Stats_13.1.csv', counters)


input_df = {'TOP1':'Fiora','TOP2':'Galio', 'JUNGLE1': 'Warwick','JUNGLE2': 'Skarner','MID1':'Viktor','MID2':'Ahri','SUPPORT1':'Nami','SUPPORT2':'VelKoz','CARRY1':'Draven','CARRY2':'Jinx'}

predictions = make_prediction(input_df, model, stats, counters, role='TOP1')

print(predictions)

















# from sklearn.model_selection import train_test_split

# def prepare_data(df, target_column):
#     X = df.drop(target_column, axis=1)
#     Y = df[target_column]
    
#     # Split the data into training and test sets
#     x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
#     return x_train, x_test, y_train, y_test


# from sklearn.linear_model import LogisticRegression

# def train_model(x_train, y_train):
#     model = LogisticRegression()
#     model.fit(x_train, y_train)
#     return model


# from sklearn.metrics import accuracy_score

# def evaluate_model(model, x_test, y_test):
#     y_pred = model.predict(x_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     return accuracy


# import pandas as pd

# # Load df_final
# df_final = pd.read_csv('EDA/df_final.csv')

# # Prepare data
# target_column = 'win'  # or whatever your target column is
# x_train, x_test, y_train, y_test = prepare_data(df_final, target_column)


# import joblib

# def save_model(model, file_path):
#     joblib.dump(model, file_path)
#     print(f"Model saved to {file_path}")

# # Example usage
# model = train_model(x_train, y_train)  # Assuming model is already trained
# file_path = 'lol_prediction_model.sav'
# save_model(model, file_path)


























# import pandas as pd

# def read_and_merge_csv(stats1_path, stats2_path, clean2_path):
#     # Read CSV files
#     df_stats1 = pd.read_csv(stats1_path)
#     df_stats2 = pd.read_csv(stats2_path)
#     df_clean = pd.read_csv(clean2_path)

#     # Merge stats1 and stats2
#     df_stats = pd.concat([df_stats1, df_stats2], ignore_index=True)

#     # Return merged dataframes
#     return df_clean, df_stats

# def clean_data(df_clean, df_stats):
#     # Perform necessary cleaning steps
#     df_clean.drop('Unnamed: 0', inplace=True, axis=1)
#     df_clean = df_clean.fillna('UN')
    
#     # Drop unnecessary columns from df_stats
#     drop_cols = list(df_stats.columns)[2:]
#     df_stats.drop(drop_cols, inplace=True, axis=1)

#     # Merge df_clean with df_stats
#     df_final = df_clean.set_index('matchid').join(df_stats.set_index('id'), how='left')
#     df_final = df_final.reset_index()
#     df_final = df_final.dropna()
#     df_final = df_final.reset_index(drop=True)

#     return df_final


# def feature_engineering(df_final):
#     # Convert categorical data to numerical, etc.
#     tier_mapping = {'UN': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, 'S': 6, 'God': 7, 'None': 1, None: 1}
#     for col in ['TOP1Tier', 'TOP2Tier', 'JUNGLE1Tier', 'JUNGLE2Tier', 'MID1Tier', 'MID2Tier', 'SUPPORT1Tier', 'SUPPORT2Tier', 'CARRY1Tier', 'CARRY2Tier']:
#         df_final[col] = df_final[col].apply(lambda x: tier_mapping[x])

#     # Convert 'win' column to binary
#     df_final['win'] = df_final['win'].apply(lambda x: int(x))

#     # Drop the 'matchid' column if it's no longer needed
#     del df_final['matchid']

#     return df_final


# import os
# import pandas as pd

# def save_df_to_folder(df, folder_path, file_name):
#     # Check if the folder exists, create it if it doesn't
#     if not os.path.exists(folder_path):
#         os.makedirs(folder_path)

#     # Full path for the CSV file
#     file_path = os.path.join(folder_path, file_name)

#     # Save the DataFrame as a CSV file
#     df.to_csv(file_path, index=False)

#     print(f"DataFrame saved as '{file_name}' in '{folder_path}'")


# # Paths to your CSV files
# stats1_path = 'EDA/stats1.csv'
# stats2_path = 'EDA/stats2.csv'
# clean2_path = 'EDA/clean2.csv'

# # Use the functions to create df_final
# df_clean, df_stats = read_and_merge_csv(stats1_path, stats2_path, clean2_path)
# df_final = clean_data(df_clean, df_stats)
# df_final = feature_engineering(df_final)

# # Specify the folder and file name
# folder_path = 'EDA'
# file_name = 'df_final.csv'

# # Save df_final to the folder
# save_df_to_folder(df_final, folder_path, file_name)

