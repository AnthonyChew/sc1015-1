import pandas as pd

# list of all csv filenames
# TAKE NOTE: 2015-2016 & 2017 have an extra column "remaining_lease"
csv_name_list = ["resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv",
                 "resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv",
                 "resale-flat-prices-based-on-approval-date-1990-1999.csv",
                 "resale-flat-prices-based-on-approval-date-2000-feb-2012.csv",
                 "resale-flat-prices-based-on-registration-date-from-mar-2012-to-dec-2014.csv"]

# convert all csv files to dataframes and store into array
csv_df_list = [pd.read_csv(i) for i in csv_name_list]

# combine dataframes without indexing
hdb = pd.concat(csv_df_list, ignore_index=True)

# 826581 data entries
# 117527 "remaining_lease" data entries
print(hdb.info())

# save clean data frame to hdb.csv
hdb.to_csv("hdb.csv")
