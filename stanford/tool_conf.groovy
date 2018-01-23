def tokenizer = 'stanford/tokenizer_2.1.0.xml'
def splitter  = 'stanford/splitter_2.1.0.xml'
def tagger = 'stanford/tagger_2.1.0.xml'
def names = 'stanford/ner_2.1.0.xml'
def parser = 'stanford/parser_2.1.0.xml'
def depparser = 'stanford/depparser_2.1.0.xml'
def coref = 'stanford/coref_2.1.0.xml'

stanford 'Stanford NLP', {
	tools tokenizer, splitter, tagger, names, parser, depparser, coref
}

tokenizers { tool tokenizer }
splitters { tool splitter }
taggers { tool tagger }
ner { tool names }
parsers { tool parser }
// depparser { tool depparser }
// coref { tool coref }
 
