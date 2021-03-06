# Only drop columns which have at least 90% non-NaNs
df.dropna(thresh=int(tube.shape[0] * 1), axis=1)

# Filter dataframe to VIEW NaNs
def view_nans(df):
    return df[df.isnull().any(axis=1)]

# Filter dataframe to REMOVE NaNs
def remove_nans(df):
    return df[~(df.isnull().any(axis=1))].reset_index(drop=True)
