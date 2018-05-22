#!/usr/bin/env python3


def to_tokens(text):
    text = text.replace("(", " ( ").replace(")", " ) ")
    text = text.replace("[", " [ ").replace("]", " ] ")
    text = text.split()
    converted = []
    for token in text:
        try:
            converted.append(float(token))
        except ValueError:
            converted.append(token)
    return converted
