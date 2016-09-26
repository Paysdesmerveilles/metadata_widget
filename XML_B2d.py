"""Create xml file"""
def xml2B2d(filePath):
    global title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1,T2,T3, t1, h1, t2, h2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor
    from lxml import etree
    import csv
    with open('Contact.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        contact_list = list(reader) 
    # Les variables sont chargés via le formulaire développé dans test5_widget.py
    # Le chargement 
#    chdir('/Users/Standard/Documents/Programme/Widget/Test')#filePath
    
    doc=etree.parse(filePath)
    root=doc.getroot()
    #Analyser le fichier xml pour remplacer les attributs voulus
    
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
    D_Organisation_xml=root[8][0][5][0][0][0]
        
    #Remplisage du fichier xml pour chaque donnée
    
    title=Title_xml.text
    abstract=Abstract_xml.text
    data_type=Data_type_xml
    North=float(North_xml.text)
    East=float(East_xml.text)
    South=float(South_xml.text)
    West=float(West_xml.text)
    Depth1=float(Depth1_xml.text)
    Depth2=float(Depth2_xml.text)
    Creation_date=Creation_date_xml.text
    T1=Date1_xml.text
    [t1, h1]=T1.split('T')
    T2=Date2_xml.text
    if type(T2)==str:
        [t2, h2]=T2.split('T')
        T3=1
    else:
        T3=0
        t2=None
        h2=None


    subject_Study=[]
    Len_su=len(root[8][0][9][0])
    for i in range(0, Len_su-2):
        subject_Study.append(root[8][0][9][0][i][0].text)
         
    project_Phase=[]
    Len_pro=len(root[8][0][10][0])
    for i in range(0, Len_pro-2):
        project_Phase.append(root[8][0][10][0][i][0].text)
    
    location=[]
    Len_loc=len(root[8][0][11][0])
    for i in range(0, Len_loc-2):
        location.append(root[8][0][11][0][i][0].text)
    
    
    variables=[]
    Len_var=len(root[8][0][12][0])
    for i in range(0, Len_var-2):
        variables.append(root[8][0][12][0][i][0].text)
    
    format1=[]
    Len_for=len(root[9][0][0][0])
    for i in range(0, Len_for-1):
        format1.append(root[9][0][0][0][i][0].text)
    
    quality=Quality_xml.text
    process=Process_step_xml.text
    use_lim=Use_xml.text
    access=Access_xml
    citation=Citation_xml.text
    
    if len(root[8][0][4])==0:
        owner1=0
        owner2=0
    elif len(root[8][0][4])==1:
        OW1_Organisation_xml=root[8][0][4][0][0][0]
        owner1=OW1_Organisation_xml.text
        owner2=0
    elif len(root[8][0][4])==2:
        OW1_Organisation_xml=root[8][0][4][0][0][0]
        OW2_Organisation_xml=root[8][0][4][1][0][0]
        owner1=OW1_Organisation_xml.text
        owner2=OW2_Organisation_xml.text
    
    resource_contact=POC_Organisation_xml.text
    distributor=D_Organisation_xml.text
    print(title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1, T2,T3, t1,h1,t2,h2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor)
    return title, abstract,data_type,North,East,South,West,Depth1,Depth2,T1, T2,T3, t1,h1,t2,h2,Creation_date,subject_Study, project_Phase, location, variables, format1, quality,process, use_lim,access,citation, resource_contact, owner1, owner2, distributor