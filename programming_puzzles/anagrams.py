from collections import Counter
import random
import string
import time

# Kiểm tra xem str1 str2 có phải anagram ko
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    dict1 = Counter(list(str1))
    dict2 = Counter(list(str2))

    for char in dict1:
        if char not in dict2 or dict2[char] != dict1[char]:
            return False

    return True

def test(anagram_fn):
    print('Testing ', anagram_fn)
    assert anagram_fn('table', 'bleat')
    assert not anagram_fn('table', 'bleate')
    assert anagram_fn('honey', 'eyhon')
    assert not anagram_fn('area', 'are3')
    assert not anagram_fn('', ' ')


def create_random_anagrams(n=10000):
    characters = [random.choice(string.ascii_letters) for _ in range(n)]
    str1 = ''.join(characters)
    random.shuffle(characters)
    str2 = ''.join(characters)
    return str1, str2


def time_test(str1, str2):
    start = time.time()
    assert are_anagrams(str1, str2)
    print('Time:', time.time() - start)

test(are_anagrams)

# Sinh dữ liệu ngẫu nhiên và đo thời gian
str1, str2 = create_random_anagrams()
time_test(str1, str2)

