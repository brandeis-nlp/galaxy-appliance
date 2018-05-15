def tokenizer = 'stanford/tokenizer_3.0.0.xml'
def splitter  = 'stanford/splitter_3.0.0.xml'
def tagger = 'stanford/tagger_3.0.0.xml'
def names = 'stanford/ner_3.0.0.xml'
def parser = 'stanford/parser_3.0.0.xml'
def depparser = 'stanford/depparser_3.0.0.xml'
def coref = 'stanford/coref_3.0.0.xml'
def relextr = 'stanford/relextr_3.0.0.xml'

stanford 'Stanford NLP', {
	tools tokenizer, splitter, tagger, names, parser, depparser, coref, relextr
}

tokenizers { tool tokenizer }
splitters { tool splitter }
taggers { tool tagger }
ner { tool names }
parsers { tools parser, depparser }
rel_extr { tool relextr }
// coref { tool coref }
 
