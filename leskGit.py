bank_sents = ['I went to the bank to deposit my money',
'The river bank was full of dead fishes']

plant_sents = ['The workers at the industrial plant were overworked',
'The plant was no longer bearing flowers']

print "======== TESTING simple_lesk ===========\n"
from pywsd.lesk import simple_lesk
print "#TESTING simple_lesk() ..."
print "Context:", bank_sents[0]
answer = simple_lesk(bank_sents[0],'bank')
print "Sense:", answer
definition = answer.definition() 
#except: definition = answer.definition # Using older version of NLTK.
print "Definition:", definition
print ''

print "#TESTING simple_lesk() with POS ..."
print "Context:", bank_sents[1]
answer = simple_lesk(bank_sents[1],'bank','n')
print "Sense:", answer
definition = answer.definition() 
#except: definition = answer.definition # Using older version of NLTK.
print "Definition:", definition
print

print "#TESTING simple_lesk() with POS and stems ..."
print "Context:", plant_sents[0]
answer = simple_lesk(plant_sents[0],'plant','n', True)
print "Sense:", answer
definition = answer.definition()
#except: definition = answer.definition
print "Definition:", definition
print

print "#TESTING simple_lesk() with nbest results" # i.e. output ranked synsets.
print "Context:", plant_sents[0]
answer = simple_lesk(plant_sents[0],'plant','n', True, nbest=True)
print "Senses ranked by #overlaps:", answer
best_sense = answer[0]
definition = best_sense.definition() 
#except: definition = best_sense.definition
print "Definition:", definition
print

print "#TESTING simple_lesk() with nbest results and scores"
print "Context:", plant_sents[0]
answer = simple_lesk(plant_sents[0],'plant','n', True, \
                     nbest=True, keepscore=True)
print "Senses ranked by #overlaps:", answer
best_sense = answer[0][1]
definition = best_sense.definition()
#except: definition = best_sense.definition
print "Definition:", definition
print

print "#TESTING simple_lesk() with nbest results and normalized scores"
print "Context:", plant_sents[0]
answer = simple_lesk(plant_sents[0],'plant','n', True, \
                     nbest=True, keepscore=True, normalizescore=True)
print "Senses ranked by #overlaps:", answer
best_sense = answer[0][1]
definition = best_sense.definition() 
#except: definition = best_sense.definition
print "Definition:", definition
print

print "======== TESTING adapted_lesk ===========\n"
from pywsd.lesk import adapted_lesk

print "#TESTING adapted_lesk() ..."
print "Context:", bank_sents[0]
answer = adapted_lesk(bank_sents[0],'bank')
print "Sense:", answer
definition = answer.definition()
#except: definition = answer.definition
print "Definition:", definition
print

print "#TESTING adapted_lesk() with pos, stem, nbest and scores."
print "Context:", bank_sents[0]
answer = adapted_lesk(bank_sents[0],'bank','n', True, \
                     nbest=True, keepscore=True)
print "Senses ranked by #overlaps:", answer
best_sense = answer[0][1]
definition = best_sense.definition() 
#except: definition = best_sense.definition
print "Definition:", definition
print