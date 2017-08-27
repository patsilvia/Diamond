class Diamond(object):

    def __init__(self, top_char):
        self._topChar = top_char

    def elaborate(self):
        char_pointer = 'A'
        arr_first_half = []
        # print("{} {}".format("Expect upto ", self._topChar))
        while (ord(char_pointer) < ord(self._topChar)):
            arr_first_half.append(char_pointer)
            char_pointer = chr(ord(char_pointer)+1)

        return arr_first_half + [self._topChar] + \
            list(reversed(arr_first_half))

    def middle_index(self, arr_elaborate):
        # print(arr_elaborate)
        return int(round(len(arr_elaborate)/2, 0))

    def run_topdown(self, arr_elaborate):
        max_length = len(arr_elaborate)
        m = self.middle_index(arr_elaborate)

        for idx, alphabet in enumerate(arr_elaborate):
            if alphabet == 'A':
                print("{}{}{}{}{}".format('|', '.' * m, 'A', '.' * m, '|'))
            else:
                if idx <= m:
                    w_space = m-idx
                else:
                    w_space = idx-m

                m_space = max_length - (2 + (2*w_space))
                print("{}{}{}{}{}{}{}".format(
                        '|', '.'*w_space, alphabet, '.'*m_space, alphabet,
                        '.' * w_space, '|'))
