String tokenizer = "opennlp/tokenizer.xml"
String splitter = "opennlp/splitter.xml"
String tagger = "opennlp/tagger.xml"
String names = "opennlp/names.xml"
// String coref = "opennlp/coreference.xml"

opennlp 'Apache OpenNLP', {
	tools tokenizer, splitter, tagger, names
}

tokenizers { tool tokenizer }
splitters { tool splitter }
taggers { tool tagger }
ner { tool names }
// coreference 'Coreference Annotators', { tool coref }
