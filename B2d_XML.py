#Chargement des modules
from os import chdir
import xlrd
from lxml import etree
from copy import deepcopy
#Changement de direction
chdir('/Users/Standard/Documents/Programme')
# Les variables sont chargés via le formulaire développé dans test5_widget.py
# Le chargement 
#Analyser le fichier xml pour remplacer les attributs voulus
doc=etree.parse('Metadata_template2.xml')
root=doc.getroot()
tag=[]
for child in root:
    tag.append(child.tag)

Title_xml=root[8][0][0][0][0][0]
Abstract_xml=root[8][0][1][0]
Data_type_xml=root[10][0][0][0][0][0].attrib['codeListValue']
North_xml=root[8][0][20][0][1][0][3][0]
East_xml=root[8][0][20][0][1][0][1][0]
South_xml=root[8][0][20][0][1][0][2][0]
West_xml=root[8][0][20][0][1][0][0][0]
Depth1_xml=root[8][0][19][0][2][0][0][0]
Depth2_xml=root[8][0][19][0][2][0][1][0]
Date1_xml=root[8][0][18][0][0][0][0][0][0]
Date2_xml=root[8][0][18][0][0][0][0][0][1]
Creation_date_xml=root[8][0][0][0][1][0][0][0]
#Subject_xml=root[8][0][9][0][0][0]
#Project_xml=root[8][0][10][0][0][0]
#Location_xml=root[8][0][11][0][3][0]
#Location2_xml=root[8][0][11][0][4][0]
#Location3_xml=root[8][0][11][0][5][0]
#Variable_xml=root[8][0][12][0][0][0]
#Variable2_xml=root[8][0][12][0][1][0]
#Variable3_xml=root[8][0][12][0][2][0]
#Format1_xml=root[9][0][0][0][0][0]
Quality_xml=root[10][0][1][0][0][0]
Process_step_xml=root[10][0][1][0][1][0][0][0]
Use_xml=root[8][0][13][0][0][0]
#Access_xml=
Citation_xml=root[10][0][1][0][1][0][1][0][0][0]
POC_Name_xml=root[3][0][0][0]
POC_Organisation_xml=root[3][0][1][0]
POC_Adress_xml=root[3][0][3][0][1][0][0][0]
POC_City_xml=root[3][0][3][0][1][0][1][0]
POC_Postalcode_xml=root[3][0][3][0][1][0][3][0]
POC_Country_xml=root[3][0][3][0][1][0][4][0]
#POC_email_xml=
D_Name_xml=root[8][0][5][0][0][0]
D_Organisation_xml=root[8][0][5][0][1][0]
D_Phone_xml=root[8][0][5][0][2][0][0][0][0][0]
D_Adress_xml=root[8][0][5][0][2][0][1][0][0][0]
D_City_xml=root[8][0][5][0][2][0][1][0][1][0]
D_Postalcode_xml=root[8][0][5][0][2][0][1][0][2][0]
D_Country_xml=root[8][0][5][0][2][0][1][0][3][0]
D_email_xml=root[8][0][5][0][2][0][1][0][4][0]
OW1_Organisation_xml=root[8][0][4][0][0][0]
OW1_Adress_xml= root[8][0][4][0][1][0][0][0][0][0]
OW1_City_xml=root[8][0][4][0][1][0][0][0][1][0]
OW1_Postalcode_xml=root[8][0][4][0][1][0][0][0][2][0]
OW1_Country_xml=root[8][0][4][0][1][0][0][0][3][0]
OW1_email_xml= root[8][0][4][0][1][0][0][0][4][0]
OW2_Organisation_xml=root[8][0][4][1][0][0]
OW2_Adress_xml=root[8][0][4][1][1][0][0][0][0][0]
OW2_City_xml=root[8][0][4][1][1][0][0][0][1][0]
OW2_Postalcode_xml=root[8][0][4][1][1][0][0][0][2][0]
OW2_Country_xml=root[8][0][4][1][1][0][0][0][3][0]
OW2_email_xml= root[8][0][4][1][1][0][0][0][4][0]

#Remplisage du fichier xml pour chaque donnée

Title_xml.text=title
Abstract_xml.text=abstract
Data_type_xml=data_type
North_xml.text=str(North)
East_xml.text=str(East)
South_xml.text=str(South)
West_xml.text=str(West)
Depth1_xml.text=str(Depth1)
Depth2_xml.text=str(Depth2)
Date1_xml.text=T1
Date2_xml.text=T2
Creation_date_xml.text=Creation_date

Len_su=len(subject_Study)
root[8][0][9][0][0][0].text=subject_Study[0]
if Len_su>1:
    for i in range(0, Len_su-1):
        root[8][0][9][0][i].addnext(deepcopy(root[8][0][9][0][0]))
        root[8][0][9][0][i+1][0].text=subject_Study[i+1]
        

