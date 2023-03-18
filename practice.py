import urllib.request
import re
import nltk
from inscriptis import get_text
from nltk import word_tokenize, sent_tokenize

#nltk.download()

text = "Real Madrid Club de Fútbol, meaning Royal Madrid Football Club), commonly referred to as Real Madrid, is a Spanish professional football club based in Madrid. Founded in 1902 as Madrid Football Club, the club has traditionally worn a white home kit since its inception. The honorific title real is Spanish for royal and was bestowed to the club by King Alfonso XIII in 1920 together with the royal crown in the emblem. Real Madrid have played their home matches in the 81,044-capacity Santiago Bernabéu Stadium in downtown Madrid since 1947. Unlike most European sporting entities, Real Madrid's members (socios) have owned and operated the club throughout its history. Real Madrid is one of the most widely supported teams internationally. The club was estimated to be worth $5.1 billion in 2022, making it the world's most valuable football team. In 2021, it was the second highest-earning football club in the world, with an annual revenue of €640.7 million. Being one of the three founding members of La Liga that have never been relegated from the top division since its inception in 1929 (along with Athletic Bilbao and Barcelona), Real Madrid holds many long-standing rivalries, most notably El Clásico with Barcelona and El Derbi Madrileño with Atlético Madrid. The club established itself as a major force in both Spanish and European football during the 1950s and 60s, winning five consecutive and six overall European Cups and reaching a further two finals. This success was replicated on the domestic front, with Madrid winning twelve league titles in the span of 16 years. This team, which included Alfredo Di Stéfano, Ferenc Puskás, Francisco Gento, and Raymond Kopa, is considered by some in the sport to be the greatest of all time. In domestic football, the club has won 68 trophies; a record 35 La Liga titles, 19 Copa del Rey, 12 Supercopa de España, a Copa Eva Duarte, and a Copa de la Liga. In European football, Real Madrid have won a record 21 trophies; a record 14 European Cup/UEFA Champions League titles, two UEFA Cups, and a record five UEFA Super Cups. In worldwide competitions, they have achieved a record eight club world championships. Real Madrid was recognised as the FIFA Club of the 20th Century on 11 December 2000 with 42.35% of the vote, and received the FIFA Centennial Order of Merit on 20 May 2004. The club was also named Best European Club of the 20th Century by the IFFHS on 11 May 2010. In June 2017, Madrid succeeded in becoming the first club to win consecutive titles in the Champions League era. In May 2022, they won a record-extending fourteenth European Cup, making it five titles in the last nine seasons. As of December 2022, Real Madrid are ranked sixth behind Manchester City, Bayern Munich, Liverpool, Chelsea and Paris Saint-Germain in the UEFA club rankings."

#Removing square brackets and extra spaces


sentence_list = nltk.sent_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

#CALCULA LA FRASE QUE MAS SE REPITE
sentence_scores ={}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in  sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#REALIZA EL RESUMEN CON LAS MEJORES FRASES
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)

from googletrans import Translator
translator = Translator()
textTranslate = translator.translate(summary, src='en',dest='es')

# from gtts import gTTS
# import os
# myobj = gTTS(text=textTranslate.text, lang='es', slow=False)
# myobj.save("resume.mp3")
# os.system("resume.mp3")

import pyttsx3

engine = pyttsx3.init()
engine.say(textTranslate.text)
engine.runAndWait()

print(textTranslate.text)