NNZ = 5
N = 3
IRN = [1, 3, 2, 2, 3]
JCN = [1, 1, 2, 3, 3]
VAL = [1, 4, 2, 3, 5]


def create_rowptr(rows):
    result = []
    current_row = 0
    for i, x in enumerate(rows):
        if x > current_row:
            current_row = x
            result.append(i+1)
    result.append(len(rows)+1)

    return result


def coo_to_csr(IRN, JCN, VAL):
    rows = []
    values = []
    ICL = []
    sorted_by_rows = sorted(zip(IRN, JCN, VAL), key=lambda key: key[0])
    for row, column, value in sorted_by_rows:
        ICL.append(column)
        values.append(value)
        rows.append(row)
    rows = create_rowptr(rows)

    return ICL, values, rows


icl, val, rowptr = coo_to_csr(IRN, JCN, VAL)
print("ICL {0}", format(icl))
print("VAL {0}", format(val))
print("ROWPTR {0}", format(rowptr))