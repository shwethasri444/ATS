import csv
import pandas
import numpy as np
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import gensim
from pandas.io.json import json_normalize
import json


def doc_sim(jd_data):
	columns=["NAME","CONTACT","EMAIL","SKILLS","WORK HISTORY"]
	# with open('C://Users//admin//heirs//jd_data.json') as json_data:
	# 	jd_data = json.load(json_data)
	print(type(jd_data))
	print(json.dumps(jd_data, indent=4, sort_keys=False))
	resume_db = pandas.read_csv('C:\\Users\\admin\\Desktop\\shwetha\\resume\\db.csv',names=columns)
	new_jd = pandas.DataFrame.from_dict(json_normalize(jd_data),orient='columns')
	print(type(new_jd))
	row_count=new_jd.shape[0]
	print(row_count)
	JD=new_jd.iloc[0].to_dict()

	print(JD)
	print(type(JD))

	from gensim import corpora
	resume_skills = resume_db["SKILLS"]
	skill_list = []
	for i in range(len(resume_db["SKILLS"])):
		skill_list.append(resume_db.iloc[i]["SKILLS"])
	stoplist = set('for a of the and to in on all an * % I have can'.split())
	texts = [[word for word in skill.lower().split() if word not in stoplist]
			  for skill in skill_list]

	skill_dic = corpora.Dictionary(texts)

	skill_corpus = [skill_dic.doc2bow(text) for text in texts]
	from gensim import models,similarities

	tfidf = models.TfidfModel(skill_corpus,normalize=True)
	skill_corpus_tfidf = tfidf[skill_corpus]

	skills_jd = JD["skills"]

	lsi = models.LsiModel(skill_corpus, id2word=skill_dic, num_topics=2)

	vec_corpus=[skill_dic.doc2bow(skills_jd.lower().split())]
	vec_lsi = lsi[vec_corpus]

	index = similarities.MatrixSimilarity(lsi[skill_corpus])
	sims = index[vec_lsi]

	flat_list = [item for sublist in list(sims) for item in sublist]
	ranked_sims = sorted(enumerate(flat_list), key=lambda item: -item[1])
	top_ten_resumes = ranked_sims[:10]
	d= pandas.DataFrame(top_ten_resumes,columns=["key","val"])
	ranked_indices = d["key"]
	print(list(ranked_indices))

	results = resume_db.iloc[list(ranked_indices)]
	# results_list=list(results.values.T.flatten())
	# print(type(results_list))
	results_json = results.to_json(orient='records')
	python_obj=json.loads(results_json)
	print(type(python_obj))
	print(json.dumps(python_obj,indent=4))

	# json.dump(python_obj,open("C://Users//admin//heirs//result_resume.json","w"))
	return python_obj
# results_json = json.dumps(results_list,indent=4)
# print(json.dumps(results_list,indent=4))
# print(type(results_json))














































































































































































