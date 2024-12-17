# Programmer: Keaton LaBorde Noah Kohler
# Assignment: Final Project
# Course: CSCI/ISAT B104 - Spring 2023

# Importing the libraries used

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Import excel data

df = pd.read_excel("Actual_Project_Data.xlsx")

# Validating User input for graphs

def Main():
    
    # Validating User input for graphs
    print("\n~~~~~~~~~~~~Welcome to our project about Weaponry on School Property~~~~~~~~~~~~")
    print("\nWhat kind of graph would you like to see?")
    print("---------------------------------------------")
    for i in range(1,7):
        if i == 1:
            print(f"\n{i}. Bar Graph")
        elif i == 2:
            print(f"{i}. Zoomed In Bar Graphs")
        elif i == 3:
            print(f"{i}. Box Plot")
        elif i == 4:
            print(f"{i}. Heatmap")
        elif i == 5:
            print(f"{i}. All Graphs")
        elif i == 6:
            print(f"{i}. No more?")
    input_is_valid = False
    while input_is_valid == False:
        try: 
            user_input = input("Enter a number from 1-5: ")
            user_input = int(user_input)
            if (1 <= user_input <= 6):
                input_is_valid = True
            else:   
                print(f"{user_input} is NOT a valid graph from 1-5. ")
        except:
              print(f"{user_input} is NOT a valid integer.")
        if user_input == 1:
            print(BarChoice())
        elif user_input == 2:
            print(ZoomedBarChoice())
        elif user_input == 3:
            print(BoxPlotChoice())
        elif user_input == 4:
            print(Heatmap())
        elif user_input == 5:
            print(AllGraphs())
        elif user_input == 6:
            print("\nThank you!")


# User Wants to see BarGraph

def BarChoice():
    print("\nWhat kind of Bar graph would you like to see?")
    print("--------------------------------------------------")
    for i in range(1,8):
        if i == 1:
            print(f"\n{i}. Weapon Carriages vs. Weapon Threatens")
        elif i == 2:
            print(f"{i}. Gender vs. Weapon Carriage")
        elif i == 3:
            print(f"{i}. Gender vs. Weapon Threatens")
        elif i == 4:
            print(f"{i}. Age vs. Weapon Carriage")
        elif i == 5:
            print(f"{i}. Age vs. Weapon Threatens")
        elif i == 6:
            print(f"{i}. Sexual Orientation vs. Weapon Carriage")
        elif i == 7:
            print(f"{i}. Sexual Orientation vs. Weapon Threatens")
    input_is_valid = False
    while input_is_valid == False:
        try: 
            user_input = input("Please select what kind of bargrph you would like to see from 1-7: ")
            user_input = int(user_input)
            if 1 <= user_input <= 7:
                input_is_valid = True
            else:   
                print(f"{user_input} is NOT a valid integer 1-7. Please input a number 1-7: ")
        except:
              print(f"{user_input} is NOT a valid integer 1-7. Please input a number 1-7: ")
    
