# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:50:57 2022

@author: daksh.sahni
"""

#Calling libraries
import pandas as pd
from  rake_nltk import Rake  
import nltk
nltk.download('stopwords')
nltk.download('punkt')

#Importing Data
wallet = "C:/Work/Codes/keyword_extraction_learningwallet/Learning Wallet approved 1 Sep 21 - 21 Jan 22.xlsx"
df = pd.read_excel(wallet)
#df.info()

#Initializing Rake - Rapid Automatic Keyword Extraction (RAKE) algorithm
r = Rake()  

#Defining Function to get rake
def rake_implement(x,r):
     r.extract_keywords_from_text(x)
     return r.get_ranked_phrases()

#Applying Function
df['Expense_Desc_rake'] =df['Expense Description'].apply(lambda x: rake_implement(x,r))
#print(df['Expense_Desc_rake'])

df['ClaimTitle_rake'] =df['Claim Title'].apply(lambda x: rake_implement(x,r))
#print(df['ClaimTitle_rake'])

#Breaking it down further to categories - Books, Subscription, harvard business review, Course, Kindle,Certificate, Newsletter,

import numpy as np

bookattributes = ["book","edition","reckoner","paperback","amazon","go"]
subsattributes = ['subscription','subscribe','hbr','harvard','digital','ken','toastmasters']
newsletterattributes =['news','newsletter','publication']
courseattributes = ['course','docker','video','session','university']
certattributes = ['certification','certificate','certified','cert']
softwareattributes = ['grammarly','adobe']
hardwareattributes =['kindle']

"""

def category(row):
    if row.str.contains('book'):
        return "Book"
    if row.str.contains('subscription'):
        return "Subscription"
    if row.str.contains('harvard'):
        return "Subscription"
    if row.str.contains('course'):
        return "Online Course"
    if row.str.contains('certificat'):
        return "Certification"
    if row.str.contains('newsletter'):
        return "Newsletter"
    else:
        return "Others"
    exit
"""

#function = np.vectorize(category)

#df['Expense Category']=function(df['Expense_Desc_rake'])

df['Expense Description']=df['Expense Description'].str.lower()

df['Expense_Category_'] = np.where(df['Expense Description'].str.contains('book|edition|reckoner|paperback|amazon|go|bestseller|audible',na=False),"book",
                                   np.where(df['Expense Description'].str.contains('subscription|subscribe|hbr|harvard|digital|ken|toastmasters|membership',na=False),"subscription",
                                            np.where(df['Expense Description'].str.contains('news|newsletter|publication|articles',na=False),"newsletter",
                                                     np.where(df['Expense Description'].str.contains('course|docker|video|session|udemy|university|mba|institute|program',na=False),"course",
                                                              np.where(df['Expense Description'].str.contains('certification|certificate|certified|cert',na=False),"certification",
                                                                       np.where(df['Expense Description'].str.contains('grammarly|adobe',na=False),"software",
                                                                                np.where(df['Expense Description'].str.contains('kindle',na=False),"Kindle","others"
                                                                                         )
                                                                                )
                                                                       )
                                                              )
                                                     )
                                            )
                                   )

#export
df.to_excel("C:/Work/Codes/keyword_extraction_learningwallet/LW_28JAN2022.xlsx")
df.info()




 