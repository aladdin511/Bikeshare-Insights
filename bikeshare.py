import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITY_LIST = ['chicago', 'new york', 'washington'] #Specifies list of cities for user prompt

MONTHS_LIST = ['january', 'february', 'march', 'april', 'may', 'june','all'] #Specifies list of months for user prompt

DAYS_LIST = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'] #Specifies list of days for user prompt

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
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York, or Washington?\n')
            if city.lower() in CITY_LIST:
                break
        except:
            Print('Invalid Input')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Would you like to filter the data by month? Type the month name or type "all" for no time filter.\n')
            if month.isalpha() and month.lower() in MONTHS_LIST:
                break
        except:
            print('Invalid Input!')
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Would you like to filter the data by day? Type the day name or type "all" for no time filter.\n')
            if day.isalpha() and day.lower() in DAYS_LIST:
                break
        except:
            print('Invalid Input!')
    

    print('-'*40)
    return city, month, day

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    #Loads specified city file.
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    
    #Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Convert End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #Extract Month and Day to new cloumn
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    #Filter by month
    if month != 'all':
        month = MONTHS_LIST.index(month)+1
        
        df = df.loc[df['month'] == month]
    
    #Filter by day
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month: {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour of the week: {}'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular station: {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    
    #Grouping start station and end station column and sorting them
    combination = df.groupby(['Start Station','End Station']).size().sort_values()
    #Printing the last tuple of 'combination' by indexing (index -1 most frequent combination)
    print('The most frequent combination of start and end station: {}'.format(combination.index[-1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #Make new 'Travel Time' column by subtracting start time from end time
    df['Total Time'] = df['End Time'] - df['Start Time'] #'Start Time' and 'End Time' are converted to datetime in the load_data function
    total_travel_time = df['Total Time'].sum()
    print('Total travel time: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Total Time'].mean()
    print('Mean travel time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Counts of user types:\n{}\n'.format(user_types_count))

    # TO DO: Display counts of gender
    genders_count = df['Gender'].value_counts()
    print('Counts of genders:\n{}\n'.format(genders_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common_year = df['Birth Year'].mode()[0]
    print("Earliest year of birth: {}".format(earliest))
    print("Most recent year of birth: {}".format(most_recent))
    print("Most common year of birth: {}".format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
