import numpy
import os
import matplotlib.pyplot as plt
%matplotlib inline

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
print(ratio)

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
plt.rcParams['figure.figsize'] = (10.0, 6.0) # 设置figure_size尺寸
rects=plt.bar(range(0,3*len(num_list),3), num_list, color='lightskyblue',width=2)
# X轴标题
index=list(range(0,3*len(num_list),3))
index=[float(c)+0 for c in index]
plt.ylim(ymax=450, ymin=0)

plt.xticks(index, name_list)
plt.xlabel('Company',font2)
plt.ylabel("Number of Problems",font2) #X轴标签
plt.title('Number of Problems on LeetCode from different companies',font1)
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
plt.savefig('problem_num_of_different_companies')
plt.show()
