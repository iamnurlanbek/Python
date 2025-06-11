import pandas as pd
df = pd.read_csv(r'C:\Python\lesson-18\homework\tackoverflow_qa.csv', index_col='quest_name')
# print(df)



"""Find all questions that were created before 2014
"""
df['creationdate'] = pd.to_datetime(df['creationdate'])
filtered = df[df['creationdate'] < '2014-01-01']
print(filtered)


"""Find all questions with a score more than 50
"""
filtered_questions = df[df['score'] > 50][['title', 'score']]
print(filtered_questions)


"""Find all questions with a score between 50 and 100
"""
filtered_questions = df[df['score'].between(50,100)][['title', 'score']]
print(filtered_questions)

"""Find all questions answered by Scott Boston
# """
filtered_questions = df[df['ans_name'] == 'Scott Boston'][['title', 'ans_name']]
print(filtered_questions)


"""# Find all questions answered by the following 5 users
"""
users = df['ans_name'].head()
print(users)


"""# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
"""
df['creationdate'] = pd.to_datetime(df['creationdate'])
filtered_date = df['creationdate'].between('2014-03-01', '2014-10-31')
answered = df['ans_name'] == 'Unutbu'
score = df['score'] < 5
result = filtered_date & score & answered
print(df[result][['ans_name', 'creationdate', 'score', 'title']])




"""Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
"""
filtered_questions =df[(df['score'].between(5,10))|(df['viewcount'] > 10000)][['score', 'viewcount']]
print(filtered_questions)


"""Find all questions that are not answered by Scott Boston"""
filtered_questions = df['ans_name'] != 'Scott Boston'
print(df[filtered_questions]['ans_name'])



"""Homework 2"""

df = pd.read_csv(r'C:\Python\lesson-18\homework\titanic.csv')
# print(df)

"""
Select Female Passengers in Class 1 with Ages between 20 and 30: 
Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
"""
df.rename(columns={'Pclass':'Class'}, inplace=True)
gender = df['Sex'] == 'female'
ages = df['Age'].between(20,30)
pclass = df['Class'] == 1
result = gender & ages & pclass
print(df[result][['Class', 'Name', 'Sex', 'Age']])


"""
Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
"""
filtered_titanic = df[df['Fare'] > 100][['Name', 'Fare']]
print(filtered_titanic)



"""Select Passengers Who Survived and Were Alone: 
Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
"""
survived_passenger = df['Survived'] == 1
siblings = df['SibSp'] == 0
parch = df['Parch'] == 0
result = df[survived_passenger & siblings & parch][['Name', 'SibSp', 'Parch', 'Survived']]
print(result)


"""
Filter Passengers Embarked from 'C' and Paid More Than $50: 
Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
"""
embarked_C = df['Embarked'] == 'C'
fare = df['Fare'] > 50
result = df[embarked_C & fare][['Name', 'Fare', 'Embarked']]
print(result)


"""
Select Passengers with Siblings or Spouses and Parents or Children:
Extract passengers who had both siblings or spouses aboard and parents or children aboard.
"""

siblings = df['SibSp'] != 0
parch = df['Parch'] != 0
result = df[siblings & parch][['Name', 'SibSp', 'Parch']]
print(result)


"""
Filter Passengers Aged 15 or Younger Who Didn't Survive: 
Create a DataFrame with passengers aged 15 or younger who did not survive.
# """
result = df[(df['Age'] <= 15) & (df['Survived'] == 0)][['Name', 'Age', 'Sex']]
print(result)


"""
Select Passengers with Cabins and Fare Greater Than $200:
Extract passengers with known cabin numbers and a fare greater than $200. 
"""
cabin = df['Cabin'].notna()
fare = df['Fare'] > 200
result = cabin & fare
print(df[result][['Name', 'Fare', 'Cabin']])

""" 
Filter Passengers with Odd-Numbered Passenger IDs: 
Create a DataFrame with passengers whose PassengerId is an odd number.
"""
passengers = df[df['PassengerId'] % 2 != 0][['Name', 'Sex', 'PassengerId']]
print(passengers)



"""
Select Passengers with Unique Ticket Numbers: 
Extract a DataFrame with passengers having unique ticket numbers.
"""
ticket_counts = df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
result = df[df['Ticket'].isin(unique_tickets)][['Name', 'Ticket']]
print(result)


"""
Filter Passengers with 'Miss' in Their Name and Were in Class 1:
Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
"""

female_passengers = df['Name'].str.contains('Miss')
class1 = df['Pclass'] == 1
result = df[female_passengers & class1][['Name', 'Sex', 'Pclass']]
print(result)