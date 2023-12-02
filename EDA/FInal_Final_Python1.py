import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


pd.options.mode.chained_assignment = None

data = ""
data2 = ""

df_stats1 = pd.read_csv('stats1.csv')
df_stats2 = pd.read_csv('stats2.csv')


# Reading data from stats1
with open('stats1.csv') as fp:
    data = fp.read()


# Reading data from stats2
with open('stats2.csv') as fp:
    data2 = fp.read()


# Merging both files to stats
data += "\n"
data += data2
 
with open ('stats.csv', 'w') as fp:
    fp.write(data)



df_clean = pd.read_csv('clean2.csv')
df_clean.drop('Unnamed: 0',inplace = True, axis = 1)
df_stats = pd.read_csv('stats.csv')
drop_cols = list(df_stats.columns)[2:]
df_stats.drop(drop_cols, inplace = True, axis = 1)
df_clean = df_clean.fillna('UN')
df_final = df_clean.set_index('matchid').join(df_stats.set_index('id'), how = 'left')
df_final = df_final.reset_index()
df_final = df_final.dropna()
df_final = df_final.reset_index(drop=True)
#display (df_final)
df_final.to_csv('final_stats.csv')



d3 = {'UN':1, 'D': 2, 'C': 3, 'B': 4, 'A': 5, 'S': 6, 'God': 7, 'None':1, None:1}
df_final['TOP1Tier']=df_final['TOP1Tier'].apply(lambda x: d3[x])
df_final['TOP2Tier']=df_final['TOP2Tier'].apply(lambda x: d3[x])
df_final['JUNGLE1Tier']=df_final['JUNGLE1Tier'].apply(lambda x: d3[x])
df_final['JUNGLE2Tier']=df_final['JUNGLE2Tier'].apply(lambda x: d3[x])
df_final['MID1Tier']=df_final['MID1Tier'].apply(lambda x: d3[x])
df_final['MID2Tier']=df_final['MID2Tier'].apply(lambda x: d3[x])
df_final['SUPPORT1Tier']=df_final['SUPPORT1Tier'].apply(lambda x: d3[x])
df_final['SUPPORT2Tier']=df_final['SUPPORT2Tier'].apply(lambda x: d3[x])
df_final['CARRY1Tier']=df_final['CARRY1Tier'].apply(lambda x: d3[x])
df_final['CARRY2Tier']=df_final['CARRY2Tier'].apply(lambda x: d3[x])


# In[61]:


# One hot encoding
df_final['win'] = df_final['win'].apply(lambda x: int(x))
del df_final['matchid']


# In[ ]:





# In[62]:


# Logistic Regression & Model Fitting

data_cols = list(df_final.columns)
target_cols = ['win']
np.random.seed(10)
X = df_final[data_cols[:-1]]
Y = df_final[target_cols]
Y = np.ravel(Y)
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
model_lr = LogisticRegression()
model_lr.fit(x_train,y_train)


# In[63]:


# Prediction
y_pred = model_lr.predict(x_test)
y_pred
print (y_pred)


# In[64]:


# Accuracy
acc = accuracy_score(y_test, y_pred)
acc


# In[65]:


