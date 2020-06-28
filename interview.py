import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sat.csv')


def question1():
	result = df["School Name"].nunique()
	return result

def question2():
	result = df['Number of Test Takers'].isnull().sum()
	return result

def question3():
	SNTT = df[df['Number of Test Takers'].max() == df['Number of Test Takers']]['School Name'].iloc[0]
	NNTT = df[df['Number of Test Takers'].max() == df['Number of Test Takers']]['Number of Test Takers'].iloc[0]
	

	SCRM = df[df['Critical Reading Mean'].max() == df['Critical Reading Mean']]['School Name'].iloc[0]
	NCRM = df[df['Critical Reading Mean'].max() == df['Critical Reading Mean']]['Number of Test Takers'].iloc[0]

	SMM = df[df['Mathematics Mean'].max() == df['Mathematics Mean']]['School Name'].iloc[0]
	NMM = df[df['Mathematics Mean'].max() == df['Mathematics Mean']]['Number of Test Takers'].iloc[0]

	SWM = df[df['Writing Mean'].max() == df['Writing Mean']]['School Name'].iloc[0]
	NWM = df[df['Writing Mean'].max() == df['Writing Mean']]['Number of Test Takers'].iloc[0]
	
	

	resutTest = f'Number of Test Takers : {SNTT} with {NNTT}'
	resultRead = f'Critical Reading Mean : {SCRM} with {NCRM}'
	resultMath = f'Mathematics Mean : {SMM} with {NMM}'
	resuktWrite = f'Writing Mean : {SWM} with {NWM}'

	result = f'\t{resutTest}\n\t{resultRead}\n\t{resultMath}\n\t{resuktWrite}'
	return result

def question4():
	
	df['Divergent Scores'] = abs(df['Mathematics Mean'] - df['Critical Reading Mean'])

	sResult = df[df.groupby('School Name').sum().sort_values('Divergent Scores', ascending = False)['Divergent Scores'].max() == df['Divergent Scores']]['School Name'].iloc[0]
	nResult = df[df.groupby('School Name').sum().sort_values('Divergent Scores', ascending = False)['Divergent Scores'].max() == df['Divergent Scores']]['Divergent Scores'].iloc[0]
	result = f'{sResult} has the most divergent scores between mathematics and critical reading with {nResult}'
	return result


def question5():
	df['Total Mathematic Score'] = df['Number of Test Takers'] * df['Mathematics Mean']
	totalTest = int(df['Number of Test Takers'].sum())
	totalScore = df['Total Mathematic Score'].sum()
	mean = round(totalScore/totalTest,0)
	result = f'The Mathematics mean is {mean} ,from {df["School Name"].nunique()} different schools and {totalTest} tests'
	return result

print(f'{question1()} schools are tracked in this database')
print(f'{question2()} schools have no associated testing information')
print(f'The overall scores scholls are : \n{question3()}')
print(question4())
# Calculate the general  Mathematics mean of all tests from all schools for question 5.
print(question5())


def BonusQuestion():
	# Create three grapf which show the means of 10 shcools for three test with school names.
	
	fig,axs = plt.subplots(3)
	fig.suptitle("The Schools and Tests Means")
	
	axs[0].plot(df.dropna().head(10)['Critical Reading Mean'],df.dropna().head(10)['School Name'],"o--b")
	axs[0].set_title("Critical Reading Mean")
	axs[1].plot(df.dropna().head(10)['Mathematics Mean'],df.dropna().head(10)['School Name'],"o--g")
	axs[1].set_title("Mathematics Mean")
	axs[2].plot(df.dropna().head(10)['Writing Mean'],df.dropna().head(10)['School Name'],"o--y")
	axs[2].set_title("Writing Mean")
	plt.tight_layout()
	
	plt.show()
	
BonusQuestion()
