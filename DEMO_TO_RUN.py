import numpy
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import string
import wordcloud
from wordcloud import WordCloud
from stop_words import get_stop_words
import shapefile as shp
import seaborn as sns
import plotly
import geopandas as gpd
from shapely.geometry import Point, Polygon
import plotly.plotly as py
import plotly.graph_objs as go

folder_name='company_folder'

def count_each_companys_problem(folder_name='company_folder'):
    '''
    This function count the problem numbers of a given company
    Para: folder_name: the folder that contains the data of different companies
    Return: a dictionary showing different companies' problem 
    '''
    assert isinstance(folder_name,str)
    company_txt_list=os.listdir(folder_name)
    print(company_txt_list)
    count_problems={}
    for company in company_txt_list:
        file=open('company_folder/'+company,'r')
        lines=file.readlines()
        company_name=company.split('.')[0]
        company_name=company_name[23:]
        count_problems[company_name]=len(lines)
        file.close()
    return count_problems

ratio=count_each_companys_problem(folder_name)
ratio_sort=sorted(ratio.items(),key=lambda x: x[1],reverse=True)
companies=[]
values=[]
for term in ratio_sort:
    companies.append(term[0])
    values.append(term[1])
	
	
name_list = companies
num_list = values
font1={'size'   : 15}
font2={'size'   : 15}
plt.rcParams['figure.figsize'] = (10.0, 6.0) # set figure_size
rects=plt.bar(range(0,3*len(num_list),3), num_list, color='lightskyblue',width=2)
# X axis's label
index=list(range(0,3*len(num_list),3))
index=[float(c)+0 for c in index]
plt.ylim(ymax=450, ymin=0)

plt.xticks(index, name_list)
plt.xlabel('Company',font2)
plt.ylabel("Number of Problems",font2) 
plt.title('Number of Problems on LeetCode from different companies',font1)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
# plt.savefig('problem_num_of_different_companies')
plt.show()

folder_name='output_AllQus'
def extract_companys_problems(company=None):
    '''
    This function extract the problems a given company
    Para: company: the given company's name 
    Return: a dictionary showing different companies' problems' difficulty and tag
    '''
    assert isinstance(company,str)
    tag_ratio=dict()
    difficulty_ratio=dict()
    all_questions_folder='output_AllQus'
    folders_in_all_questions_folder=os.listdir(folder_name)
    file_name='company_folder/'+'leetcode_links_company_'+company+'.txt'
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
company_name2='microsoft'
company_tag,company_difficulty=extract_companys_problems(company_name2)
print(company_difficulty)

top_labels=[]
top_values=[]
top_num=8
company_sorted=sorted(company_tag.items(),key=lambda x:x[1],reverse=True)
for term in company_sorted[0:top_num]:
    top_labels.append(term[0])
    top_values.append(term[1])
###### Plot the figure of tags' ratio
explode=[0]*top_num
explode[0]=0.1
plt.rcParams['figure.figsize'] = (5.0, 5.0) # 设置figure_size尺寸
plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
#autopct ，show percet
plt.pie(x=top_values, labels=top_labels, explode=explode,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6
        )
plt.title('Top {} hot problems in {}'.format(top_num,company_name2.upper()))
# plt.savefig('Pie chart of most asked problems in {}'.format(company_name2.upper()))
plt.show()

####### Plot the figure of difficulties' ratio
explode_diff=[0]*3
explode_diff[0]=0.1
plt.axes(aspect=1)  
plt.pie(x=company_difficulty.values(), labels=company_difficulty.keys(), explode=explode_diff,autopct='%3.1f %%',
        shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6
        )
plt.title('Difficulties of The Problems In {}'.format(company_name2.upper()))
# plt.savefig('Pie chart of Difficulties of problems in {}'.format(company_name2.upper()))
plt.show()

file=pd.read_csv('Dice_US_jobs_utf81.csv',error_bad_lines=False)
print(file.columns)
word_freq={}
for job in file['job_title']:
    try:
        job=job.translate(str.maketrans('', '', string.punctuation))
        words=job.split()
        for word in words:
            if word in word_freq:
                word_freq[word]=word_freq[word]+1
            else:
                word_freq[word]=1
    except:
        pass
most_freq=sorted(word_freq.items(),key=lambda x: x[1],reverse=True)[0:40]
most_freq=dict(most_freq)
print(dict(most_freq))

wc = WordCloud(background_color='white',
               width=4000,
               height=3200,
               ).generate_from_frequencies(most_freq)
# wc.to_file('jobcloud.png') 
plt.imshow(wc) 
plt.axis('off') 
plt.show() 

file=pd.read_csv('Dice_US_jobs_utf81.csv',error_bad_lines=False)
location=dict()
states_list=['AK','AR','AZ','CA','FL','LA','NM','NV','OK','OR','TX','UT','AL','CO','CT','DE','GA','IA',
            'ID','IL','IN','KS','KY','MA','WI','MD','ME','MI','MN','MO','MS',
            'MT','NC','ND','NE','NH','NJ','NY','OH','PA','WV','RI','SC','SD',
            'TN','VA','VT','WA','WY','HI','RL']
for term in file['location']:
    
    try:
        location_cur=term.split(', ')[1]
    except:
        pass
    location_cur=location_cur.upper()
    if location_cur in states_list:
        if location_cur in location:
            location[location_cur]=location[location_cur]+1
        else:
            location[location_cur]=1
for temp_state in states_list:
    if temp_state not in location:
        location[temp_state]=1
print(location)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]


data = [go.Choropleth(
    autocolorscale = True,
    locations=list(location.keys()),
    z=list(location.values()),
    locationmode = 'USA-states',
    visible=True,
    text=list(location.values()),
    hovertext=list(location.values()),
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "Number of Jobs")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = '2017 US Jobs On Monster.com'
    ),
    hovermode='closest',
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
        legend = go.layout.Legend(
           traceorder = 'reversed'
    )
)

fig = go.Figure(data = data, layout = layout)
plotly.offline.plot(fig, filename = 'd3-cloropleth-map')

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
total.head(5)

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