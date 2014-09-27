#!/usr/bin/env python
import mincemeat
import glob

text_files = glob.glob('hw3data/*')
# stop_words = glob.glob('stopwords.py')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
              for file_name in text_files)



data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    stopwords = open('stopwords.py').read()
    for w in v.split('\n'):
        w2 = w.split(':::')
        if len(w2) < 3:
            continue
        # print len(w2)
        titleWords = w2[2].split(' ')
        cleanedWords = []
        
        
        for titleWord in titleWords:
            titleWord = ''.join(e for e in titleWord if (e.isalnum() or e == '-'))
            titleWord = titleWord.replace('-', ' ')
            if (len(titleWord) > 1 and not (titleWord in stopwords)):
                cleanedWords.append(titleWord)
        
    #print cleanedWords
    #    print titleWords
    
        for writer in w2[1].split('::'):
            #       print writer
            # writers = w2[1].split('::')
            # print writers
            for cleanedWord in cleanedWords:
                key = writer + ':' + cleanedWord
                #   print key
                yield key, 1

def reducefn(k, vs):
    result = sum(vs)
    return result



s = mincemeat.Server()
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
f1 = open('./results.txt', 'w+')
print >> f1, results
f1.close

#print results
