import collections, string, re, math

stopWords = ['a','T','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or'
                           ]
queries = collections.defaultdict(dict)
words_query = collections.defaultdict(dict)
documents = collections.defaultdict(dict)
query_scores = collections.defaultdict(dict)
abstracts = collections.defaultdict(dict)
abstract_words = collections.defaultdict(dict)

with open("cran.qry") as f:
    i = 0
    query = []
    in_query = False
    for line in f:
        tok = line
        ids = ""
        ids = tok[0] + tok[1]
        if ids == ".W":
            i  = i + 1
            in_query = True
        elif ids == ".I":
            queries[i] = query
            #print(query)
            query = []
            in_query = False
        elif in_query:
            tok = re.findall(r'[a-zA-Z]+', tok)
            tok2 = []
            for item in tok:
                if item not in stopWords:
                    tok2.append(item)
                
            query = query + tok2
    queries[225] = query

for query in queries:
    sentence = queries[query]
   
    for words in sentence:
        
        if words in words_query:
            words_query[words] += 1
        else:
            words_query[words] = 1


def queryCalc():
    for query in queries:
        sen = queries[query]
        for word in sen:
            idf_score = (math.log(225/(words_query[word])))
            tf_score = sen.count(word)
            query_scores[query][word] = [idf_score * tf_score]
 
with open("cran.all.1400") as f:
    i = 0
    abstract = []
    in_aabstract = False
    for line in f:
        li = line
        ids = ""
        ids = li[0] + li[1]
        if ids == ".W":
            
            in_abstract = True
        elif ids == ".I":
            abstracts[i] = abstract
            i  = i + 1
            #print(query)
            abstract = []
            in_abstract = False
        elif in_query:
            pattern = r'[a-zA-Z]+'
            li = re.findall(pattern, li)
            li2 = []
            for item in li:
                if item not in stopWords:
                    li2.append(item)
            li2 = [i for i in li2 if len(i) > 1]

            abstract = abstract + li2
    abstracts[1400] = abstract
'''
def abstractCalc():
    for abstract in abstracts:
        bag = queries[query]
        for word in bag:
            idf_score = (math.log(225/(words_query[word])))
            tf_score = sen.count(word)
            query_scores[query][word] = [idf_score * tf_score]    
'''  
for abstract in abstracts:
    for word in abstracts[abstract]:
        for x in abstracts:
            if word in abstracts[x]:
                print(abstracts[abstract][word])
                
#queryCalc()

#print(query_scores[220])

print(abstracts[1400])