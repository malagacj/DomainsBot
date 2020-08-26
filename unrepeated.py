def unrepeated_counter(input_word):
    max_length = 0

    for index in range(len(input_word)):
        valid_word = ''
        for letter in input_word[index:]:
            if letter not in valid_word:
                valid_word += letter
            else:
                break

        if len(valid_word) > max_length:
            max_length = len(valid_word)
    return max_length

def adv_unrepeated_counter(input_word):
    def find_max_length(init, fin):
        for letter in fin:
            init += letter
            if len(init) != len(set(init)):
                break
        return len(set(init))

    max_length = 1

    for index in range(len(input_word)):
        word = input_word[index:] # Word to be checked

        if max_length >= len(word):
            break # No point to continue as max_length has already been found

        init, fin = word[:max_length], word[max_length:]

        if len(init) != len(set(init)):
            continue

        length = find_max_length(init, fin)

        max_length = length if length >  max_length else max_length

    return max_length


if __name__ == '__main__':
    import timeit

    print(timeit.timeit('unrepeated_counter("abcabcbb")',
                        setup='from __main__ import unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('adv_unrepeated_counter("abcabcbb")',
                        setup='from __main__ import adv_unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('unrepeated_counter("bbbbb")',
                        setup='from __main__ import unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('adv_unrepeated_counter("bbbbb")',
                        setup='from __main__ import adv_unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('unrepeated_counter("abcdefghijklaxyz")',
                        setup='from __main__ import unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('adv_unrepeated_counter("abcdefghijklaxyz")',
                        setup='from __main__ import adv_unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('unrepeated_counter("abcdefghijklmnobpqrstu")',
                        setup='from __main__ import unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('adv_unrepeated_counter("abcdefghijklmnobpqrstu")',
                        setup='from __main__ import adv_unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('unrepeated_counter("abcdefghijklmnopqcrstuvwxyz")',
                        setup='from __main__ import unrepeated_counter',
                        number=100000
                        )
          )

    print(timeit.timeit('adv_unrepeated_counter("abcdefghijklmnopqcrstuvwxyz")',
                        setup='from __main__ import adv_unrepeated_counter',
                        number=100000
                        )
          )