# Predictions start here
#Defining dictionaries
counters = {'aatrox': ['poppy', 'singed', 'vayne',], 
            'ahri':['tristana', 'yasuo', 'irelia'],
            'akali':['tristana', 'twisted fate', 'pantheon'],
            'alistar': ['velkoz', 'swain', 'brand'],
            'amumu': ['karthus', 'nidalee', 'khazix'],
            'anivia': ['yasuo', 'twisted fate', 'irelia'],
            'annie': ['diana', 'irelia', 'yasuo'],
            'ashe': ['draven', 'kalista', 'tristana'],
            'aurelion sol': ['irelia', 'fizz', 'zed'],
            'azir': ['irelia', 'twisted fate', 'ziggs'],
            'bard': ['heimerdinger', 'velkoz'],
            'blitzcrank': ['heimerdinger', 'brand'],
            'brand': ['xerath', 'velkoz'],
            'braum': ['xerath', 'lux', 'brand'],
            'caitlyn': ['draven', 'kalista', 'varus'],
            'camille': ['warwick', 'tryndamere', 'renekton'],
            'cassiopeia': ['yasuo', 'ziggs', 'irelia'],
            'chogath': ['kled', 'volibear', 'aatrox'],
            'corki': ['diana', 'tristana', 'yasuo'], 
            'darius': ['vayne', 'pantheon', 'kled'],
            'diana': ['swain', 'anivia', 'ryze'],
            'drmundo': ['tryndamere', 'aatrox', 'yorick'],
            'draven': ['ziggs', 'miss fortune', 'kogmaw'],
            'ekko': ['kassadin', 'pantheon', 'talon'],
            'elise': ['nidalee', 'rengar', 'diana'], 
            'evelynn': ['karthus', 'nidalee', 'talon'],
            'ezreal': ['draven', 'kalista'],
            'fiddlesticks': ['talon', 'karthus', 'nidalee'],
            'fiora': ['urgot', 'nasus', 'quinn'], 
            'fizz': ['pantheon', 'yasuo', 'irelia'],
            'galio': ['pantheon', 'twisted fate', 'talon'],
            'gangplank': ['rengar', 'tryndamere', 'irelia'],
            'garen': ['tryndamere', 'darius', 'teemo'], 
            'gnar': ['irelia', 'yasuo', 'tryndamere'], 
            'gragas': ['hecarim', 'karthus', 'nidalee'], 
            'graves': ['nidalee', 'talon', 'master yi'],
            'hecarim': ['talon', 'khazix', 'nidalee'], 
            'heimerdinger': ['brand', 'xerath', 'velkoz'],
            'illaoi': ['tryndamere', 'irelia', 'yorick'],
            'irelia': ['renekton', 'pantheon', 'yasuo'], 
            'ivern': ['nidalee', 'karthus', 'hecarim'], 
            'janna': ['xerath', 'velkoz'], 
            'jarvan iv': ['nidalee', 'karthus', 'master yi'], 
            'jax':['illaoi', 'akali', 'kennen'], 
            'jayce': ['irelia', 'yasuo', 'diana'],
            'jhin': ['draven', 'kalista', 'tristana', 'varus'], 
            'jinx': ['draven', 'kalista', 'varus'],
            'kalista': ['twitch', 'draven', 'miss fortune'], 
            'karma': ['poppy', 'akali', 'nasus'], 
            'karthus': ['nidalee', 'master yi', 'ekko'],
            'kassadin': ['talon', 'anivia', 'annie'],
            'katarina': ['kassadin', 'vladimir', 'annie'],
            'kayle': ['irelia', 'tryndamere', 'kled'],
            'kayn': ['nidalee', 'master yi', 'hecarim'],
            'kennen': ['khazix', 'nidalee', 'karthus'],
            "khazix": ['nidalee', 'karthus', 'rengar'],
            'kindred': ['nidalee', 'master yi', 'khazix'], 
            'kled': ['vayne', 'teemo', 'fiora'],
            "kogmaw": ['draven', 'kalista', 'tristana'], 
            'leblanc': ['irelia', 'diana', 'yasuo'], 
            'lee sin': ['karthus', 'nidalee', 'hecarim'], 
            'leona': ['velkoz', 'swain', 'brand'],
            'lissandra': ['ziggs' 'irelia', 'twisted fate'], 
            'lucian': ['draven', 'kalista', 'varus'],
            'lulu':['zyra', 'brand'],
            'lux': ['twisted fate', 'annie', 'swain'],
            'malphite': ['sion', 'mordekaiser', 'volibear'],
            'malzahar':['twisted fate', 'irelia', 'fizz'],
            'maokai': ['kled', 'illaoi', 'mordekaiser'],
            'master yi': ['nidalee', 'khazix', 'hecarim'], 
            'miss fortune': ['draven', 'kalista', 'tristana'],
            'mordekaiser': ['olaf', 'kled', 'tryndamere'],
            'morgana': ['velkoz', 'xerath', 'zyra'],
            'nami': ['xerath', 'zyra', 'velkoz'],
            'nasus': ['tahm kench', 'camille', 'olaf'],
            'nautilus': ['heimerdinger', 'swain', 'brand'],
            'nidalee': ['hecarim', 'master yi', 'rengar'],
            'nocturne': ['nidalee', 'hecarim', 'karthus'],
            'nunu': ['master yi', 'nidalee', 'kindred'],
            'olaf': ['kled', 'renekton', 'illaoi'], 
            'orianna': ['ziggs', 'aurelion sol', 'talon'],
            'ornn': ['olaf', 'shen', 'fiora'],
            'pantheon': ['xerath', 'swain', 'ryze'],
            'poppy': ['hecarim', 'talon', 'karthus'],
            'quinn': ['gragas', 'vayne', 'drmundo'],
            'rakan': ['zyra', 'janna'],
            'rammus': ['udyr', 'karthus', 'nunu'],
            "reksai": ['shyvana', 'nocturne', 'kindred'],
            'renekton': ['nasus', 'vayne', 'illaoi'],
            'rengar': ['shyvana', 'karthus', 'master yi'],
            'riven': ['quinn', 'kennen', 'renekton'],
            'rumble': ['poppy', 'irelia', 'tahm kench'],
            'ryze': ['galio', 'malzahar', 'katarine'],
            'sejuani': ['amumu', 'hecarim', 'karthus'],
            'shaco': ['karthus', 'ivern', 'evelynn'],
            'shen': ['urgot', 'vayne', 'kayle'],
            'shyvana': ['ivern', 'poppy', 'evelynn'],
            'singed': ['vayne', 'fiora', 'gangplank'],
            'sion': ['singed', 'aatrox', 'fiora'],
            'sivir': ['vayne', 'draven', 'lucian'],
            'skarner': ['ivern', 'karthus', 'jarvan iv'],
            'sona': [],
            'soraka': [],
            'swain': ['ekko', 'katarina', 'viktor'],
            'syndra': ['fizz', 'swain', 'katarina'],
            'tahm kench': ['olaf', 'riven', 'shen'],
            'taliyah': ['evelynn', 'talon', 'aurelion sol'],
            'talon': ['ziggs', 'swain', 'lux'],
            'taric': [],
            'teemo': ['tahm kench', 'chogath', 'ornn'],
            'thresh': [],
            'tristana': ['twitch', 'kogmaw', 'jhin'],
            'trundle': ['karthus', 'fiddlesticks', 'jarvan iv'],
            'tryndamere': ['malphite', 'poppy', 'tahm kench'],
            'twisted fate': ['vladimir', 'swain', 'taliyah'],
            'twitch': ['draven', 'lucian', 'vayne'],
            'udyr': ['reksai', 'master yi', 'poppy'],
            'urgot': ['kayle', 'tryndamere', 'nasus'],
            'varus': ['kogmaw', 'miss fortune', 'twitch'],
            'vayne': ['twitch', 'miss fortune', 'draven'],
            'veigar': ['swain', 'kassadin', 'ekko'],
            'velkoz': ['ekko', 'corki', 'taliyah'],
            'vi': ['reksai', 'kindred', 'nocturne'],
            'viktor': ['kassadin', 'akali', 'talon'],
            'vladimir': ['ryze', 'annie', 'swain'],
            'volibear': ['vayne', 'drmundo', 'kayle'],
            'warwick': ['jax', 'nocturne', 'zac'],
            'wukong':['ivern', 'hecarim', 'shyvana'],
            'xayah': ['ziggs', 'miss fortune', 'ashe'],
            'xerath': ['diana', 'fizz', 'annie'],
            'xin zhao': ['karthus', 'kindred', 'reksai'],
            'yasuo': ['malphite', 'swain', 'taliyah', 'malzahar', 'viktor'],
            'yorick': ['irelia', 'shen', 'malphite', 'jax'],
            'zac': ['ekko', 'kayn', 'master yi'],
            'zed': ['garen', 'malphite', 'swain', 'rumble'],
            'ziggs': ['xerath', 'fizz', 'anivia'],
            'zilean': [],
            'zyra': []}
