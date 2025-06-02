import pandas as pd
df = pd.read_csv("Medicaldataset.csv.csv")  
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)


print(df.isnull().sum())    #missing values

df = df.dropna()            #drop missing vals

print(df.duplicated().sum())        #check for duplicates
df = df.drop_duplicates()

df['Result'] = df['Result'].str.strip().str.upper()

if 'age' in df.columns:
    df['age'] = df['age'].astype(int)

df = df.drop('CK-MB', axis=1)       #delete a row


cleaned_path = "cleaned_medicaldataset.csv"
df.to_csv(cleaned_path, index=False)
print("\nCleaned dataset saved to:", cleaned_path)      #save the new cleaned data

print("\nFinal Shape:", df.shape)