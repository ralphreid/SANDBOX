TRIE = GET_TRIE()


def generate_anagrams(source)
    anagrams = []
    sentence = []
    available_letters = get_counts(source)

    def search()
        if last_word(sentence) not in TRIE
            return
        if is_empty(available_letters)
            anagrams.add(sentence.join(''))
            return

        for char, value in available_letters + (' ', 1)
            if char == ' ' and sentence[-1] == ' '
                continue
            if value == 0
                continue
            sentence.add(char)
            available_letters[char] - -
            search()
            sentence.pop()
            available_letters[char] + +

    search()
    return anagrams