'''
Utility script to parse links in the raw logs and extract all links for problems
'''

def extract_all_problems(fname = '.\log\leetcode_links_raw.log'):
	fsuffix = fname.split('leetcode_links_raw',1)[-1]
	fsuffix = fsuffix.split('.log',1)[0]
	foutput = f'leetcode_links_problems{fsuffix}.txt'
	with open(fname, 'r') as links_raw:
		content = links_raw.readlines()

	valid_links = []
	for line in content:
		link = line.split('js:149 ',1)[-1]
		if 'https://leetcode.com/problems/' in link:
			current_link = f'{link.strip()}\n'
			if current_link not in valid_links: valid_links.append(current_link)

	with open(foutput,'w') as links_valid:
		for lines in valid_links: links_valid.write(lines)
	

def extract_all_tags(fname = '.\log\leetcode_links_raw.log'):
	foutput = 'leetcode_links_tags.txt'
	with open(fname, 'r') as links_raw:
		content = links_raw.readlines()

	valid_links = []
	for line in content:
		link = line.split('js:149 ',1)[-1]
		if 'https://leetcode.com/tag/' in link:
			current_link = f'{link.strip()}\n'
			if current_link not in valid_links: valid_links.append(current_link)

	with open(foutput,'w') as links_valid:
		for lines in valid_links: links_valid.write(lines)
	
def extract_all_companies(fname = '.\log\leetcode_links_raw.log'):
	foutput = 'leetcode_links_companies.txt'
	with open(fname, 'r') as links_raw:
		content = links_raw.readlines()

	valid_links = []
	for line in content:
		link = line.split('js:149 ',1)[-1]
		if 'https://leetcode.com/company/' in link:
			current_link = f'{link.strip()}\n'
			if current_link not in valid_links: valid_links.append(current_link)

	with open(foutput,'w') as links_valid:
		for lines in valid_links: links_valid.write(lines)
		
def extract_problems_from_tags(fname = 'leetcode_links_tags.txt'):
	with open(fname,'r') as tag_directory:
		tag_links = tag_directory.readlines()
	
	count = 1
	for line in tag_links:
		fsuffix = line.split('https://leetcode.com/tag/',1)[-1]
		fsuffix = fsuffix[:-2]
		#print(fsuffix)
		foutput = f'leetcode_links_tag_{fsuffix}.txt'
		
		with open(f'./log/{count}.log', 'r') as links_raw:
			content = links_raw.readlines()

		valid_links = []
		for line in content:
			link = line.split('js:149 ',1)[-1]
			if 'https://leetcode.com/problems/' in link: 
				current_link = f'{link.strip()}\n'
				if current_link not in valid_links: valid_links.append(current_link)

		with open(foutput,'w') as links_valid:
			for lines in valid_links: links_valid.write(lines)
	count = count+1
	
def extract_problems_from_company(fname = 'leetcode_links_companies.txt'):
	with open(fname,'r') as tag_directory:
		tag_links = tag_directory.readlines()
	
	count = 1
	for line in tag_links:
		fsuffix = line.split('https://leetcode.com/company/',1)[-1]
		fsuffix = fsuffix[:-2]
		#print(fsuffix)
		foutput = f'leetcode_links_company_{fsuffix}.txt'
		
		with open(f'./log/c{count}.log', 'r') as links_raw:
			content = links_raw.readlines()

		valid_links = []
		for line in content:
			link = line.split('js:149 ',1)[-1]
			if 'https://leetcode.com/problems/' in link: 
				current_link = f'{link.strip()}\n'
				if current_link not in valid_links: valid_links.append(current_link)

		with open(foutput,'w') as links_valid:
			for lines in valid_links: links_valid.write(lines)
		count = count+1
		if count==11: break


extract_all_problems()
extract_all_tags()
extract_all_companies()
extract_problems_from_tags()
extract_problems_from_company()