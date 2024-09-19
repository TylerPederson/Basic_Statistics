import math
import random


def main():
    random.seed()
    menu()
    print("Exiting Program")

def menu():
    while(True):
        data = []
        print("----------------------")
        print("1) Input data directly")
        print("q) quit")
        response = input()
        if response == "q" or response == "quit":
            exit()
        if response == "1":
            data = read_in_data()
        else:
            print(f"Unrecognized Input: {response}")
            continue
        report_data(data)



def compute_variance(data):
    expected_mean = compute_expected(data)
    variance = 0 
    for datum in data:
        variance += ((datum[0] - expected_mean) ** 2 ) * datum[1]
    return round(variance, 4)

def compute_expected(data):
    weighted_sum = 0
    for datum in data:
        weighted_sum += (datum[0] * datum[1])
    return round(weighted_sum, 4)

def compute_standard_dev(data):
    return round(math.sqrt(compute_variance(data)), 4)


def read_in_data():
    my_data = []
    print("Enter a value and probability")
    while(True):
        value = float(input("Value: "))
        prob = float(input("Probalbility: "))
        my_data.append((value, prob))
        
        answer = input("Would you like to enter another data point: ")
        answer = answer.lower()
        if answer == 'n' or answer == "no":
            return my_data

def report_data(data):
    print(f"Data: {data}")
    print(f"Expected Average: {compute_expected(data)}")
    print(f"Variance: {compute_variance(data)}")
    print(f"Standard Deviations: {compute_standard_dev(data)}")
    

main()