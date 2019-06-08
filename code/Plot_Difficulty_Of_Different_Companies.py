import numpy
import os
import matplotlib.pyplot as plt
import pandas
folder_name='output_AllQus'
def extract_companys_problems(company=None):
	'''
	this function extracts problems of each company from the raw data
	'''
    tag_ratio=dict()
    difficulty_ratio=dict()
    all_questions_folder='output_AllQus'
    folders_in_all_questions_folder=os.listdir(folder_name)
    file_name='leetcode_links_company_'+company+'.txt'
    file=open(file_name,'r')
    for line in file:
        problem_name=line[30:-2]
        for term in folders_in_all_questions_folder:
            if problem_name in term:
                
                description_problem=open(all_questions_folder+'/'+term+'/README.md','r',encoding='utf-8')
                
                for line2 in description_problem:
                    if '**Tags:**' in line2:
                        tag_list=line2[10:-1].split(', ')
                        for tag in tag_list:
                            if tag in tag_ratio:
                                tag_ratio[tag]=tag_ratio[tag]+1
                            else:
                                tag_ratio[tag]=1
                    if '**Difficulty:**' in line2:
                        difficulty=line2[16:-1]
                        if difficulty in difficulty_ratio:
                            difficulty_ratio[difficulty]=difficulty_ratio[difficulty]+1
                        else:
                            difficulty_ratio[difficulty]=1
                description_problem.close()
                break
    file.close()
    return tag_ratio,difficulty_ratio
	
import pandas as pd
def company_question():
    df = pd.DataFrame()
    Companies=['google', 'amazon', 'apple','facebook','linkedin','microsoft']
   
    for com in Companies:
        companies_tag,companies_difficulty=extract_companys_problems(company=com)
        total=sum(companies_tag.values())
        companies_tag = {k: v / total for k, v in companies_tag.items()}
        companies_difficulty = {l: w / total for l, w in companies_difficulty.items()}
        print(total)
        df1 = pd.DataFrame.from_dict(companies_difficulty, orient = 'index',columns = [com])
        df2 = pd.DataFrame.from_dict(companies_tag, orient = 'index',columns = [com])
        df1 = pd.concat([df1,df2],axis = 0,sort = True)
        df = pd.concat([df,df1], axis=1, join_axes=[df1.index])
    #print(df)
    df.to_csv(r'company_dataframe.csv')
    return df
	
def plot_company():
    total = pd.read_csv('company_dataframe.csv',index_col = 0)
	
	
total = pd.read_csv('company_dataframe.csv',index_col = 0)

import matplotlib.pyplot as plt
import numpy as np
x = list(total.columns.values)
print(x)
y = list(total.values)[0:3]
print(y)
x1 = np.arange(len(x))
wid = 0.2
print(len(list(total.values)[0:3][0]),'len')
ax = plt.subplot(111)
#plt.figure(figsize = (20,12))
ax.bar(x1-wid, list(total.values)[0:3][0],color = 'g',width=0.4,align='center',label = 'Easy')
ax.bar(x1, list(total.values)[0:3][1],color = 'b',width=0.4,align='center',label = 'Medium')
ax.bar(x1+wid, list(total.values)[0:3][2],color = 'r',width=0.4,align='center',label = 'Hard')
# ax.set_xticklabels(x)
plt.xticks([0,1,2,3,4,5,],x)
ax.autoscale_view()
plt.legend()
plt.xlabel("company",fontsize=18)
plt.ylim([0,0.35])
plt.ylabel("Percentage",fontsize=18)
plt.title("Bar plot of difficulty for different company",fontsize=20)
plt.show()
