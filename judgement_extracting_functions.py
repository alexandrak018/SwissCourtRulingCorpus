from typing import Optional, Iterable


def CH_BGer(rulings: str, namespace: dict) -> Optional[Iterable[str]]:
    """
    IMPORTANT: So far, only German is supported!
    :param rulings:     the string containing the rulings
    :param namespace:   the namespace containing some metadata of the court decision
    :return:            the sections dict, None if not in German
    """
    if namespace['language'] != 'de':
        return None

    judgement_markers = {'approval': ['In Gutheissung', 'aufgehoben', 'gutgeheissen', 'gutzuheissen'],
                         'partial approval': ['teilweise gutgeheissen'],
                         'dismissal': ['abgewiesen'],
                         'partial dismissal': ['abgewiesen, soweit darauf einzutreten ist'],
                         'formal problems': ['nicht eingetreten', 'als gegenstandslos abgeschrieben', 'Nichteintreten']}

    judgements = set()
    for judgement, markers in judgement_markers.items():
        for marker in markers:
            if marker in rulings:
                judgements.add(judgement)

    if not judgements:
        message = f"Found no judgement for the case {namespace['html_url']}. Please check!"
        raise ValueError(message)
    elif len(judgements) > 1:
        if "partial_approval" in judgements:
            judgements.remove("approval")  # if partial_approval is found, it will find approval as well
        if "partial_dismissal" in judgements:
            judgements.remove("dismissal")  # if partial_dismissal is found, it will find dismissal as well

    return judgements


def CH_BGE(rulings: str, namespace: dict) -> Optional[Iterable[str]]:
    return CH_BGer(rulings, namespace)
