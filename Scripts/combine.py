import pandas as pd

old = pd.read_csv('../Dataset Parts/nuforc_events_old.csv')
new = pd.read_csv('../Dataset Parts/nuforc_events_new.csv')

combined = pd.concat([new, old])
# summary column was chosen in case there were
# differences in duplicates between tables.
combined.drop_duplicates(subset = ['summary'], inplace = True)

combined.to_csv('nuforc_events_complete.csv')