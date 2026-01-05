def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = ([0] * (n+1) for _ in range(m+1))

    for i in range(1, m+1):
        for j in range(1, n+1):