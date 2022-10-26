#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# filepath to the location of the input data file
sPath = r'C:\Users\USER\Desktop\6DS data.xlsx'
# names of Actors you want to find the connection between
Person1 = "Scarlett Johansson"
Person2 = "Meryl Streep"
dfInput = pd.read_excel(sPath)


# In[3]:


def Phase1 (Data, Name1, Name2):

    dfdata = Data
    sStart = Name1
    sDest  = Name2
    
    dfdata['Layer'] = 0
    df7 = df8 = df6 = df5 = df4 = df3 = df2 = df1 = pd.DataFrame(columns = dfdata.columns)

    df1 = dfdata.loc[dfdata['Person'] == sStart]   #ilayer = 2
    df1.loc[:]['Layer'] = 1
    df2 = dfdata.loc[dfdata['Film'].isin(df1.Film)]
    df2.loc[:]['Layer'] = 2
    dfTest = df2[df2['Person'] == sDest]
    
    if dfTest.empty:    #ilayer = 4
    
        df3 = dfdata.loc[dfdata['Person'].isin(df2.Person)]
        df3.loc[:]['Layer'] = 3
        df4 = dfdata.loc[dfdata['Film'].isin(df3.Film)]
        df4.loc[:]['Layer'] = 4
        dfTest = df4[df4['Person'] == sDest]
    
        if dfTest.empty:     #ilayer = 6
    
            df5 = dfdata.loc[dfdata['Person'].isin(df4.Person)]
            df5.loc[:]['Layer'] = 5
            df6 = dfdata.loc[dfdata['Film'].isin(df5.Film)]
            df6.loc[:]['Layer'] = 6
            dfTest = df6[df6['Person'] == sDest]
    
            if dfTest.empty:    #ilayer = 8
                
                df7 = dfdata.loc[dfdata['Person'].isin(df6.Person)]
                df7.loc[:]['Layer'] = 7
                df8 = dfdata.loc[dfdata['Film'].isin(df7.Film)]
                df8.loc[:]['Layer'] = 8
                dfTest = df8[df8['Person'] == sDest]
                
                if dfTest.empty:
                    print ("Name not found in dataset at layer 8")
                
    dFinal = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])
    dFinal = (dFinal.reset_index()
            .drop_duplicates(subset='index', keep='first')
            .set_index('index'))
    dFinal['Path'] = 0
    return dFinal


# In[4]:


def Phase2(Data, Name1, Name2, finalselection, iLayer):
    
    dFinal = Data
    sStart = Name1
    sDest = Name2
    iOption = finalselection
    
    #last layer
    iIndex = dFinal.loc[dFinal['Person']== sDest].index[iOption]
    dFinal.at[iIndex,'Path'] = 1
    #second last layer
    sConnection = dFinal.loc[dFinal['Person']== sDest].Film.values[iOption]
    iCurrentLayer = dFinal.loc[dFinal['Person']== sDest].Layer.values[iOption] - 1
    dfConnection = dFinal.query('Film == @sConnection and Layer == @iCurrentLayer')
    dFinal.at[dfConnection.index[0],'Path'] = 1
    
    if iLayer > 2:   #iLayer == 4
    
        sConnection = dFinal.loc[dfConnection.index].Person.values[0]
        iCurrentLayer = iCurrentLayer - 1
        dfConnection = dFinal.query('Person == @sConnection and Layer == @iCurrentLayer')
        dFinal.at[dfConnection.index[0],'Path'] = 1
  
    if iLayer > 4:   #iLayer ==6
        
        sConnection = dFinal.loc[dfConnection.index].Film.values[0]
        iCurrentLayer = iCurrentLayer - 1
        dfConnection = dFinal.query('Film == @sConnection and Layer == @iCurrentLayer')
        dFinal.at[dfConnection.index[0],'Path'] = 1
    
        sConnection = dFinal.loc[dfConnection.index].Person.values[0]
        iCurrentLayer = iCurrentLayer - 1
        dfConnection = dFinal.query('Person == @sConnection and Layer == @iCurrentLayer')
        dFinal.at[dfConnection.index[0],'Path'] = 1
        
    if iLayer > 6:  #iLayer ==8
    
        sConnection = dFinal.loc[dfConnection.index].Film.values[0]
        iCurrentLayer = iCurrentLayer - 1
        dfConnection = dFinal.query('Film == @sConnection and Layer == @iCurrentLayer')
        dFinal.at[dfConnection.index[0],'Path'] = 1
    
        sConnection = dFinal.loc[dfConnection.index].Person.values[0]
        iCurrentLayer = iCurrentLayer - 1
        dfConnection = dFinal.query('Person == @sConnection and Layer == @iCurrentLayer')
        dFinal.at[dfConnection.index[0],'Path'] = 1
    
    #layer 1
    sConnection = dFinal.loc[dfConnection.index].Film.values[0]
    dfConnection = dFinal.query('Film == @sConnection and Person == @sStart')
    dFinal.at[dfConnection.index,'Path'] = 1
    return dFinal


# In[5]:


dfPhase1 = Phase1(dfInput, Person1, Person2)
dfPhase1[dfPhase1['Person'] == Person2]


# In[6]:


# if output above contains more than one film, you can change iLine to 1,2,3.... 
# to a max value of number of rows minus one. Default value iLine = 0
iLine = 0
dfOutput = Phase2(dfPhase1, Person1, Person2, iLine, dfPhase1.Layer.max() )
dfOutput[dfOutput['Path'] == 1]


# In[ ]:




