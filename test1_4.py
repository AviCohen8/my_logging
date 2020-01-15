def sof(*args, **kwargs):
    m_sortd = {}

    def add(index, my_word):
        last = my_word[-1]
        if last in m_sortd.keys():
            m_sortd[last].update({index: my_word})
        else:
            m_sortd[last] = {index: my_word}

    for i, word in enumerate(args):
        add(i, word)
    for k, v in m_sortd.items():
        print(f"Words ending with {k}: {v}")
    if kwargs != 0:
        print(f"Key value arguments {kwargs} are not handled yet")


sof("bear", "hhhhh", "bath", "door", "r", r="r", g="g")
