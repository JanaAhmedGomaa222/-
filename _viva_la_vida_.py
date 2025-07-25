# -*- coding: utf-8 -*-
""""Viva La Vida"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18_Y9Ru3Y8eBjQ3O5ydYyS0jD3I165WWn
"""

def collect_data():  # Function to collect user data over several days
    while True:
        try:
            days = int(input("How many days do you want to track? "))
            if days <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")
    symptoms = []# Create empty lists to store data
    sleep = []
    stress = []
    for i in range(days):
        print("\nDay", i + 1)
        symptom = input("What symptom did you feel? (or 'none'): ")
        while True:# Get sleep hours
            try:
                sleep_hours = float(input("How many hours did you sleep? "))
                if sleep_hours < 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")
        while True:# Get stress level
            try:
                stress_level = int(input("Rate your stress (1 to 10): "))
                if stress_level < 1 or stress_level > 10:
                    print("Please enter a number between 1 and 10.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        symptoms.append(symptom)# Append valid data
        sleep.append(sleep_hours)
        stress.append(stress_level)
    return symptoms, sleep, stress  # Return the three lists
def analyze_data(symptoms, sleep, stress):  # Function to analyze the collected data
    total_sleep = sum(sleep)
    total_stress = sum(stress)
    avg_sleep = total_sleep / len(sleep)
    avg_stress = total_stress / len(stress)
    repeated_symptom = ""
    for s in symptoms:
        if symptoms.count(s) > 1 and s != "none":
            repeated_symptom = s
            break
    return avg_sleep, avg_stress, repeated_symptom
def give_advice(avg_sleep, avg_stress, repeated_symptom):
    print("\n___Health Report___")
    print("Average sleep:", avg_sleep, "hours")
    print("Average stress:", avg_stress)
    if avg_sleep < 6:
        print("Advice: Try to sleep more.")
    if avg_stress > 7:
        print("Advice: Your stress is high. Try relaxing activities.")
    if repeated_symptom != "":
        print("You had the symptom:", repeated_symptom, "more than once.")
        print("Advice: Consider seeing a doctor.")
    if avg_sleep >= 6 and avg_stress <= 7 and repeated_symptom == "":
        print("You are doing well! Keep it up!")
symptoms, sleep, stress = collect_data()# Run the full program
avg_sleep, avg_stress, repeated_symptom = analyze_data(symptoms, sleep, stress)
give_advice(avg_sleep, avg_stress, repeated_symptom)