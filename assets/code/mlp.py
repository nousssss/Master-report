from typing import Sequence
embedding = None


def mlp_sequence(input: Sequence):
    """
    @param input: The sequence to be processed
    """
    output = []
    for element in input:
        e = embedding(element)
        output.append(e)
    return output