Len_pro=len(project_Phase)
root[8][0][10][0][0][0].text=project_Phase[0]
if Len_pro>1:
    for i in range(0, Len_pro-1):
        root[8][0][10][0][i].addprevious(deepcopy(root[8][0][10][0][0]))
        root[8][0][10][0][i+1][0].text=project_Phase[i+1]


Len_loc=len(location)
root[8][0][11][0][0][0].text=location[0]
if Len_loc>1:
    for i in range(0, Len_loc-1):
        root[8][0][11][0][i].addnext(deepcopy(root[8][0][11][0][0]))
        root[8][0][11][0][i+1][0].text=location[i+1]


Len_var=len(variables)
root[8][0][12][0][0][0].text=variables[0]
if Len_var>1:
    for i in range(0, Len_var-1):
        root[8][0][12][0][i].addnext(deepcopy(root[8][0][12][0][0]))
        root[8][0][12][0][i+1][0].text=variables[i+1]


Len_for=len(format1)
root[9][0][0][0][0][0].text=format1[0]
if Len_var>1:
    for i in range(0, Len_for-1):
        root[9][0][0][0][i].addnext(deepcopy(root[9][0][0][0][0]))
        root[9][0][0][0][i+1][0].text=format1[i+1]
else:
    root[9][0][0][0][0][0].text=format1[0]

Quality_xml.text=quality
Process_step_xml.text=process
Use_xml.text=use_lim
#Access_xml=
Citation_xml.text=citation


##root[8][0][4].append(deepcopy(root[8][0][4][1]))
#POC_Name_xml=root[3][0][0][0]
#POC_Organisation_xml=root[3][0][1][0]
#POC_Adress_xml=root[3][0][3][0][1][0][0][0]
#POC_City_xml=root[3][0][3][0][1][0][1][0]
#POC_Postalcode_xml=root[3][0][3][0][1][0][3][0]
#POC_Country_xml=root[3][0][3][0][1][0][4][0]
##POC_email_xml=
#D_Name_xml=root[8][0][5][0][0][0]
#D_Organisation_xml=root[8][0][5][0][1][0]
#D_Phone_xml=root[8][0][5][0][2][0][0][0][0][0]
#D_Adress_xml=root[8][0][5][0][2][0][1][0][0][0]
#D_City_xml=root[8][0][5][0][2][0][1][0][1][0]
#D_Postalcode_xml=root[8][0][5][0][2][0][1][0][2][0]
#D_Country_xml=root[8][0][5][0][2][0][1][0][3][0]
#D_email_xml=root[8][0][5][0][2][0][1][0][4][0]
#OW1_Organisation_xml=root[8][0][4][0][0][0]
#OW1_Adress_xml= root[8][0][4][0][1][0][0][0][0][0]
#OW1_City_xml=root[8][0][4][0][1][0][0][0][1][0]
#OW1_Postalcode_xml=root[8][0][4][0][1][0][0][0][2][0]
#OW1_Country_xml=root[8][0][4][0][1][0][0][0][3][0]
#OW1_email_xml= root[8][0][4][0][1][0][0][0][4][0]
#OW2_Organisation_xml=root[8][0][4][1][0][0]
#OW2_Adress_xml=root[8][0][4][1][1][0][0][0][0][0]
#OW2_City_xml=root[8][0][4][1][1][0][0][0][1][0]
#OW2_Postalcode_xml=root[8][0][4][1][1][0][0][0][2][0]
#OW2_Country_xml=root[8][0][4][1][1][0][0][0][3][0]
#OW2_email_xml= root[8][0][4][1][1][0][0][0][4][0]



#
#if location3[i] != '':
#    Location3_xml.text=location3[i]
#else:
#    Location3_xml.clear()
#    root[8][0][11][0][4].clear()
#if contact[i]=='EOST/IPGS':
#    ContactOrganisation_xml.text='EOST/IPGS'
#elif contact[i]=='BRGM':
#    ContactOrganisation_xml.text='BRGM'
#    ContactAdress_xml.text=BRGM[0]
#    CodePostal_xml.text=str(BRGM[1])
#    Ville_xml.text=BRGM[2]
#    Country_xml.text=BRGM[3]
#    ContactName_xml.text=BRGM[4]
#    email_xml.text=BRGM[6]


doc.write('Test.xml', xml_declaration=True)
#To remove or add contact owner
#root[8][0][4].remove(root[8][0][4][1])
#root[8][0][4].append(deepcopy(root[8][0][4][1]))
#add location
#root[8][0][11][0][0].addnext(deepcopy(root[8][0][11][0][0]))
#root[8][0][11][0][0].addnext(deepcopy(root[8][0][11][0][0]))
#root[8][0][11][0][1][0].text='test2'
#root[8][0][11][0][2][0].text='test3'