# Bar graph

    def BarGraph():
        bar_graph = user_input
        if bar_graph == 1:
            print("\n Weapon Carriages vs. Weapon Threatens")
            print("-------------------------------------------\n")
            filt_q13_q16 = df[["q16", "q13"]].value_counts().sort_index(ascending = True) # Used to isolate 2 columns and count each number within
            q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_q13_q16.iloc[:8] # Grabs the data from the isolated dataframe
            answer2 = filt_q13_q16.iloc[8:16]
            answer3 = filt_q13_q16.iloc[16:24]
            answer4 = filt_q13_q16.iloc[24:32]
            answer5 = filt_q13_q16.iloc[32:40]
            barwidth = .2
            xpos = np.arange(len(q16))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
            plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
            plt.xticks(xpos, q16)
            plt.title("Weapon Carriages vs. Weapon Threatens")
            plt.xlabel("Weapon Threatens (Times)")
            plt.ylabel("Answers")
            plt.legend()
            plt.show()
        elif bar_graph == 2:
            print("\n Gender vs. Weapon Carriages")
            print("-------------------------------------------\n")
            filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
            q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_sex_q16.iloc[:8]
            answer2 = filt_sex_q16.iloc[8:16]
            barwidth = .2
            xpos = np.arange(len(q16))
            plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
            plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
            plt.xticks(xpos, q16)
            plt.title("Gender vs. Weapon Threatens")
            plt.xlabel("Times")
            plt.ylabel("Weapon Carriage answered")
            plt.legend()
            plt.show()
        elif bar_graph == 3:
            print("\n Gender vs. Weapon Threantens")
            print("-------------------------------------------\n")
            filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
            q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_sex_q16.iloc[:8]
            answer2 = filt_sex_q16.iloc[8:16]
            barwidth = .2
            xpos = np.arange(len(q16))
            plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
            plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
            plt.xticks(xpos, q16)
            plt.title("Gender vs. Weapon Threatens")
            plt.xlabel("Times")
            plt.ylabel("Weapon Carriage Answered")
            plt.legend()
            plt.show()
        elif bar_graph == 4:
            print("\n Age vs. Weapon Carriages")
            print("-------------------------------------------\n")
            filt_age_q13 = df[["q13", "age"]].value_counts().sort_index(ascending = True)
            age = ["12", "13", "14", "15", "16", "17", "18+"]
            answer1 = filt_age_q13.iloc[:7]
            answer2 = filt_age_q13.iloc[7:14]
            answer3 = filt_age_q13.iloc[14:21]
            answer4 = filt_age_q13.iloc[21:28]
            answer5 = filt_age_q13.iloc[28:35]
            barwidth = .2
            xpos = np.arange(len(age))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
            plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
            plt.xticks(xpos, age)
            plt.title("Age vs. Weapon Carriage")
            plt.xlabel("Age")
            plt.ylabel("Weapon Carriage")
            plt.legend()
            plt.show()
        elif bar_graph == 5:
            print("\n Age vs. Weapon Threatens")
            print("-------------------------------------------\n")
            barwidth = .4
            filt_age_q16 = df[["q16", "age"]].value_counts().sort_index(ascending = True)
            age = ["12", "13", "14", "15", "16", "17", "18+"]
            answer1 = filt_age_q16.iloc[:7]
            answer2 = filt_age_q16.iloc[7:14]
            answer3 = filt_age_q16.iloc[14:21]
            answer4 = filt_age_q16.iloc[21:28]
            answer5 = filt_age_q16.iloc[28:35]
            answer6 = filt_age_q16.iloc[35:42]
            answer7 = filt_age_q16.iloc[42:49]
            answer8 = filt_age_q16.iloc[49:56]
            barwidth = .125
            xpos = np.arange(len(age))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .125, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .25, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .375, answer4, barwidth, color = "cornflowerblue", label = "4-5")
            plt.bar(xpos + .5, answer5, barwidth, color = "deepskyblue", label = "6-7")
            plt.bar(xpos + .65, answer6, barwidth, color = "cyan", label = "8-9")
            plt.bar(xpos + .75, answer7, barwidth, color = "c", label = "10-11")
            plt.bar(xpos + .875, answer8, barwidth, color = "darkcyan", label = "12+")
            plt.xticks(xpos, age)
            plt.title("Age vs. Threatens")
            plt.xlabel("Age")
            plt.ylabel("Weapon Threatens")
            plt.legend()
            plt.show()
        elif bar_graph == 6:
            print("\n Sexual Orientation vs. Weapon Carriages")
            print("-------------------------------------------\n")
            filt_q13_sexid = df[["q13", "sexid"]].value_counts().sort_index(ascending = True)
            sexid = ["Heterosexual", "Gay/Lesbian", "Bisexual", "Not Sure"]
            answer1 = filt_q13_sexid.iloc[:4]
            answer2 = filt_q13_sexid.iloc[4:8]
            answer3 = filt_q13_sexid.iloc[8:12]
            answer4 = filt_q13_sexid.iloc[12:16]
            answer5 = filt_q13_sexid.iloc[16:20]
            barwidth = .2
            xpos = np.arange(len(sexid))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
            plt.bar(xpos + .8, answer4, barwidth, color = "deepskyblue", label = "6+")
            plt.xticks(xpos, sexid)
            plt.title("Sexual Orientation vs. Weapon Carriages")
            plt.xlabel("Weapon Threatens (Times)")
            plt.ylabel("Answers")
            plt.legend()
            plt.show()
        elif bar_graph == 7:
            print("\n Sexual Orientation vs. Weapon Threatens")
            print("-------------------------------------------\n")
            filt_q13_sexid = df[["sexid", "q16"]].value_counts().sort_index(ascending = True)
            sexid = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_q13_sexid.iloc[:8]
            answer2 = filt_q13_sexid.iloc[8:16]
            answer3 = filt_q13_sexid.iloc[16:24]
            answer4 = filt_q13_sexid.iloc[24:32]
            barwidth = .25
            xpos = np.arange(len(sexid))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "Heterosexual")
            plt.bar(xpos + .25, answer2, barwidth, color = "blue", label = "Gay or Lesbian")
            plt.bar(xpos + .5, answer3, barwidth, color = "dodgerblue", label = "Bisexual")
            plt.bar(xpos + .75, answer4, barwidth, color = "deepskyblue", label = "Not Sure")
            plt.xticks(xpos, sexid)
            plt.title("Sexual Orientation vs. Weapon Threatens")
            plt.xlabel("Weapon Threatens (Times)")
            plt.ylabel("Answers")
            plt.legend()
            plt.show()

            
    BarGraph()
    return Main()

