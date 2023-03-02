import pandas as pd

"""Reagents specification needed for Organick step TargetedMixSamples"""
reaction_volume_uL=20

#Reagent 1 is 'Spermidine'
reagents_1_sID=68187677
reagents_1_stock_conc_mM =250
reagents_1_mM = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]

#Reagent 2 is 'Putrescine'
reagents_2_sID=68187678
reagents_2_stock_conc_mM =250
reagents_2_mM = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]

#Reagent 3 is 'Water'
reagents_3_sID=68187679

#Volume of Reagent 1, Reagent 2, and water
R1_R2_water_volume_uL=2.434

"""Plate visualization with reagent 1 and reagent 2 concentrations"""

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

df = pd.DataFrame(output_plate, columns=[col_index], index=[row_index])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)
print(df)

"""Building Dataframe with all the informations"""
df2 = pd.DataFrame()

#Plate well index
Well_index = []
for r in range(len(row_index)):
    for c in range(len(col_index)):
        Well_index.append(row_index[r] + str(col_index[c]))
df2['Well_ID'] = Well_index

#set DataFrame index
df2.set_index('Well_ID',inplace=True)

#Well's column index
col=[]
for r in range(len(row_index)):
    for c in range(len(col_index)):
        col.append(c+1)
df2['col_index'] = col

#Well's row index
row=[]
for r in range(len(row_index)):
    for c in range(len(col_index)):
        row.append(r+1)  
df2['col_row'] = row

#Final concentration of Reagent 1
reagent_1_mM = []
for r in range(len(row_index)):
    for c in range(len(col_index)):
        reagent_1_mM.append(reagents_1_mM[c])
df2['conc_reagents_1_mM'] = reagent_1_mM

#Final concentration of Reagent 2
reagent_2_mM = []
for r in range(len(row_index)):
    for c in range(len(col_index)):
        reagent_2_mM.append(reagents_2_mM[r])
df2['conc_reagents_2_mM'] = reagent_2_mM

#volume of reagent 1 [µL]
volume_reagents_1_uL=[]
for x in range(len(reagent_1_mM)):
        volume_reagents_1_uL.append(reagent_1_mM[x]*reaction_volume_uL/reagents_1_stock_conc_mM)
df2['volume_reagents_1_uL'] = volume_reagents_1_uL

#volume of reagent 2 [µL]
volume_reagents_2_uL=[]
for y in range(len(reagent_2_mM)):
    volume_reagents_2_uL.append(reagent_2_mM[y]*reaction_volume_uL/reagents_2_stock_conc_mM)
df2['volume_reagents_2_uL'] = volume_reagents_2_uL

#volume of water [µL]
volume_water_uL=[]
for r in range(len(df2.axes[0])):
        volume_water_uL.append(R1_R2_water_volume_uL-df2.loc[Well_index[r],'volume_reagents_1_uL']-df2.loc[Well_index[r],'volume_reagents_2_uL'])
df2['volume_water_uL']=volume_water_uL

#Sample ID reagent 1 (Spermidine)
Sample_ID_reagent_1=[]
for r in range(len(df2.axes[0])):
    Sample_ID_reagent_1.append(reagents_1_sID)
df2['Sample_ID_reagent_1']=Sample_ID_reagent_1

#Sample ID reagent 2 (Putrescine)
Sample_ID_reagent_2=[]
for r in range(len(df2.axes[0])):
    Sample_ID_reagent_2.append(reagents_2_sID)
df2['Sample_ID_reagent_2']=Sample_ID_reagent_2

#Sample ID reagent 3 (Water)
Sample_ID_reagent_3=[]
for r in range(len(df2.axes[0])):
    Sample_ID_reagent_3.append(reagents_3_sID)
df2['Sample_ID_reagent_3']=Sample_ID_reagent_3

"""#Container ID
cID = [] 
for r in range(len(df2.axes[0])):
    cID.append(1137442)
df2['cID']=cID"""

#Empty row needed for Organick
Blank =[]
for r in range(len(df2.axes[0])):
    Blank.append(' ')
df2['Blank']=Blank

#cID index needed for Organick
cID_index =[]
for r in range(len(df2.axes[0])):
    cID_index.append(1)
df2['cID_index']=cID_index
print(df2)

"""Dataframe in correct format for Organick step TargetedMixSamples"""
df3 = pd.DataFrame()
df3['Sample_ID_reagent_1']=Sample_ID_reagent_1
df3['volume_reagents_1_uL'] = volume_reagents_1_uL
df3['cID_index']=cID_index
df3['Blank']=Blank
df3['col_row'] = row
df3['col_index'] = col
df3['Sample_ID_reagent_2']=Sample_ID_reagent_2
df3['volume_reagents_2_uL'] = volume_reagents_2_uL
df3['Sample_ID_reagent_3']=Sample_ID_reagent_3
df3['volume_water_uL']=volume_water_uL
df3.round(decimals=3)
#set index
df3.set_index('Sample_ID_reagent_1',inplace=True)

print(df3)


# In[193]:


"""csv export"""
df3.to_csv('TargetedMixSamples', float_format='%.3f', header=False)


# In[ ]:




