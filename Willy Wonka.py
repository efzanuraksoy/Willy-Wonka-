#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 18:51:43 2023

@author: efzanuraksoy
"""

# Willy Wonka Project

# Collaborators Info:
#we read the problems and talked about what we can do.
#We worked on the project for an average of 2-3 hours a day.
#In the first problem, we all created a code draft and went through these code drafts.
#We wrote our codes by discussing each step in the first question on zoom. 
#For problem 2, we did research and watched videos to write code for graphics and tables.    
#For problem 3, we first set up the algorithm and then wrote the code.    



#Time Spent: h:m
             # 36:40 
    

########################## Problem 1 ################################
def Productivity():
    import csv
    import pandas as pd
    
    def get_raw_data(csv_file_loc):
        from collections import defaultdict
        result_list = []
        with open(csv_file_loc) as file_obj:
            reader = csv.DictReader(file_obj, fieldnames=('machine_name', 'chocolate_produced_in_this_machine',
                                                      'number_of_non_defective_units_produced', 'number_of_defective_units_produced'))
            for row in reader:
                result_list.append(dict(row))
    
    
        output = defaultdict(dict)
        for machine in result_list:
            output[machine['machine_name']]['chocolate_produced_in_this_machine'] = machine['chocolate_produced_in_this_machine']
            output[machine['machine_name']]['number_of_non_defective_units_produced'] = machine['number_of_non_defective_units_produced']
            output[machine['machine_name']]['number_of_defective_units_produced'] = machine['number_of_defective_units_produced']
        return output
    
    
    def get_ratios(csv_file_loc, chocolate_type=None):
        result = {}
        with open(csv_file_loc, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if chocolate_type is not None:
                    if row[1] == chocolate_type:
                        if row[0] in result:
                            result[row[0]].append(int(row[3]) / (int(row[2])+int(row[3])))
                        else:
                            result[row[0]] = [int(row[3]) / (int(row[2])+int(row[3]))]
                else:
                    if row[0] in result:
                        result[row[0]].append(int(row[3]) / (int(row[2]) + int(row[3])))
                    else:
                        result[row[0]] = [int(row[3]) / (int(row[2]) + int(row[3]))]
    
            return result
    
    
    def get_overall_statistic(csv_file_loc):
        res = get_overall_prod_quantities(csv_file_loc)
        total_quantities = 0
        for c, q in res.items():
            total_quantities += q
        return total_quantities
    
    
    def get_defective_prod_quantities(csv_file_loc):
        result = {}
        with open(csv_file_loc, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if row[0] in result:
                    result[row[0]].append(int(row[3]))
                else:
                    result[row[0]] = [int(row[3])]
    
            for k, v in result.items():
                t = 0
                for i in v:
                    t += i
                result[k] = t
            return result
    
    
    def get_nondefective_prod_quantities(csv_file_loc):
        result = {}
        with open(csv_file_loc, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if row[0] in result:
                    result[row[0]].append(int(row[2]))
                else:
                    result[row[0]] = [int(row[2])]
    
            for k, v in result.items():
                t = 0
                for i in v:
                    t += i
                result[k] = t
            return result
    
    
    def get_overall_prod_quantities(csv_file_loc):
        result = {}
        with open(csv_file_loc, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if row[1] in result:
                    result[row[1]].append(int(row[2])+int(row[3]))
                else:
                    result[row[1]] = [int(row[2])+int(row[3])]
            for k, v in result.items():
                t = 0
                for i in v:
                    t += i
                result[k] = t
            return result
    
    
    def visualise(my_dict):
        print("{:<15} {:<10}".format('Chocolate Type', 'Total produced number'))
        for k, v in my_dict.items():
            print("{:<15} {:<10}".format(k, v))
    
    
    while True:
        print("*" * 70)
        print("Willy Wonka's Production line Tracking Program")
        print("*" * 70)
        print("Select an operation:")
        print("1-Display the overall production quantities")
        print("2-Display the production quantities for a specific product")
        print("3-Display the most reliable more machine")
        print("4-Display the most reliable more machine for a specific product")
        print("5-Display the production percentages of all machines")
        print("0-EXIT")
        print("*" * 70)
        menu = int(input("Enter the number:"))
    
        prod_csv_file = 'production.csv'
        if menu == 0:
            if True:
                print()
                print("***************************************************")
                print("                Willy Wonka Factory System")
                print("***************************************************")
                print("1. Productivity")
                print("2. Forecasting")
                print("3. Simulation")
                print("0. EXIT")
                print("***************************************************")
                
                choice = input("Select module: ")
                if choice.isdigit():
                    choice = int(choice)
                else:
                    choice = 0    
                
                if choice == 1:
                    Productivity()
                elif choice == 2:
                    Forecasting()
                elif choice == 3:
                    Simulation()
                else:
                    break
                
                

        
        if menu == 1:
            res = get_overall_prod_quantities(prod_csv_file)
            production2020 = pd.DataFrame(res, index=[2020,])
            production2020.to_csv (r'pro.csv', index = True, header=True)
            #print(production2020)
            visualise(res)
    
        if menu == 2:
            res = get_overall_prod_quantities(prod_csv_file)
            name = input("Enter the name of Chocolate:").capitalize()
            try:
                print(f"== Production Quantities of {name}: " + str(res[name]) + " ==")
            except:
                print("Wrong product name")
    
        if menu == 3:
            print(" == Smallest ratio == ")
            ratio_list = get_ratios(prod_csv_file)
            smallest_machine = min(ratio_list, key=ratio_list.get)
            print(f"Machine: {smallest_machine} | Ratio (defective units/total units): {ratio_list[smallest_machine]}")
            print(ratio_list)
    
        if menu == 4:
            name = input("Enter the name of Chocolate:").capitalize()
            try:
                ratio_list = get_ratios(prod_csv_file, name)
                smallest_machine = min(ratio_list, key=ratio_list.get)
                print(f"{smallest_machine} Machine has smallest ratio")
                print(f"Chocolate: {name} | Machine: {smallest_machine} | Ratio (defective units/total units): {ratio_list[smallest_machine]}")
            except:
                print("Wrong product name")
    
        if menu == 5:
            from collections import Counter
            res = get_overall_statistic(prod_csv_file)
            pq = get_overall_prod_quantities(prod_csv_file)
            defectives = get_defective_prod_quantities(prod_csv_file)
            non_defectives = get_nondefective_prod_quantities(prod_csv_file)
            A = Counter(defectives)
            B = Counter(non_defectives)
            tot = dict(A+B)
            data = get_raw_data(prod_csv_file)
            c_q = get_overall_prod_quantities(prod_csv_file)
            for m, v in tot.items():
                chocolate_type = data[m]['chocolate_produced_in_this_machine']
                print("{} is producing {}% of all chocolates and {}% of {}"
                      .format(m, round((v*100) / sum(pq.values()), 1),
                              round((v*100) / int(c_q[chocolate_type]), 1), chocolate_type))
                
########################## Problem 2 ################################
def Forecasting():
    import pandas as pd
    from numpy.random import randint
    import matplotlib.pyplot as plt

    def Visualise(df, title):
            
        df.plot()
        
        ax1 = plt.axes()
        x_axis = ax1.axes.get_xaxis()    
        x_axis.set_visible(False)
        
        the_table = plt.table(cellText=df.T.values,
                              rowLabels=df.T.index,                      
                              colLabels=df.T.columns,
                              loc='bottom')
        
        the_table.auto_set_font_size(False)    
        the_table.set_fontsize(8)
            
        plt.subplots_adjust(left=0.1, bottom=0.1)            
        plt.title(title)     
        plt.legend(bbox_to_anchor=(0.5, -0.35), loc='upper center', fontsize = "small" ,ncol=5)    
       
        plt.show()
    
    def PredictProductions(data):
        
        rows = data.columns
        print(rows)
        df = pd.DataFrame(data)
        lastYear = df.index[0];
        
        for i in range(10):
            for j in range(len(df.columns)):
                growth = (randint(-2, 6)+100)/100
                print(growth)
                predictedValue = growth * df.at[lastYear + i,rows[j]]
                df.at[lastYear + i + 1,rows[j]] = predictedValue
                
        df = df.astype(int)
        print(df)
        return df;
        
    #################################################################
    
    dfLastYear = pd.read_csv("pro.csv", index_col=0)
    
    dfPrediction = PredictProductions(dfLastYear)
    Visualise(dfPrediction, "Production")
    
    df = dfPrediction.diff().loc[2021:]
    df['Total'] = df.sum(axis=1)
    
    df = df.astype(int)
    Visualise(df, "Production Differences")
    
########################## Problem 3 ################################
def Simulation():
    def coordinatesofbumblebee1(x, y):
        import random
        possibilities = random.randint(1, 100)
        if possibilities <= 80:
            return x+1, y
        elif possibilities <= 90:
            return x, y+1
        else:
            return x, y-1
    
    def coordinatesofbumblebee2(x, y):
        import random
        possibilities=random.randint(1,100)
        if y_start==3:
            if possibilities<=50:   
                return x+1, y
            elif possibilities<=75:
                return x, y+1
            else :
                return x,y-1     
        elif y_start==1 or y_start==2:
            if possibilities<=50:   
                return x,y+1
            elif possibilities<=90:
                return x+1,y 
            else:
                return x,y-1
        elif y_start==4 or y_start==5:
            if possibilities<=50:  
                return x,y-1
            elif possibilities<=90:
                return x+1,y
            else:
                return x, y+1
            
    def coordinatesofbumblebee3(x,y):
        import random
        possibilities=random.randint(1,100)
        if y_start==3:
            if possibilities<=20:   
                return x+1, y
            elif possibilities<=60:
                return x, y+1
            else :
                return x,y-1     
        elif y_start==1 or y_start==5:
            if possibilities<=30:   
                return x+1, y
            elif possibilities<=90:
                if y_start==1:
                    return x, y+1
                elif y_start==5:
                    return x, y-1 
            else:
                if y_start==1:
                    return x, y-1
                elif y_start==5:
                    return x, y+1 
        elif y_start==2 or y_start==4:
            if possibilities<=20:
                return x+1,y
            elif possibilities<=60:
                return x, y+1
            else :
                return x, y-1 
    
    if __name__ == '__main__':
        malfunction = 0
        d={}
        for r in ["b1", "b2","b3"]:
            for s in range(1000000):
                x_start = 0
                y_start = 3
                for i in range(200):
                    if r == "b1":
                        x_start, y_start = coordinatesofbumblebee1(x_start, y_start)
                    elif r == "b2":
                        x_start, y_start = coordinatesofbumblebee2(x_start, y_start)
                    elif r == "b3":
                        x_start, y_start = coordinatesofbumblebee3(x_start, y_start)
                    if i == 0 and (y_start != 3 and x_start == 0):
                        malfunction += 1
                        break
                    elif y_start == 6 or y_start == 0:
                        malfunction +=1
                        break
                d[r]=malfunction
                
        
        a=d['b2']-d['b1']
        b=d['b3']-d['b2']
        s={}
        s["Bumblebee1"]=d['b1']
        s["Bumblebee2"]=a
        s["Bumblebee3"]=b
        print(s)
        lowest_key = min(s, key=s.get)
        print("The least malfunction is", lowest_key,"it's value:",s[lowest_key])
        
       
        
print()
print("***************************************************")
print("                Willy Wonka Factory System")
print("***************************************************")
print("1. Productivity")
print("2. Forecasting")
print("3. Simulation")
print("0. EXIT")
print("***************************************************")

    
choice = input("Select module: ")
if choice.isdigit():
    choice = int(choice)
else:
    choice = 0    

if choice == 1:
    Productivity()
elif choice == 2:
    Forecasting()
elif choice == 3:
    Simulation()

    
               
    
            
                        
                
                
                
 
                