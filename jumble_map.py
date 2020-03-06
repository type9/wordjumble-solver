def build_map(word_list):
    '''Builds a map from sorted word to unsorted word'''
    map = {}
    for word in word_list:
        sorted = ''.join(sorted(word))
        map.setdefault(sorted, []).append(word)
    return map