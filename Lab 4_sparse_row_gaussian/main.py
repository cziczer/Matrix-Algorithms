class CSRMatrix:
    def __init__(self, icl, value, rowptr):#rowptr - lets count from 0, not 1 and icl(columns) too
        self.icl = icl
        self.value = value
        self.rowptr = rowptr


def sparse_gauss_row_elimination(matix: CSRMatrix):
    current_row = 0
    for i, k in enumerate(matix.rowptr): #enumerato for each column, i = row indx
        akk = 0
        for x in matix.icl[matix.rowptr[current_row]: matix.rowptr[current_row+1]]:
            if x == i:
                akk = matix.value[matix.icl.index(x, matix.rowptr[current_row], matix.rowptr[current_row+1])]

        if akk != 0:
            for index, x in enumerate(matix.value[matix.rowptr[current_row]: matix.rowptr[current_row+1]]):
                matix.value[index + matix.rowptr[current_row]] /= akk

        current_row_values = matix.value[matix.rowptr[current_row]: matix.rowptr[current_row + 1]]
        current_row_icl = matix.icl[matix.rowptr[current_row]: matix.rowptr[current_row + 1]]
        for j in range(i+1, len(matix.rowptr)-1):# each row
            delete_row_icl = matix.icl[matix.rowptr[j]: matix.rowptr[j+1]]
            if i in delete_row_icl:
                ajk = matix.value[matix.icl.index(i, matix.rowptr[j], matix.rowptr[j+1])]
                for index_delete in current_row_icl:
                    if index_delete in delete_row_icl: #index from current row exists in row we are searching right now
                        matix.value[matix.icl.index(index_delete, matix.rowptr[j], matix.rowptr[j+1])] -= \
                            current_row_values[current_row_icl.index(index_delete)] * ajk
                    else: # we have to insert another record
                        new_value_index = index_delete + matix.rowptr[j]
                        for insert_index, x in enumerate(matix.icl[matix.rowptr[j]: matix.rowptr[j+1]]):
                            if new_value_index == insert_index + matix.rowptr[j]: #insert there
                                #1. add value
                                matix.value.insert(new_value_index,
                                                   (-current_row_values[current_row_icl.index(index_delete)] * ajk))
                                # 2. add column index
                                matix.icl.insert(new_value_index,
                                                 index_delete)
                                # 3. update row ptr
                                for row_ptr_i in range(j+1, len(matix.rowptr)):
                                    matix.rowptr[row_ptr_i] += 1
                                break

        current_row += 1

        if current_row == len(matix.rowptr) - 1:
            #delete 0 values
            del_indexes = [] #when [0, 0] in for we dont see second 0
            for index, value in enumerate(matix.value):
                if value == 0:
                    del_indexes.append(matix.value.index(value, index))
            for index in del_indexes[::-1]:
                matix.value.pop(index)
                matix.icl.pop(index)
                # update row pointer
                for row_ptr_index, pointer in enumerate(matix.rowptr):
                    if pointer > index:
                        matix.rowptr[row_ptr_index] -= 1

            return


A = CSRMatrix([0, 1, 2, 0, 2], [1, 2, 3, 4, 5], [0, 1, 3, 5])
sparse_gauss_row_elimination(A)
print(A.value)
print(A.icl)
print(A.rowptr)
print()
B = CSRMatrix([0, 1, 1, 2, 0, 2], [1, 2, 2, 3, 4, 5], [0, 2, 4, 6])
sparse_gauss_row_elimination(B)
print(B.value)
print(B.icl)
print(B.rowptr)