import nltk

adjectiveTags = [ 'JJ', 'JJR', 'JJS', 'JJT' ]
nounTags = [ 'NN', 'NNP', 'NNS', 'NNPS' ]

def parse ( data ):
    words = nltk.tokenize.word_tokenize( data['summary'] )
    taggedWords = nltk.pos_tag( words )
    
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