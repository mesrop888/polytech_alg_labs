def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            print("Pattern found at index:", i)


text = "ABAAABCDABCABC"
pattern = "ABC"

naive_search(text, pattern)