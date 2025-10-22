import pandas as pd
import numpy as np
import math as m
data = pd.read_csv(r"C:\Users\mrabd\OneDrive\Desktop\Naive Bayes Classifier\data3.csv")
r, c = data.shape

# ----------------functions----------------------
def unique_class():          # Classes in each Column
    temp = []
    for i in range(c):
        temp.append(list(data.iloc[:,i].unique()))
    return temp
unique = unique_class()

def intro():
    print(f"\nThis program will predict the probability of {data.columns[c-1]} : {unique[c-1]}")
    print(f"The prediction of {data.columns[c-1]} is depends upon {list(data.columns[:c-1])} ")
    print("\nChoose the classes")

def take_input():
    temp = []
    for i in range(len(unique)-1):
        print(f"\nSelect : {data.columns[i]}")
        for j in range(len(unique[i])):
            print(f"{j+1}. {unique[i][j]}")

        inp = int(input("Enter your choice: "))
        temp.append(unique[i][inp-1])
    print(f"Your selected classes are : {temp}")
    return temp

def prob_of_e():
    pe = []
    for i in range(len(unique[c-1])):
        pe.append(round((data.iloc[:,c-1] == unique[c-1][i]).sum()/r,4))
    return pe

def conditional_prob():
    temp2 = []
    for i in range(len(unique[c-1])):
        temp = []
        for j in range(c - 1):
            numerator = ((data.iloc[:, j] == inputs[j]) & (data.iloc[:, c-1] == unique[c-1][i])).sum()
            denominator = pe[i] * r
            v = len(unique[j])
            value = round(float((numerator + 1) / (denominator + v)), 4)        #numerator+1/denominator+k
            temp.append(value)
        temp2.append(temp)
    return temp2

def final_result():
    temp = []
    total = []
    for i in range(len(unique[c-1])):
        total.append(pe[i] * m.prod(cond_prob[i]))
    total = sum(total)

    for i in range(len(unique[c-1])):
        print(f"\nP({unique[c - 1][i]}) : {pe[i]}")     #print probability P(E)
        for j in range(c-1):
            print(f"P({data.columns[j]} = {inputs[j]} | {unique[c - 1][i]}) : {cond_prob[i][j]}")   #Print Conditional Prob P(X|E)
        temp.append((pe[i] * m.prod(cond_prob[i]))/total)
        print("-"*80,f"\nScore of {unique[c-1][i]} is : {round(temp[i],5)}")                #  P(E)*P(X|E)
    print(f"\nThe Prediction of {data.columns[c-1]} is {unique[c-1][temp.index(max(temp))]}")
    print(f"The Sum of all probabilities : {[round(float(x),5) for x in temp]} = {round(sum(temp),3)}")     #sum of P(a,b,c,...,n)=1

# ---------------function's call--------------------
intro()
inputs = take_input()
pe = prob_of_e()
cond_prob = conditional_prob()
final_result()