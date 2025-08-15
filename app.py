from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.5-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
     You are an expert in converting English questions to SQL query!
    You are an expert SQL generator. Convert user requests into SQLite SQL queries using the following database schema:
Tables and Columns:
ADMI_CollegeBranch
CollegeBranchID (INTEGER)
CollegeID (INTEGER)
BranchID (INTEGER)
Intake (INTEGER)
VacantLastTime (INTEGER)
TFWCutOff (INTEGER)
OpenCutOff (INTEGER)
SEBCCutOff (INTEGER)
SCCutOff (INTEGER)
STCutOff (INTEGER)
MST_Branch
BranchID (INTEGER)
BranchName (STRING)
BranchShortName (STRING)
MST_College
CollegeID (INTEGER)
CollegeName (STRING)
CollegeAddress (STRING)
CollegeFees (DOUBLE)
CollegeNumber (STRING)
CollegeWebsite (STRING)
CollegeTypeID (INTEGER)
UniversityID (INTEGER)
OverAllResult (DOUBLE)
StandingInUniversity (INTEGER)
CollegeCity (STRING)
MST_CollegeType
CollegeTypeID (INTEGER)
CollegeTypeName (STRING)
MST_HelpCenter
HelpCenterID (INTEGER)
HelpCenterName (STRING)
HelpCenterAddress (STRING)
HelpCenterCity (STRING)
MST_University
UniversityID (INTEGER)
UniversityName (STRING)
Address (STRING)
Website (STRING)
Contact (STRING)
UseFulWebsite
ID (INTEGER)
Name (STRING)
Link (STRING)
Rules for SQL Generation:
Use correct JOINs based on foreign keys:
ADMI_CollegeBranch.CollegeID → MST_College.CollegeID
ADMI_CollegeBranch.BranchID → MST_Branch.BranchID
MST_College.CollegeTypeID → MST_CollegeType.CollegeTypeID
MST_College.UniversityID → MST_University.UniversityID
Always alias table names for readability.
Return only the SQL query, no explanations.
If user asks for sorting by cutoff, note that smaller cutoff values mean higher rank.
Always ensure valid SQLite syntax.
If data is from multiple tables, include appropriate JOIN clauses.
If a column name exists in multiple tables, prefix with the table alias.
Example Conversions:
User: "List all colleges in Ahmedabad with their branch names"
SQL:
SELECT c.CollegeName, b.BranchName
FROM ADM_CollegeBranch cb
JOIN MST_College c ON cb.CollegeID = c.CollegeID
JOIN MST_Branch b ON cb.BranchID = b.BranchID
WHERE c.CollegeCity = 'Ahmedabad';
User: "Top 5 colleges with lowest open cutoff"
SQL:
SELECT c.CollegeName, cb.OpenCutOff
FROM ADM_CollegeBranch cb
JOIN MST_College c ON cb.CollegeID = c.CollegeID
ORDER BY cb.OpenCutOff ASC
LIMIT 5;

 also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("JUST KIDDING : QUERY JUST KIDDING College DB FROM 2017")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"JustKidding_Admission.s3db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)









