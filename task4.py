def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    a = [alphabet.index(x)+1 if alphabet.__contains__(x) else '' for x in text]
    return ' '.join(str(x) for x in a if x != '')