#Counter functions
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
#Read and clean stats file
stats = pd.read_csv('League_of_Legends_Champion_Stats_13.1.csv')
stats = stats[['Name', 'Tier', 'Role']]
def normit(a):
    s = ''
    for i in a:
        if i.isalpha() or i.isspace():
            s+=i.lower()
    return s
stats['Name']=stats['Name'].apply(normit)

m = stats[stats['Name']==list(counters.keys())[0]]
for i in range(1, len(list(counters.keys()))):
    b = stats[stats['Name']==list(counters.keys())[i]]
    m = pd.concat([m, b])
stats = m
#Function to modify the record
def mod(df1):
    df1['top2countered'] = 0
    df1['top1countered'] = 0
    df1['jg2countered'] = 0
    df1['jg1countered'] = 0
    df1['mid2countered'] = 0
    df1['mid1countered'] = 0
    df1['carry2countered'] = 0
    df1['carry1countered'] = 0
    for i in range(0, len(df1)):
        df1['top2countered'].iloc[i] = ctrtop2(df1.iloc[i])
        df1['top1countered'].iloc[i] = ctrtop1(df1.iloc[i])
        df1['jg2countered'].iloc[i] = ctrjg2(df1.iloc[i])
        df1['jg1countered'].iloc[i] = ctrjg1(df1.iloc[i])
        df1['mid2countered'].iloc[i] = ctrmid2(df1.iloc[i])
        df1['mid1countered'].iloc[i] = ctrmid1(df1.iloc[i])
        df1['carry2countered'].iloc[i] = ctrcarry2(df1.iloc[i])
        df1['carry1countered'].iloc[i] = ctrcarry1(df1.iloc[i])
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


