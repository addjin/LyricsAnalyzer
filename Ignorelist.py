ARTICLES = ['a', 'an', 'the']
PRONOUNS = ['I', 'you', 'he', 'she', 'it', 'we', 'they']
PRONOUNS_POSSESIVE = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']
DETERMINERS_POSSESIVE = ['my', 'your', 'his', 'her', 'its', 'our', 'their']
DETERMINERS_DEMONSTRATIVE = ['this', 'that', 'these', 'those']

PREPOSITIONS = ['aboard', 'about', 'above', 'across', 'after', 'against', 
'along', 'amid', 'among', 'around', 'as', 'at', 'before', 'behind', 'below', 
'beneath', 'beside', 'between', 'beyond', 'but', 'by', 'concerning', 'considering', 
'despite', 'down', 'during', 'except', 'following', 'for', 'from', 'in', 'inside', 'into', 'like', 'minus', 
'near', 'next', 'of', 'off', 'on', 'onto', 'opposite', 'out', 'outside', 'over', 'past', 'per', 'plus', 
'regarding', 'round', 'save', 'since', 'than', 'through', 'till', 'to', 'toward', 'under', 'underneath', 
'unlike', 'until', 'up', 'upon', 'versus', 'via', 'with', 'within', 'without']

def is_exception_word(word, ignorearticles=False, ignorepronouns=False, ignoredeterminers=False, ignoreprepositions=False):
    if not ignorearticles and (word in ARTICLES):
        return True
    
    if not ignorepronouns and (word in PRONOUNS + PRONOUNS_POSSESIVE):
        return True

    if not ignoredeterminers and (word in DETERMINERS_POSSESIVE + DETERMINERS_DEMONSTRATIVE):
        return True

    if not ignoreprepositions and (word in PREPOSITIONS):
        return True

    return False
