# custom class
class Well:
    def __init__(self, reagent_1_mM, reagent_2_mM, column_no, row_no):
        self.reagent_1_mM = reagent_1_mM
        self.reagent_2_mM = reagent_2_mM
        self.column_no = column_no
        self.row_no = row_no
        self.well_no = row_no + str(column_no)

    def __str__(self):
        return "({} {})".format(self.reagent_1_mM, self.reagent_2_mM, self.row_no, self.column_no)

    # strange that _str_ is not working
    def __repr__(self):
        return "({} {} {} {})".format(self.reagent_1_mM, self.reagent_2_mM, self.row_no, self.column_no)


# but we are not really using Class Well here
reagents_1_mM = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ]
reagents_2_mM = [0, 10, 20, 40, 80, 160, 360, 400]
# create row index for a plate
ascii_row = []
for index in range(len(reagents_2_mM)):
    ascii_row.append(65 + index)

row_index = []
for x in ascii_row:
    row_index.append(chr(x))

# create column index for a plate
col_index = []
for x in range(len(reagents_1_mM)):
    col_index.append(x + 1)

# create list of empty lists
output_plate = [[] for i in range(len(reagents_2_mM))]

# Fill it with reagents values
for row in range(len(reagents_2_mM)):
    for col in range(len(reagents_1_mM)):
        output_plate[row].append(Well(reagents_1_mM[col], reagents_2_mM[row], col_index[col], row_index[row]))

print(output_plate)
