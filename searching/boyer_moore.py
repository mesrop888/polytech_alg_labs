def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)

    bad_char = {}

    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index:", s)

            if s + m < n:
                s += m - bad_char.get(text[s + m], -1)
            else:
                s += 1

        else:
            s += max(1, j - bad_char.get(text[s + j], -1))


text = "ABAAABCDABCABC"
pattern = "ABC"

boyer_moore(text, pattern)
