def multiplication_tables(row, col):
    Matrix = [[0 for x in range(row)] for y in range(col)]
    for r in range(row):
        for c in range(col):
            Matrix[r][c] = (r + 1) * (c + 1)
    return Matrix
