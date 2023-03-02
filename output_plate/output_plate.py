# custom class
import pandas as pd
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

df = pd.DataFrame(output_plate, columns=[col_index], index=[row_index])
print(df)

Well_index = []
for r in range(len(row_index)):
    for c in range(len(col_index)):
        Well_index.append(row_index[r] + str(col_index[c]))
# print(Well_index)

reagent_1 = []
for r in range(len(row_index)):
    for c in range(len(col_index)):
        reagent_1.append(reagents_1_mM[c])
# print(reagent_1)

reagent_2 = []
for r in range(len(row_index)):
    for c in range(len(col_index)):
        reagent_2.append(reagents_2_mM[r])
# print(reagent_2)

df2 = pd.DataFrame()
df2['Well_ID'] = Well_index
df2['conc_reagents_1'] = reagent_1
df2['conc_reagents_2'] = reagent_2

print(df2)