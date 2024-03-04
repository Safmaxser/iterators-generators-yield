class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.next = [0]

    def __iter__(self):
        return self

    def __next__(self):
        result = self.list_of_list
        flag_repeat = True
        flag_stop = False
        while flag_repeat:
            for index in self.next:
                try:
                    result = result[index]
                except IndexError:
                    if len(self.next) == 1:
                        flag_repeat = False
                        flag_stop = True
                    else:
                        self.next.pop()
                        self.next[len(self.next) - 1] += 1
                        result = self.list_of_list
                        flag_repeat = True
                else:
                    if result == []:
                        self.next[len(self.next)-1] += 1
                        result = self.list_of_list
                        flag_repeat = True
                    else:
                        flag_repeat = False
        if flag_stop:
            raise StopIteration
        else:
            while True:
                if isinstance(result, list):
                    result = result[0]
                    self.next.append(0)
                else:
                    self.next[len(self.next)-1] += 1
                    result = result
                    break
            return result


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None,
                                                   '!']


if __name__ == '__main__':
    test_3()
