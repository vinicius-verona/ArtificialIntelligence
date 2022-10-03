# Task: Implement an abduction method

import copy


def abduction(explanationSet, kb, observations):
    """
        Returns explanation to the observations inputed given a knowledge base.
        PS: Not an efficient implementation
    """
    explanationSet = explanationSet.copy()

    if not observations:
        return [explanationSet]

    observation = observations[0]
    if (observation in kb['assumables']):
        explanationSet.add(observation)
        return abduction(explanationSet, kb, observations[1:])

    else:
        explanations = []

        for rule in kb['rules'][observation]:
            explanations += abduction(explanationSet, kb, rule + observations[1:])

        return explanations


def ask(askable):
    ans = input(f'Is {askable} true ? ')
    return True if ans.lower() in ['sim', 's', 'yes', 'y'] else False


if __name__ == "__main__":
    kb = {
        'rules':
            {
                'bronchitis': [['influenza'], ['smokes']],
                'coughing': [['bronchitis']],
                'wheezing': [['bronchitis']],
                'fever': [['influenza', 'infection']],
                'sore_throat': [['influenza']],
                'false': [['smokes', 'nonsmokers']]
            },
        'askables': [],
        'assumables': ['smokes', 'nonsmokers', 'influenza', 'infection']
    }

    observation = ['wheezing', 'fever', 'sore_throat']
    print(f"Explanation to {observation}: {explain(observation, kb)}")
    observation = ['wheezing', 'fever', 'sore_throat']
    print(f"Explanation to {observation}: {abduction(set(), kb, observation)}")