# Zoomed In Bar Graph Choices

def ZoomedBarChoice():
    print("\nWhat kind of Zoomed in Bar graph would you like to see?")
    print("-------------------------------------------------------------")
    for i in range(1,8):
        if i == 1:
            print(f"\n{i}. Weapon Carriages vs. Weapon Threatens")
        elif i == 2:
            print(f"{i}. Gender vs. Weapon Carriage")
        elif i == 3:
            print(f"{i}. Gender vs. Weapon Threatens")
        elif i == 4:
            print(f"{i}. Age vs. Weapon Carriage")
        elif i == 5:
            print(f"{i}. Age vs. Weapon Threatens")
        elif i == 6:
            print(f"{i}. Sexual Orientation vs. Weapon Carriage")
        elif i == 7:
            print(f"{i}. Sexual Orientation vs. Weapon Threatens")
    input_is_valid = False
    while input_is_valid == False:
        try: 
            user_input = input("Please select what kind of zoomed in bargrph you would like to see from 1 to 7: ")
            user_input = int(user_input)
            if 1 <= user_input <= 7:
                input_is_valid = True
            else:   
                print(f"{user_input} is NOT a valid integer 1-7. Please input a number 1-7: ")
        except:
            print(f"{user_input} is NOT a valid integer 1-7. Please input a number 1-7: ")
         
    def ZoomedInBarGraphs():
        bar_graph = user_input
        if bar_graph == 1:
            print("\n Weapon Carriages vs. Weapon Threatens")
            print("-------------------------------------------\n")
            filt_q13_q16 = df[["q16", "q13"]].value_counts().sort_index(ascending = True)
            q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_q13_q16.iloc[:8]
            answer2 = filt_q13_q16.iloc[8:16]
            answer3 = filt_q13_q16.iloc[16:24]
            answer4 = filt_q13_q16.iloc[24:32]
            answer5 = filt_q13_q16.iloc[32:40]
            barwidth = .2
            xpos = np.arange(len(q16))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
            plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
            plt.ylim(0, 2000)
            plt.xticks(xpos, q16)
            plt.title("Weapon Carriages vs. Weapon Threatens")
            plt.xlabel("Weapon Threatens (Times)")
            plt.ylabel("Answers")
            plt.legend()
            plt.show()
        elif bar_graph == 2:
            print("\n Gender vs. Weapon Carriages")
            print("-------------------------------------------\n")
            filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
            q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_sex_q16.iloc[:8]
            answer2 = filt_sex_q16.iloc[8:16]
            barwidth = .2
            xpos = np.arange(len(q16))
            plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
            plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
            plt.ylim(0, 2000)
            plt.xticks(xpos, q16)
            plt.title("Gender vs. Weapon Threatens")
            plt.xlabel("Times")
            plt.ylabel("Weapon Carriage answered")
            plt.legend()
            plt.show()
        elif bar_graph == 3:
            print("\n Gender vs. Weapon Threantens")
            print("-------------------------------------------\n")
            filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
            q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_sex_q16.iloc[:8]
            answer2 = filt_sex_q16.iloc[8:16]
            barwidth = .2
            xpos = np.arange(len(q16))
            plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
            plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
            plt.ylim(0, 2000)
            plt.xticks(xpos, q16)
            plt.title("Gender vs. Weapon Threatens")
            plt.xlabel("Times")
            plt.ylabel("Weapon Carriage Answered")
            plt.legend()
            plt.show()
        elif bar_graph == 4:
            print("\n Age vs. Weapon Carriages")
            print("-------------------------------------------\n")
            filt_age_q13 = df[["q13", "age"]].value_counts().sort_index(ascending = True)
            age = ["12", "13", "14", "15", "16", "17", "18+"]
            answer1 = filt_age_q13.iloc[:7]
            answer2 = filt_age_q13.iloc[7:14]
            answer3 = filt_age_q13.iloc[14:21]
            answer4 = filt_age_q13.iloc[21:28]
            answer5 = filt_age_q13.iloc[28:35]
            barwidth = .2
            xpos = np.arange(len(age))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
            plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
            plt.ylim(0, 1000)
            plt.xticks(xpos, age)
            plt.ylim(0, 5000)
            plt.title("Age vs. Weapon Carriage")
            plt.xlabel("Age")
            plt.ylabel("Weapon Carriage")
            plt.legend()
            plt.show()
        elif bar_graph == 5:
            print("\n Age vs. Weapon Threatens")
            print("-------------------------------------------\n")
            barwidth = .4
            filt_age_q16 = df[["q16", "age"]].value_counts().sort_index(ascending = True)
            age = ["12", "13", "14", "15", "16", "17", "18+"]
            answer1 = filt_age_q16.iloc[:7]
            answer2 = filt_age_q16.iloc[7:14]
            answer3 = filt_age_q16.iloc[14:21]
            answer4 = filt_age_q16.iloc[21:28]
            answer5 = filt_age_q16.iloc[28:35]
            answer6 = filt_age_q16.iloc[35:42]
            answer7 = filt_age_q16.iloc[42:49]
            answer8 = filt_age_q16.iloc[49:56]
            barwidth = .125
            xpos = np.arange(len(age))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .125, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .25, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .375, answer4, barwidth, color = "cornflowerblue", label = "4-5")
            plt.bar(xpos + .5, answer5, barwidth, color = "deepskyblue", label = "6-7")
            plt.bar(xpos + .65, answer6, barwidth, color = "cyan", label = "8-9")
            plt.bar(xpos + .75, answer7, barwidth, color = "c", label = "10-11")
            plt.bar(xpos + .875, answer8, barwidth, color = "darkcyan", label = "12+")
            plt.ylim(0, 1000)
            plt.xticks(xpos, age)
            plt.title("Age vs. Threatens")
            plt.xlabel("Age")
            plt.ylabel("Weapon Threatens")
            plt.legend()
            plt.show()
        elif bar_graph == 6:
            print("\n Sexual Orientation vs. Weapon Carriages")
            print("-------------------------------------------\n")
            filt_q13_sexid = df[["q13", "sexid"]].value_counts().sort_index(ascending = True)
            sexid = ["Heterosexual", "Gay/Lesbian", "Bisexual", "Not Sure"]
            answer1 = filt_q13_sexid.iloc[:4]
            answer2 = filt_q13_sexid.iloc[4:8]
            answer3 = filt_q13_sexid.iloc[8:12]
            answer4 = filt_q13_sexid.iloc[12:16]
            answer5 = filt_q13_sexid.iloc[16:20]
            barwidth = .2
            xpos = np.arange(len(sexid))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
            plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
            plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
            plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
            plt.bar(xpos + .8, answer4, barwidth, color = "deepskyblue", label = "6+")
            plt.ylim(0,2000)
            plt.xticks(xpos, sexid)
            plt.title("Sexual Orientation vs. Weapon Carriages")
            plt.xlabel("Weapon Threatens (Times)")
            plt.ylabel("Answers")
            plt.legend()
            plt.show()
        elif bar_graph == 7:
            print("\n Sexual Orientation vs. Weapon Threatens")
            print("-------------------------------------------\n")
            filt_q13_sexid = df[["sexid", "q16"]].value_counts().sort_index(ascending = True)
            sexid = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
            answer1 = filt_q13_sexid.iloc[:8]
            answer2 = filt_q13_sexid.iloc[8:16]
            answer3 = filt_q13_sexid.iloc[16:24]
            answer4 = filt_q13_sexid.iloc[24:32]
            barwidth = .25
            xpos = np.arange(len(sexid))
            plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "Heterosexual")
            plt.bar(xpos + .25, answer2, barwidth, color = "blue", label = "Gay or Lesbian")
            plt.bar(xpos + .5, answer3, barwidth, color = "dodgerblue", label = "Bisexual")
            plt.bar(xpos + .75, answer4, barwidth, color = "deepskyblue", label = "Not Sure")
            plt.ylim(0, 2000)
            plt.xticks(xpos, sexid)
            plt.title("Sexual Orientation vs. Weapon Threatens")
            plt.xlabel("Weapon Threatens (Times)")
            plt.ylabel("Answers")
            plt.legend()
            plt.show()

            
    ZoomedInBarGraphs()
    return Main()

