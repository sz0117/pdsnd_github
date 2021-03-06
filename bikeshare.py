import time
import pandas as pd

CITY_DATASETS = { 'chicago': 'chicago.csv',
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

    # get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city=input('Please enter the city whose data you want to explore. Choose: Chicago, New York, or Washington\n')
      cities=['chicago','new york','washington']
      if city.lower() not in cities:
             print("Please choose one of the three cities")
      else:
             city=city.lower()
             break
    print('You chose {}'.format(city.title()))

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("Choose a month you want to view: Jan, Feb, Mar, Apr, May, Jun or \"All\"\n")
        months=['jan','feb','mar','apr','may','jun','all']
        if month[:3].lower() not in months:
            print("Please Choose one of the valid months, or \"all\"")
        else:
            month=month[:3].lower()
            break
    print('You chose {}'.format(month.title()))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter the three letter expression for the day of the week:Mon, Tue, Wed , etc. ; or \"All\"\n")
        days=['mon','tue','wed','thu','fri','sat','sun','all']
        if day[:3].lower() not in days:
            print("Please choose a valid day, or \"all")
        else:
            day=days.index(day)
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATASETS[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    months=['all','jan','feb','mar','apr','may','jun']
    if month!='all':
        month=months.index(month)
        df=df[df['month']==month]

    if day !=7:
        df=df[df['day_of_week']==day]


    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month=df['month'].mode()
    print ("The Most Common Month")
    print(most_month)
    # display the most common day of week
    most_day=df['day_of_week'].mode()
    print ('The Most Common Weekday')
    print(most_day)

    # display the most common start hour
    most_start_hour=df['hour'].mode()
    print('The Most Common Hour')
    print(most_start_hour)

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station: {}'.format(pop_start_station))

    # display most commonly used end station
    pop_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station: {}'.format(pop_end_station))



    # display most frequent combination of start station and end station trip

    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]

    print("The most commonly used start station and end station : {}, {}"\

            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tot_travel_time=df['Trip Duration'].sum()
    print("Total Travel Time is: {}".format(tot_travel_time))
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df.groupby(['User Type']).sum()
    print('User Types\n',user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print("Gender Counts")
        print(gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_year=df['Birth Year'].max()
        late_year=df['Birth Year'].min()
        common_year=df['Birth Year'].mode()
        print('The earliest birth year is: {}'.format(early_year))
        print('The most recent birth year is: {}'.format(late_year))
        print('The most common birth year is: {}'.format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    def display(df):
        """
        Allow raw data to be desplayed upon request by user. \Prompt the user \if they want to see five lines of raw data,
        display that data \if the answer is \'yes\', and \continue these prompts and displays until the user says \'no\'.
        """
    a = 0
    b = 5
    disp = input("Would you like to view the first 5 rows of data? Enter \"Yes\" or \"No\"\n")
    while True:
        if disp.lower() == 'no':
            break
        if disp.lower() == 'yes':
            print(df.iloc[a:b])
        disp = input("Would you like to view the first 5 rows of data? Enter \"Yes\" or \"No\"\n").lower()
        a += 5
        b += 5

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
