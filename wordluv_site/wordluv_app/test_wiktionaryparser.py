# https://github.com/Suyash458/WiktionaryParser
# https://gist.github.com/nichtich/674522 (js)
# https://wiki.fluidproject.org/display/fluid/Online+Dictionary+APIs+-+Options+and+Thoughts
'''
STRUCTURE
[{
    "pronunciations": {
        "text": ["pronunciation text"],
        "audio": ["pronunciation audio"]
    },
    "definitions": [{
        "relatedWords": [{
            "relationshipType": "word relationship type",
            "words": ["list of related words"]
        }],
        "text": ["list of definitions"],
        "partOfSpeech": "part of speech",
        "examples": ["list of examples"]
    }],
    "etymology": "etymology text",
}]
'''

from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

word = parser.fetch('moindre', 'french')

print(word)

parser.set_default_language('french')
another_word = parser.fetch('produit')
print(another_word)