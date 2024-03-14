import pickle
import os
from collections import Counter
import pandas as pd

df = pd.DataFrame(columns=['value','count'])


file = open(r"/home/gourav/projects/deepparse-address-data/testINdata_decom/address_data/clean_data/india_address/in.p", "rb")

data = pickle.load(file)

count = 0
# Storing all the words
newWordsList = []

for d in data :
    # print(d[0])

    newWordsList.extend(d[0].split()) 
    count += 1
    

    

wordsFrequency = dict(Counter(newWordsList))

sort_list = sorted(wordsFrequency.items(), key=lambda x:x[1])[-500:]
sort_list.reverse()

for tup in sort_list:
    val = tup[0]
    count = tup[1]

    df2 = {'value':val,
            'count':count
            }
    df = df.append(df2, ignore_index = True)

print("\n\n", "\n\n",sort_list,"\n\n",len(wordsFrequency), "\n\n",len(newWordsList), )
df.to_excel("most_freq_words.xlsx")