# Box Plot choices

def BoxPlotChoice():
    print("\nWhat kind of Box plot would you like to see?")
    print("-------------------------------------------------")
    for i in range(1,3):
        if i == 1:
            print(f"\n{i}. BMI vs. Weapon Carriage")
        elif i == 2:
            print(f"{i}. BMI vs. Weapon Threatens")
    input_is_valid = False
    while input_is_valid == False:
        try: 
            user_input = input("Please select what kind of box plot you would like to see 1 or 2: ")
            user_input = int(user_input)
            if 1 <= user_input <= 2:
                input_is_valid = True
            else:   
                print(f"{user_input} is NOT a valid integer between 1 or 2. Please input a number 1 or 2. ")
        except:
              print(f"{user_input} is NOT a valid integer between 1 or 2. Please input a number 1 or 2. ")

    
# Box Plots

    def BoxPlots():
        box_plot = user_input
        if box_plot == 1:
            print("\n Weight vs. Weapon Carriage")
            print("-------------------------------------------\n")
            plt.title("BMI and Weapon Carriage")
            sns.boxplot(x = "q13", y = "BMI", data = df, palette="Blues")
            plt.ylim(0, 80)
            plt.show()
        elif box_plot == 2:
            print("\n Weight vs. Weapon Threatens")
            print("-------------------------------------------\n")
            plt.title("Weight and Weapon Threatens")
            sns.boxplot(x = "q16", y = "BMI", data = df, palette="Blues")
            plt.ylim(0, 80)
            plt.show()
    BoxPlots()
    return Main()

