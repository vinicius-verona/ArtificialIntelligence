# Task: Implement an abduction method

def abduction(kb, observation):
    """
        Returns explanation to the observations inputed given a knowledge base.
        PS: Not an efficient implementation
    """
    if not observation:
        return []

    explanation = []
    logicalConsequence = bottom_up(kb)
    observationRules = []

    for obs in observation:
        observationRules += kb["rules"][obs]

    for rule in observationRules:
        isAnExplanation = True
        ruleAtoms = []
        for atom in rule:
            ruleAtoms.append(atom)

            if not (atom in logicalConsequence or atom in kb["assumables"]):
                isAnExplanation = False
                ruleAtoms = []
                break

        if isAnExplanation and not (rule in explanation):
            explanation += [rule]

    return explanation


# The following code has been extracted from https://github.com/rcpsilva/BCC325_ArtificialIntelligence/blob/main/2022-1/Logical%20Agents/logical_agents.py
# And modified in order to fit the task
def bottom_up(kb):
    C = []

    if 'askables' in kb:
        for a in kb['askables']:
            if a in kb["assumables"] or ask(a):
                C.append(a)

    if 'assumables' in kb:
        for a in kb['assumables']:
            if not a in C:
                C.append(a)

    new_consequence = True

    while new_consequence:
        new_consequence = False

        for head in kb['rules']:
            if head not in C:  # Very innefient
                for body in kb['rules'][head]:
                    if not set(body).difference(set(C)):  # Very innefient
                        C.append(head)
                        new_consequence = True

    return C


def ask(askable):
    ans = input(f'Is {askable} true ? ')
    return True if ans.lower() in ['sim', 's', 'yes', 'y'] else False


if __name__ == "__main__":
    kb = {'rules': {'bronchitis': [['influenza'], ['smokes']],
                    'coughing': [['bronchitis']],
                    'wheezing': [['bronchitis']],
                    'fever': [['influenza', 'infection']],
                    'sore_throat': [['influenza']],
                    'false': [['smokes', 'nonsmokers']]},
          'askables': [],
          'assumables': ['smokes', 'nonsmokers', 'influenza', 'infection']}

    observation = ['wheezing', 'fever', 'sore_throat']
    print(f"Explanation to {observation}: {abduction(kb, observation)}")
