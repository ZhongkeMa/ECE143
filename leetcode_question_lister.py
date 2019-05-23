'''
Utility script to parse links in the raw logs and extract all links for problems
'''

fname = 'leetcode_links_raw.log'
foutput = 'leetcode_links_problems.txt'
with open(fname, 'r') as links_raw:
	content = links_raw.readlines()

valid_links = ''
for line in content:
	link = line.split('js:149 ',1)[-1]
	if 'https://leetcode.com/problems/' in link: valid_links+=f'{link.strip()}\n'

with open(foutput,'w') as links_valid:
	links_valid.write(valid_links)
	

	
