#%%
import pandas as pd
#%%
inst = pd.read_csv('gen/pku_inst.csv')
quest = pd.read_csv('gen/pku_quest.csv')
#%%
inst_mask = inst['completion'].apply(lambda x: x.capitalize()).apply(lambda x: x.startswith("I'm sorry") or x.startswith("I am sorry"))
quest_mask = quest['completion'].apply(lambda x: x.capitalize()).apply(lambda x: x.startswith("I'm sorry") or x.startswith("I am sorry"))
#%%
inst.loc[inst_mask].to_csv('gen/inst_filt.csv', index=False)
quest.loc[quest_mask].to_csv('gen/quest_filt.csv', index=False)
# %%
