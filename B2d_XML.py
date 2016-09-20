"""Create xml file"""
def xml(A,title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1,T2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor):
    from os import chdir
    from lxml import etree
    from copy import deepcopy
    #Changement de direction
    import csv
    with open('Contact.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        contact_list = list(reader)
    
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
    Quality_xml=root[10][0][1][0][0][0]
    Process_step_xml=root[10][0][1][0][1][0][0][0]
    Use_xml=root[8][0][13][0][0][0]
    Access_xml=root[8][0][13][0][1][0].attrib['codeListValue']
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
    Access_xml=access
    Citation_xml.text=citation
    #root[8][0][4].append(deepcopy(root[8][0][4][1]))
    if resource_contact=='EOST/ IPGS':
        a=1
    elif resource_contact=='BRGM':
        a=2
    elif resource_contact=='Es Géothermie':
        a=3
    elif resource_contact=='GEIE':
        a=4    
    if distributor=='EOST/ IPGS':
        b=1
    elif distributor=='BRGM':
        b=2
    elif distributor=='Es Géothermie':
        b=3
    elif distributor=='GEIE':
        b=4
    if owner1=='EOST/ IPGS':
        c=1
    elif owner1=='BRGM':
        c=2
    elif owner1=='Es Géothermie':
        c=3
    elif owner1=='GEIE':
        c=4
    elif owner1==0:
        root[8][0][4].remove(root[8][0][4][0])
        c=0
    if owner2=='EOST/ IPGS':
        d=1
    elif owner2=='BRGM':
        d=2
    elif owner2=='Es Géothermie':
        d=3 
    elif owner2=='GEIE':
        d=4
    elif owner2==0:
        root[8][0][4].remove(root[8][0][4][1])
        d=0
    POC_Organisation_xml.text=contact_list[a][0]
    POC_Adress_xml.text=contact_list[a][1]
    POC_City_xml.text=contact_list[a][3]
    POC_Postalcode_xml.text=contact_list[a][2]
    POC_Country_xml.text=contact_list[a][4]
    #POC_email_xml=
    
    D_Organisation_xml.text=contact_list[b][0]
    D_Adress_xml.text=contact_list[b][1]
    D_City_xml.text=contact_list[b][3]
    D_Postalcode_xml.text=contact_list[b][2]
    D_Country_xml.text=contact_list[b][4]
    D_email_xml.text=contact_list[b][5]
    
    if c!=0: 
        OW1_Organisation_xml.text=contact_list[c][0]
        OW1_Adress_xml.text=contact_list[c][1]
        OW1_City_xml.text=contact_list[c][3]
        OW1_Postalcode_xml.text=contact_list[c][2]
        OW1_Country_xml.text=contact_list[c][4]
        OW1_email_xml.text=contact_list[c][5]
    
    if d!=0:
        OW2_Organisation_xml.text=contact_list[d][0]
        OW2_Adress_xml.text=contact_list[d][1]
        OW2_City_xml.text=contact_list[d][3]
        OW2_Postalcode_xml.text=contact_list[d][2]
        OW2_Country_xml.text=contact_list[d][4]
        OW2_email_xml.text=contact_list[d][5]
    
    doc.write('Test/Test%d.xml' %A, xml_declaration=True)
