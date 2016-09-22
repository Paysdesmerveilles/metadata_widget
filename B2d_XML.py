"""Create xml file"""
def xml(A,title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1,T2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor, name):
    from lxml import etree
    from copy import deepcopy
    #Changement de direction
    import csv
    with open('Contact.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        contact_list = list(reader) 
    # Les variables sont chargés via le formulaire développé dans test5_widget.py
    # Le chargement 
    #Analyser le fichier xml pour remplacer les attributs voulus
    doc=etree.parse('Metadata_template3.xml')
    root=doc.getroot()
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
    POC_Organisation_xml=root[3][0][0][0]
    POC_Adress_xml=root[3][0][2][0][1][0][0][0]
    POC_City_xml=root[3][0][2][0][1][0][1][0]
    POC_Postalcode_xml=root[3][0][2][0][1][0][3][0]
    POC_Country_xml=root[3][0][2][0][1][0][4][0]
    POC_email_xml=root[3][0][2][0][1][0][5][0]
    
    D_Organisation_xml=root[8][0][5][0][0][0]
    D_Adress_xml=root[8][0][5][0][1][0][1][0][0][0]
    D_City_xml=root[8][0][5][0][1][0][1][0][1][0]
    D_Postalcode_xml=root[8][0][5][0][1][0][1][0][2][0]
    D_Country_xml=root[8][0][5][0][1][0][1][0][3][0]
    D_email_xml=root[8][0][5][0][1][0][1][0][4][0]

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
    condition_contact(resource_contact,POC_Organisation_xml,POC_Adress_xml, POC_City_xml,POC_Postalcode_xml , POC_Country_xml, POC_email_xml, contact_list)
    condition_contact(distributor,D_Organisation_xml,D_Adress_xml, D_City_xml,D_Postalcode_xml , D_Country_xml, D_email_xml, contact_list)
    condition_contact(owner1,OW1_Organisation_xml,OW1_Adress_xml, OW1_City_xml,OW2_Postalcode_xml , OW1_Country_xml, OW1_email_xml, contact_list)
    condition_contact(owner2, OW2_Organisation_xml,OW2_Adress_xml, OW2_City_xml,OW2_Postalcode_xml , OW2_Country_xml, OW2_email_xml, contact_list)
    if owner2==0:
        root[8][0][4].remove(root[8][0][4][1])
    if owner1==0:
        root[8][0][4].remove(root[8][0][4][0])      
    doc.write('Test/XML_%s.xml' %name, xml_declaration=True)

def condition_contact(type_contact, organisation, adress, city, post_code, country, mail, contact_list):
    if type_contact=='EOST/ IPGS':
        variable=1
    elif type_contact=='BRGM':
        variable=2
    elif type_contact=='Es Géothermie':
        variable=3 
    elif type_contact=='GEIE':
        variable=4
    else:
        return
    organisation.text=contact_list[variable][0]
    adress.text=contact_list[variable][1]
    city.text=contact_list[variable][3]
    post_code.text=contact_list[variable][2]
    country.text=contact_list[variable][4]
    mail.text=contact_list[variable][5]


    