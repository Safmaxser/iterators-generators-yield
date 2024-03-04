class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.next = [0]

    def __iter__(self):
        return self

    def __next__(self):
        result = None
        flag_repeat = True
        while flag_repeat:
            result = self.list_of_list
            for index in self.next:
                try:
                    result = result[index]
                except IndexError:
                    if len(self.next) == 1:
                        raise StopIteration
                    else:
                        self.next.pop()
                        self.next[len(self.next)-1] += 1
                        flag_repeat = True
                else:
                    if result == []:
                        self.next[len(self.next)-1] += 1
                        flag_repeat = True
                    else:
                        flag_repeat = False
        while True:
            if isinstance(result, list):
                result = result[0]
                self.next.append(0)
            else:
                self.next[len(self.next)-1] += 1
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
