def pnt(text):

    # just a function to print and end on
    # the same line
    print(text, end="")


def column_lengths(table):

    # Table is just the entire table as a tuple where
    # each row is a sub tuple

    column_chr = []
    # This list will contain the maximum chars in each column

    for i in range(len(table[0])):
        max_char = 0
        for row in table:
            if len(str(row[i])) > max_char:
                max_char = len(str(row[i]))

        column_chr.append(max_char + 2)  # the +2 for space

    return tuple(column_chr)


def top_line(column_chr, sep_ver, sep_hori, corner, func=pnt):
   # Just the seperator b/w 2 rows

    for each in column_chr:
        func(corner + (sep_hori * each))
    func(corner + "\n")


def display(table, sep_ver="|", sep_hori="-", corner="+", func=pnt):

    column_chr = column_lengths(table)

    # sum of the widths of the columns
    # + the lines in b\w columns
    # + 1 last dash at the end as to create 9 columns you need 10 lines

    row_no = 0
    for row in table:
        if table.index(row) == 1:
            top_line(column_chr, ' ', ' ', '|', func=func)
            top_line(column_chr, sep_ver, sep_hori,
                     corner, func=func)
        else:
            top_line(column_chr, sep_ver, sep_hori,
                     corner, func=func)

        column = 0

        for element in row:

            func(sep_ver + str(element))
            func(" " * (column_chr[column] - len(str(element))))
            column += 1

        func(sep_ver)
        if row_no:
            func(str(row_no) + "\n")
        else:
            func("\n")
        row_no += 1

    top_line(column_chr, sep_ver, sep_hori, corner, func=func)