# In[73]:


positions = ['TOP1', 'TOP2','JUNGLE1', 'JUNGLE2', 'MID1','MID2', 'SUPPORT1', 'SUPPORT2', 'CARRY1', 'CARRY2']


def ranks(df):
    for i in positions:
    
    # rename CARRY as ADC (Attack Damage Carry)
        posit = i.replace('CARRY','ADC')                         
    
    # remove the number that represent the teams. e.g. 'TOP1' -> 'TOP'
        stats_filtered = stats[stats['Role'] == posit[:-1]]
    # develop dict for mapping the tier   
        name_to_tier = dict(zip(stats_filtered['Name'],stats_filtered['Tier'])) 
    # map the tier to each character for their role
        df[i+'Tier'] = df[i].map(lambda x: name_to_tier.get(x.lower(), None))
    df['TOP1Tier']=df['TOP1Tier'].apply(lambda x: d3[x])
    df['TOP2Tier']=df['TOP2Tier'].apply(lambda x: d3[x])
    df['JUNGLE1Tier']=df['JUNGLE1Tier'].apply(lambda x: d3[x])
    df['JUNGLE2Tier']=df['JUNGLE2Tier'].apply(lambda x: d3[x])
    df['MID1Tier']=df['MID1Tier'].apply(lambda x: d3[x])
    df['MID2Tier']=df['MID2Tier'].apply(lambda x: d3[x])
    df['SUPPORT1Tier']=df['SUPPORT1Tier'].apply(lambda x: d3[x])
    df['SUPPORT2Tier']=df['SUPPORT2Tier'].apply(lambda x: d3[x])
    df['CARRY1Tier']=df['CARRY1Tier'].apply(lambda x: d3[x])
    df['CARRY2Tier']=df['CARRY2Tier'].apply(lambda x: d3[x])
    return df.iloc[:, 10:]


# In[74]:


proba = model_lr.predict_proba(x_test)


# In[75]:


def predictor(df, role):
    preds = model_lr.predict_proba(ranks(mod(pd.DataFrame(filler(df, role)[0]))))
    values = {}
    keys = list(filler(df, role)[1])
    for i in range (0, len(keys)):
        values[keys[i]] = preds[i][0]
    sorted_vals = sorted(values.items(), key=lambda x:-x[1])
    return sorted_vals[:5], {'Current': values[list(values.keys())[0]]}


# In[76]:


df = {'TOP1':'Fiora','TOP2':'Galio', 'JUNGLE1': 'Warwick','JUNGLE2': 'Skarner','MID1':'Viktor','MID2':'Ahri','SUPPORT1':'Nami','SUPPORT2':'VelKoz','CARRY1':'Draven','CARRY2':'Jinx'}
predictor(df, 'MID1')
#([('annie', 0.5159242472073283),
#  ('aurelion sol', 0.5159242472073283),
#  ('azir', 0.5159242472073283),
#  ('brand', 0.5159242472073283),
#  ('corki', 0.5159242472073283)],
# {'Current': 0.5102058533461278})

