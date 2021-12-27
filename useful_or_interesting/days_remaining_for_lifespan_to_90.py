#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total_days_in_90_years   = 90 * 365
total_weeks_in_90_years  = 90 * 52
total_months_in_90_years = 90 * 12

int_age = int(age)

input_age_in_days   = int_age * 365
input_age_in_weeks  = int_age * 52
input_age_in_months = int_age * 12

days_remaining   = total_days_in_90_years - input_age_in_days
weeks_remaining  = total_weeks_in_90_years - input_age_in_weeks
months_remaining = total_months_in_90_years - input_age_in_months

print(f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.')
