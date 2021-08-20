#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:10:46 2021

@author: frank
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''

    while city not in CITY_DATA.keys():
        print('\nPlease enter your city: ')
        city = input().lower()

        if city not in CITY_DATA.keys():
            print('\nPlease enter a valid city (Chicago, New York City, Washington)')
    print(f"\nYou have chosen {} as your city.".format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA:
        print('\nPlease enter the month between January and June or All for seeing the data for all months:')
        month = input().lower()

        if month not in MONTH_DATA:
            print('\nInvalid input! Please enter again a valid month you can see above.')
    print(f"\nYou have chosen {} as your month.".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print('\nPlease enter a day in the week or all:')
        day = input().lower()
        if day not in DAY_LIST:
            print('\nInvalid input! Please enter a day in the week again.')
    print(f"\nYou have chosen {} as your day.".format(day.title()))

    print('\nYou have chosen {} as your city, {} as your month and {} as your day! Congratulation.'.format(city.title(),month.title(),day.title()))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('\nThe most popular month is {}'.format(popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day of week is {}'.format(popular_day))
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\The most popular hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common Start Station is {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common End Station is {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End Station'] = df['Start Station'] + ' to ' + df['End Station']
    start_to_end_station = df['Start To End Station'].mode()[0]
    print('\nThe most frequent combination of start station and end station for a trip is {}'.format(start_to_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Calculate the total trip duration with sum method
    total_duration = df['Trip Duration'].sum()
    # Calculate the total trip duration in minutes and seconds format
    minute, second = divmod(total_duration,60)
    # Calculate the total trip duration in hours and minutes format
    hour, minute = divmod(minute, 60)
    print('\nThe total drip duration is {} hours, {} minutes and {} seconds.'.format(hour,minute,second))

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    # Calculate the mean travel time in minutes and seconds format
    mins, secs = divmod(average_duration, 60)
    # Filter calculates the time in hours, mins, secs format if the mins are higher than 60 and prints the result
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print('\nThe average trip duration is {} hours, {} minutes and {} seconds.'.format(hrs,mins,secs))
    else:
        print('\nThe average trip duration is {} minutes and {} seconds.'.format(mins,secs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nDisplay counts of user types:\n{}'.format(user_type))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nThe gender types of users:\n{}'.format(gender))
    except:
        print('\nThere is no Gender column given in this file.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_by = int(df['Birth Year'].min())
        recent_by = int(df['Birth Year'].max())
        common_by = int(df['Birth Year'].mode()[0])
        print('\nThe earliest year of birth: {}\nThe most recent year of birth: {}\nThe most common year of birth: {}'.format(earliest_by,recent_by,common_by))
    except:
        print('\nThere is no data towards the birth year available in this file.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    response = ['yes', 'no']
    while True:
        choice = input('\nWould you like to view your individual trip data based on your input? (First five results) Please type "Yes" or "No"').lower()
        if choice in response:
            if choice == 'yes':
                start = 0
                end = 5
                data = df.iloc[start:end, :9]
                print(data)
            break
        else:
            print('\nYour answer was no or you choose an invalid input!')

    if choice == 'yes':
        while True:
            choice_2 = input('\nWould you like to view more trip data? Type "yes" or "no".')
            if choice_2 in response:
                if choice_2 == 'yes':
                    start += 5
                    end += 5
                    data = df.iloc[start:end, :9]
                    print(data)
                else:
                    break
            else:
                print('\nPlease enter a valid response!')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
