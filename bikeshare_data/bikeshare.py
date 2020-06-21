import time
import calendar
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
    while True:
        city = str(input("Select City: chicago, new york city, or washington  "))
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Please input a city name that is listed.")
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Select Month: january, february, march, april, may, or june  "))
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            print("Please input a month that is listed.")
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Select Day: monday, tuesday, wednesday, thursday, friday, or all  "))
        day = day.lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all'):
            print("Please input a day of the week that is listed.")
        else:
            break

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
        df        - Pandas DataFrame containing city data filtered by month an   """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    df['start_time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['start_time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The most popular month:  ", calendar.month_name[popular_month])

    # TO DO: display the most common day of week
    df['day'] = df['start_time'].dt.day
    popular_day = df['day'].mode()[0]
    print("The most popular day:  ", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['start_time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour:  ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("The most popular start station:  ", popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("The most popular end station:  ", popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_path = df.groupby(['Start Station','End Station']).size()
    print("The most popular train path:  ", popular_path.nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time in mins:  ", total_time)

    # TO DO: display mean travel time
    count_row = df.shape[0]
    mean_travel = (total_time / count_row)
    print("The average travel time in mins:  ", int(round(mean_travel)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = (df['User Type'].value_counts())
    print("The total per user type:  ", user_types)

    # TO DO: Display counts of gender
    # Check if gender column is in dataset
    if 'Gender' in df:
        gender = (df['Gender'].value_counts())
        print("The total per gender:  ", gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    # Check if birth year column is in dataset
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        earliest_year = int(earliest_year)
        recent_year = df['Birth Year'].max()
        recent_year = int(recent_year)
        common_year = df['Birth Year'].mode()
        common_year = int(common_year)
        print("The earliest birth year:  ", earliest_year)
        print("The most recent birth year:  ", recent_year)
        print("The most common birth year:  ", common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    raw_data = str(input("Would you like to see raw data?  "))
    raw_data = raw_data.lower()
    index = 0
    while raw_data == 'yes':
        print(df.iloc[(index):(index+5)])
        index = index + 5
        raw_data = str(input("Would you like to see more raw data?  "))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

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
