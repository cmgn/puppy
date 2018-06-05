#!/usr/bin/env python3


def to_tokens(text):
    text = text.replace("(", " ( ").replace(")", " ) ")
    text = text.replace("[", " [ ").replace("]", " ] ")
    text = text.split()
    converted = []
    for token in text:
        # special syntactic sugar for a lambda
        if token == "->":
            var = converted.pop()
            converted.append("lambda")
            converted.append(var)
            continue
        try:
            converted.append(int(token))
        except ValueError:
            try:
                converted.append(float(token))
            except ValueError:
                converted.append(token)
    return converted
