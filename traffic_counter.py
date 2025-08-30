import pandas as pd

class TrafficCounter:
    def __init__(self, traffic_data):
        self.df = self.read_file(traffic_data)

    def read_file(self, traffic_data):
        '''Reads the traffic data from a file and returns a DataFrame.'''
        df = pd.read_csv(
            traffic_data,
            sep=" ",
            names=["timestamp", "traffic_count"],
            parse_dates=["timestamp"]
        )
        df = df.sort_values(by="timestamp").reset_index(drop=True)
        return df
    

    def total_traffic_count(self):
        '''Returns the total traffic count of all rows in the DataFrame.'''
        return self.df['traffic_count'].sum()

    def daily_traffic_count(self):
        '''Returns the daily traffic count Grouped by timestamps in the DataFrame.'''
        return self.df.groupby(self.df['timestamp'].dt.date)['traffic_count'].sum()

    def top_half_hours(self, n=3):
        '''Returns the top n half-hour periods with the most traffic.'''
        return self.df.nlargest(n, 'traffic_count')
    
    def least_ninety_min_window(self):
        '''Returns the least seen traffic count and the corresponding timestamps in a 1.5 hour window.'''
        roll_sum = self.df["traffic_count"].rolling(3).sum()
        contiguous = (
            self.df["timestamp"].diff().eq("30min") &
            self.df["timestamp"].diff(2).eq("60min")
        )
        contiguous_df = roll_sum.where(contiguous)
        if contiguous_df.empty:
            return None, None

        # Finds the value of the lowest sum in contiguous df
        min_index = contiguous_df.idxmin()
        min_sum = int(contiguous_df.loc[min_index])

        # Finds the rows that make up the lowest sum in contiguous df
        pos = self.df.index.get_loc(min_index)
        min_window = self.df.iloc[pos-2:pos+1, [0, 1]]

        return min_sum, min_window
    
    def display_stats(self):
        '''Displays the traffic statistics.'''
        print('\n--------------------')
        print(f"Total Cars: {self.total_traffic_count()}")
        
        print("Total Cars per Day:")
        for day, count in self.daily_traffic_count().items():
            print(f"  {day} {count}")
        
        print("Top 3 half hours with most cars:")
        for _, row in self.top_half_hours(n=3).iterrows():
            print(f"  {row['timestamp'].isoformat()} {row['traffic_count']}")

        min_sum, min_window = self.least_ninety_min_window()
        if min_window is None:
            print("Least seen in a 1.5 hour period: N/A")
        else:
            print(f"Least seen in a 1.5 hour period: {int(min_sum)}")
            for _, row in min_window.iterrows():
                print(f"  {row['timestamp'].isoformat()} {row['traffic_count']}")
        print('--------------------\n')