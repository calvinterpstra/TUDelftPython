# -*- coding: utf-8 -*-
"""
ConceptsScore.py       Calc weighted scores for concepts you have 
                       developed in the project. Skip concept for
                       which weight==0, and break altogether when
                       2 or more weights are missing

@author: Bart Gerritsen
"""

# given the scores of a concept;
#            id            scores          weight
scores = [ ['001', [4, 5, 3, 3, 6, 3, 3, 4], 3], 
           ['002', [2, 2, 5, 5, 5, 6, 4, 4], 4],
           ['003', [4, 2, 2, 5, 5, 6, 1, 4], 1],
           ['004', [5, 2, 5, 4, 5, 7, 4, 4], 0],
           ['005', [3, 2, 2, 4, 4, 4, 5, 4], 3] ]

# EXPERIMENT: try to enforce breaks and continues ...
# set weights=0; 2 or more missing--> break
missing = 0
for concept in range(len(scores)):
    id     = scores[concept][0]
    weight = scores[concept][2]
    scored = scores[concept][1] # a list
    if weight == 0:
        missing +=1
        # permit max 2 missing weights; otherwise break ...
        if missing > 2:
            print('BREAK: 2 or more weights missing.')
            break
        else:
            print('SKIPPING: {:s}; missing weight.'.format(id))
            continue
    # now we can safely calculate the weighted score
    scoreSum = 0
    for s in scored:
        scoreSum += s
    scoreSum /= weight
    print('Concept {:3s} weighted score: {:6.3f}'.format(id,scoreSum))

print('Done ({:d} weights missing).'.format(missing))
    
    