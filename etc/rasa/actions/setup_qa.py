import time
from googlesearch import search
from newspaper import Article
#from transformers import pipeline

#def question_answering_pipeline(query):
#    qa_pipeline = pipeline("question-answering",
#                           model="mrm8488/bert-multi-cased-finetuned-xquadv1",
#                           tokenizer="mrm8488/bert-multi-cased-finetuned-xquadv1"
#                          )
#    return qa_pipeline({'context': final_text(query),'question': query})["answer"]

def search_article(query):
    my_results_list = []
    for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'ru',  # The language
                num = 5,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = 3,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
        my_results_list.append(i)
    return my_results_list

def extract_text(url):
    article = Article(url, language='ru')
    article.download()
    article.parse()
    return article.text.replace("\n"," ")

def final_text(query):
    if len(extract_text(search_article(query)[0]))<100:
        return extract_text(search_article(query)[1])[:10000]
    else:
        return extract_text(search_article(query)[0])[:10000]