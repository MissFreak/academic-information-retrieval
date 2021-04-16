# 获取ACL前100篇top cited文章，ACL.html是在aminer下载的（地址是https://www.aminer.cn/conference/5eeb1307b5261c744f15bd9a）

import re
with open('D:/documents/tools/html/ACL.html', encoding='utf-8') as f:
    html = f.read()
# print('读取到以下html内容：{}...'.format(html[:20]))

lst = re.split('</?script.*>', html)
for string in lst:
	if "g_initialProps" in string:
		json_file = re.sub('undefined', '"undefined"', string.split(';', 1)[1].split('= ')[-1].rsplit(';', 1)[0])

dict_json = json.loads(json_file)
top_cited_papers = dict_json['rank']['confInfo']['top_cited_papers']

lst_of_ids = [paper['id'] for paper in top_cited_papers]
lst_of_titles = [paper['title'] for paper in top_cited_papers]
lst_of_num_citations = [paper['num_citation'] for paper in top_cited_papers]

import pandas as pd
df = pd.DataFrame(list(zip(lst_of_ids, lst_of_titles, lst_of_num_citations)),columns =['id', 'title', 'citation'])
df.to_csv('D:/documents/tools/html/top_cited_papers.csv')
