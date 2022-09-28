import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            while True:
                city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower().strip()
                if city in CITY_DATA:
                    break
                else:
                    print("That's not a valid input.")
            
            while True:
                filter_bool = input('\nWould you like to filter the data by month, day, both or not at all? Type "none" for no time filter\n').lower().strip()
                if filter_bool == "none":
                    month = "all"
                    day = "all"
                    break
                elif filter_bool == "month":
                    month = input('\nWhich month - January, February, March, April, May, or June?\n').lower().strip()
                    day = "all"
                    break
                elif filter_bool == "day":
                    month = "all"
                    day = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower().strip()
                    break
                elif filter_bool == "both":
                    month = input('\nWhich month - January, February, March, April, May, or June?\n').lower().strip()
                    day = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower().strip()
                    break
                else:
                    print("That's not a valid input")
            break
        
        except KeyboardInterrupt:
            print("That's not a valid input.")
   
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
    mode_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    mode_dw = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mode_hour = df['hour'].mode()[0]
    
    print("\nThe most common month is {}.\nThe most common day of week is {}.\nThe most common start hour is {}.".format(mode_month,mode_dw,mode_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station']+df['End Station']
    mode_station_combination = df['Station Combination'].mode()[0]

    print("\nThe most commonly used start station is {}.\nThe most commonly used end station is {}.\nThe most frequent combination of start station and end station is {}.".format(mode_start_station,mode_end_station,mode_station_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    
    print("\nThe total travel time is {}.\nThe mean travel time is {}.".format(total_time,mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(user_type)
    if city != 'washington':
        
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        latest_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()[0]

        print("\nThe earliest year of birth is {}.\nThe most recent year of birth is {}.\nThe most common year of birth is{}".format(earliest_year_of_birth, latest_year_of_birth, most_common_year_of_birth))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        df2 = pd.read_csv(CITY_DATA[city])
        front = 0
        end = 5
        length = len(df2)
        while True:
            raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            
            if raw_data.lower().strip() == 'yes':
                print(df2.head(5))
                for i in range(front,end):
                    df2 = df2.drop(i)
                front += 5
                end += 5
            elif raw_data.lower().strip() == 'no' or end >length:
                break
            else:
                print("That's not a valid input")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() = 'no':
            break
        elif restart.lower() != "no" or restart.lower() != "yes":
            print("That's not a valid input.")


if __name__ == "__main__":
	main()
