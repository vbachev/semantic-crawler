# This file uses the natural language processing toolkit to parse the 
# crawled summary text and derive it's adjectives and nouns 
import nltk

# word categories from the Brown tagset that represent 
# nouns and adjectives
adjectiveTags = [ 'JJ', 'JJR', 'JJS', 'JJT' ]
nounTags = [ 'NN', 'NNP', 'NNS', 'NNPS' ]

def parse ( data ):
    # tokenize and tag the summary text
    words = nltk.tokenize.word_tokenize( data['summary'] )
    taggedWords = nltk.pos_tag( words )
    
    # take out nouns and adjectives
    nouns = []
    adjectives = []
    for item in taggedWords:
        if item[1] in adjectiveTags:
            adjectives.append( item[0] )
        elif item[1] in nounTags:
            nouns.append( item[0] )

    # set the unique values as concatenated CSV
    data['nouns'] = ','.join( list( set( nouns )))
    data['adjectives'] = ','.join( list( set( adjectives )))