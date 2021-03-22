import spacy
from spacy.tokens import Span

nlp = spacy.load("es_core_news_sm")
doc = nlp("@BinMad_ Vecino, ven a limpiar mi casa y el arenero del gato y te llevas un extra!")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)