# Heatmap

def Heatmap():
    print("\nHeatmap")
    print("---------")
    corr = df.corr()
    sns.heatmap(corr, annot = True, cmap = "Blues")
    plt.show()
    return Main()


# All Graphs

def AllGraphs():
    
    # Bar Graphs
    
    print("\n Weapon Carriages vs. Weapon Threatens")
    print("-------------------------------------------\n")
    filt_q13_q16 = df[["q16", "q13"]].value_counts().sort_index(ascending = True)
    q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_q13_q16.iloc[:8]
    answer2 = filt_q13_q16.iloc[8:16]
    answer3 = filt_q13_q16.iloc[16:24]
    answer4 = filt_q13_q16.iloc[24:32]
    answer5 = filt_q13_q16.iloc[32:40]
    barwidth = .2
    xpos = np.arange(len(q16))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
    plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
    plt.xticks(xpos, q16)
    plt.title("Weapon Carriages vs. Weapon Threatens")
    plt.xlabel("Weapon Threatens (Times)")
    plt.ylabel("Answers")
    plt.legend()
    plt.show()
    
    print("\n Gender vs. Weapon Carriages")
    print("-------------------------------------------\n")
    filt_sex_q13 = df[["sex", "q13"]].value_counts().sort_index(ascending = True)
    q13 = ["0", "1", "2-3", "4-5", "6+"]
    answer1 = filt_sex_q13.iloc[:5]
    answer2 = filt_sex_q13.iloc[5:10]
    barwidth = .4
    xpos = np.arange(len(q13))
    plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
    plt.bar(xpos + .4, answer2, barwidth, color = "dodgerblue", label = "Male")
    plt.xticks(xpos, q13)
    plt.title("Gender vs. Weapon Carriage")
    plt.xlabel("Times")
    plt.ylabel("Weapon Carriage Answered")
    plt.legend()
    plt.show()
    
    
    print("\n Gender vs. Weapon Threantens")
    print("-------------------------------------------\n")
    filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
    q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_sex_q16.iloc[:8]
    answer2 = filt_sex_q16.iloc[8:16]
    barwidth = .2
    xpos = np.arange(len(q16))
    plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
    plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
    plt.xticks(xpos, q16)
    plt.title("Gender vs. Weapon Threatens")
    plt.xlabel("Times")
    plt.ylabel("Weapon Carriage Answered")
    plt.legend()
    plt.show()
    
    
    print("\n Age vs. Weapon Carriages")
    print("-------------------------------------------\n")
    filt_age_q13 = df[["q13", "age"]].value_counts().sort_index(ascending = True)
    age = ["12", "13", "14", "15", "16", "17", "18+"]
    answer1 = filt_age_q13.iloc[:7]
    answer2 = filt_age_q13.iloc[7:14]
    answer3 = filt_age_q13.iloc[14:21]
    answer4 = filt_age_q13.iloc[21:28]
    answer5 = filt_age_q13.iloc[28:35]
    barwidth = .2
    xpos = np.arange(len(age))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
    plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
    plt.xticks(xpos, age)
    plt.title("Age and Weapon Carriage")
    plt.xlabel("Age")
    plt.ylabel("Weapon Carriage")
    plt.legend()
    plt.show()


    print("\n Age vs. Weapon Threatens")
    print("-------------------------------------------\n")
    barwidth = .4
    filt_age_q16 = df[["q16", "age"]].value_counts().sort_index(ascending = True)
    age = ["12", "13", "14", "15", "16", "17", "18+"]
    answer1 = filt_age_q16.iloc[:7]
    answer2 = filt_age_q16.iloc[7:14]
    answer3 = filt_age_q16.iloc[14:21]
    answer4 = filt_age_q16.iloc[21:28]
    answer5 = filt_age_q16.iloc[28:35]
    answer6 = filt_age_q16.iloc[35:42]
    answer7 = filt_age_q16.iloc[42:49]
    answer8 = filt_age_q16.iloc[49:56]
    barwidth = .125
    xpos = np.arange(len(age))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .125, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .25, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .375, answer4, barwidth, color = "cornflowerblue", label = "4-5")
    plt.bar(xpos + .5, answer5, barwidth, color = "deepskyblue", label = "6-7")
    plt.bar(xpos + .65, answer6, barwidth, color = "cyan", label = "8-9")
    plt.bar(xpos + .75, answer7, barwidth, color = "c", label = "10-11")
    plt.bar(xpos + .875, answer8, barwidth, color = "darkcyan", label = "12+")
    plt.xticks(xpos, age)
    plt.title("Age and Threatens")
    plt.xlabel("Age")
    plt.ylabel("Weapon Threatens")
    plt.legend()
    plt.show()
    
    
    print("\n Sexual Orientation vs. Weapon Carriages")
    print("-------------------------------------------\n")
    filt_q13_sexid = df[["q13", "sexid"]].value_counts().sort_index(ascending = True)
    sexid = ["Heterosexual", "Gay/Lesbian", "Bisexual", "Not Sure"]
    answer1 = filt_q13_sexid.iloc[:4]
    answer2 = filt_q13_sexid.iloc[4:8]
    answer3 = filt_q13_sexid.iloc[8:12]
    answer4 = filt_q13_sexid.iloc[12:16]
    answer5 = filt_q13_sexid.iloc[16:20]
    barwidth = .2
    xpos = np.arange(len(sexid))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
    plt.bar(xpos + .8, answer4, barwidth, color = "deepskyblue", label = "6+")
    plt.xticks(xpos, sexid)
    plt.title("Sexual Orientation vs. Weapon Carriages")
    plt.xlabel("Weapon Threatens (Times)")
    plt.ylabel("Answers")
    plt.legend()
    plt.show()
    
    
    print("\n Sexual Orientation vs. Weapon Threatens")
    print("-------------------------------------------\n")
    filt_q13_sexid = df[["sexid", "q16"]].value_counts().sort_index(ascending = True)
    sexid = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_q13_sexid.iloc[:8]
    answer2 = filt_q13_sexid.iloc[8:16]
    answer3 = filt_q13_sexid.iloc[16:24]
    answer4 = filt_q13_sexid.iloc[24:32]
    barwidth = .25
    xpos = np.arange(len(sexid))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "Heterosexual")
    plt.bar(xpos + .25, answer2, barwidth, color = "blue", label = "Gay or Lesbian")
    plt.bar(xpos + .5, answer3, barwidth, color = "dodgerblue", label = "Bisexual")
    plt.bar(xpos + .75, answer4, barwidth, color = "deepskyblue", label = "Not Sure")
    plt.xticks(xpos, sexid)
    plt.title("Sexual Orientation vs. Weapon Threatens")
    plt.xlabel("Weapon Threatens (Times)")
    plt.ylabel("Answers")
    plt.legend()
    plt.show()

    # Zoomed in graphs
    
    print("\n Weapon Carriages vs. Weapon Threatens")
    print("-------------------------------------------\n")
    filt_q13_q16 = df[["q16", "q13"]].value_counts().sort_index(ascending = True)
    q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_q13_q16.iloc[:8]
    answer2 = filt_q13_q16.iloc[8:16]
    answer3 = filt_q13_q16.iloc[16:24]
    answer4 = filt_q13_q16.iloc[24:32]
    answer5 = filt_q13_q16.iloc[32:40]
    barwidth = .2
    xpos = np.arange(len(q16))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
    plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
    plt.ylim(0, 2000)
    plt.xticks(xpos, q16)
    plt.title("Weapon Carriages vs. Weapon Threatens")
    plt.xlabel("Weapon Threatens (Times)")
    plt.ylabel("Answers")
    plt.legend()
    plt.show()
    
    
    print("\n Gender vs. Weapon Carriages")
    print("-------------------------------------------\n")
    filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
    q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_sex_q16.iloc[:8]
    answer2 = filt_sex_q16.iloc[8:16]
    barwidth = .2
    xpos = np.arange(len(q16))
    plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
    plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
    plt.ylim(0, 2000)
    plt.xticks(xpos, q16)
    plt.title("Gender vs. Weapon Threatens")
    plt.xlabel("Times")
    plt.ylabel("Weapon Carriage answers")
    plt.legend()
    plt.show()
    
    
    print("\n Gender vs. Weapon Threantens")
    print("-------------------------------------------\n")
    filt_sex_q16 = df[["sex", "q16"]].value_counts().sort_index(ascending = True)
    q16 = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_sex_q16.iloc[:8]
    answer2 = filt_sex_q16.iloc[8:16]
    barwidth = .2
    xpos = np.arange(len(q16))
    plt.bar(xpos, answer1, barwidth, color = "violet", label = "Female")
    plt.bar(xpos + .2, answer2, barwidth, color = "dodgerblue", label = "Male")
    plt.ylim(0, 2000)
    plt.xticks(xpos, q16)
    plt.title("Gender vs. Weapon Threatens")
    plt.xlabel("Times")
    plt.ylabel("Weapon Carriage Answers")
    plt.legend()
    plt.show()
    
    
    print("\n Age vs. Weapon Carriages")
    print("-------------------------------------------\n")
    filt_age_q13 = df[["q13", "age"]].value_counts().sort_index(ascending = True)
    age = ["12", "13", "14", "15", "16", "17", "18+"]
    answer1 = filt_age_q13.iloc[:7]
    answer2 = filt_age_q13.iloc[7:14]
    answer3 = filt_age_q13.iloc[14:21]
    answer4 = filt_age_q13.iloc[21:28]
    answer5 = filt_age_q13.iloc[28:35]
    barwidth = .2
    xpos = np.arange(len(age))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
    plt.bar(xpos + .8, answer5, barwidth, color = "deepskyblue", label = "6+")
    plt.ylim(0, 1000)
    plt.xticks(xpos, age)
    plt.ylim(0, 5000)
    plt.title("Age vs. Weapon Carriage")
    plt.xlabel("Age")
    plt.ylabel("Weapon Carriage")
    plt.legend()
    plt.show()
    
    
    print("\n Age vs. Weapon Threatens")
    print("-------------------------------------------\n")
    barwidth = .4
    filt_age_q16 = df[["q16", "age"]].value_counts().sort_index(ascending = True)
    age = ["12", "13", "14", "15", "16", "17", "18+"]
    answer1 = filt_age_q16.iloc[:7]
    answer2 = filt_age_q16.iloc[7:14]
    answer3 = filt_age_q16.iloc[14:21]
    answer4 = filt_age_q16.iloc[21:28]
    answer5 = filt_age_q16.iloc[28:35]
    answer6 = filt_age_q16.iloc[35:42]
    answer7 = filt_age_q16.iloc[42:49]
    answer8 = filt_age_q16.iloc[49:56]
    barwidth = .125
    xpos = np.arange(len(age))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .125, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .25, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .375, answer4, barwidth, color = "cornflowerblue", label = "4-5")
    plt.bar(xpos + .5, answer5, barwidth, color = "deepskyblue", label = "6-7")
    plt.bar(xpos + .65, answer6, barwidth, color = "cyan", label = "8-9")
    plt.bar(xpos + .75, answer7, barwidth, color = "c", label = "10-11")
    plt.bar(xpos + .875, answer8, barwidth, color = "darkcyan", label = "12+")
    plt.ylim(0, 1000)
    plt.xticks(xpos, age)
    plt.title("Age vs. Threatens")
    plt.xlabel("Age")
    plt.ylabel("Weapon Threatens")
    plt.legend()
    plt.show()
    
    
    print("\n Sexual Orientation vs. Weapon Carriages")
    print("-------------------------------------------\n")
    filt_q13_sexid = df[["q13", "sexid"]].value_counts().sort_index(ascending = True)
    sexid = ["Heterosexual", "Gay/Lesbian", "Bisexual", "Not Sure"]
    answer1 = filt_q13_sexid.iloc[:4]
    answer2 = filt_q13_sexid.iloc[4:8]
    answer3 = filt_q13_sexid.iloc[8:12]
    answer4 = filt_q13_sexid.iloc[12:16]
    answer5 = filt_q13_sexid.iloc[16:20]
    barwidth = .2
    xpos = np.arange(len(sexid))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "0")
    plt.bar(xpos + .2, answer2, barwidth, color = "mediumblue", label = "1")
    plt.bar(xpos + .4, answer3, barwidth, color = "blue", label = "2-3")
    plt.bar(xpos + .6, answer4, barwidth, color = "dodgerblue", label = "4-5")
    plt.bar(xpos + .8, answer4, barwidth, color = "deepskyblue", label = "6+")
    plt.ylim(0,2000)
    plt.xticks(xpos, sexid)
    plt.title("Sexual Orientation vs. Weapon Carriages")
    plt.xlabel("Weapon Threatens (Times)")
    plt.ylabel("Answers")
    plt.legend()
    plt.show()
    
    
    print("\n Sexual Orientation vs. Weapon Threatens")
    print("-------------------------------------------\n")
    filt_q13_sexid = df[["sexid", "q16"]].value_counts().sort_index(ascending = True)
    sexid = ["0", "1", "2-3", "4-5", "6-7", "8-9", "10-11", "12+"]
    answer1 = filt_q13_sexid.iloc[:8]
    answer2 = filt_q13_sexid.iloc[8:16]
    answer3 = filt_q13_sexid.iloc[16:24]
    answer4 = filt_q13_sexid.iloc[24:32]
    barwidth = .25
    xpos = np.arange(len(sexid))
    plt.bar(xpos, answer1, barwidth, color = "midnightblue", label = "Heterosexual")
    plt.bar(xpos + .25, answer2, barwidth, color = "blue", label = "Gay or Lesbian")
    plt.bar(xpos + .5, answer3, barwidth, color = "dodgerblue", label = "Bisexual")
    plt.bar(xpos + .75, answer4, barwidth, color = "deepskyblue", label = "Not Sure")
    plt.ylim(0, 2000)
    plt.xticks(xpos, sexid)
    plt.title("Sexual Orientation vs. Weapon Threatens")
    plt.xlabel("Weapon Threatens (Times)")
    plt.ylabel("Answers")
    plt.legend()
    plt.show()

    # Box plots

    print("\n BMI vs. Weapon Carriage")
    print("-------------------------------------------\n")
    plt.title("BMI and Weapon Carriage")
    sns.boxplot(x = "q13", y = "BMI", data = df, palette="Blues")
    plt.ylim(0, 80)
    plt.show()


    print("\n BMI vs. Weapon Threatens")
    print("-------------------------------------------\n")
    plt.title("BMI and Weapon Threatens")
    sns.boxplot(x = "q16", y = "BMI", data = df, palette="Blues")
    plt.ylim(0, 80)
    plt.show()

    # Heatmap
    
    print("\nHeatmap")
    print("---------")
    corr = df.corr()
    sns.heatmap(corr, annot = True, cmap = "Blues")
    plt.show()

             

Main()



