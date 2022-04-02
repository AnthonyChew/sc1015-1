# SC1015 DSAI Mini-Project
Eddy, Bryan & Yue Zhong

## EDA
### 1. Time Series & Lease Remaining (Eddy)
- To be Updated

### 2. Location & Block No. (Bryan)
<ins>Location</ins>
- Need to breakdown by flat type if not its not a good representation of the town price median
- Most Data for 3-5 Room Flat (will be focusing on this)
- Moderate Data for Executive Flat
- Very Little for 1-2 Room Flat

<ins>Flat Type Counts</ins>
```
4 ROOM              309314
3 ROOM              272580
5 ROOM              170408
EXECUTIVE            62641
2 ROOM                9863
1 ROOM                1273
MULTI GENERATION       279
MULTI-GENERATION       223
```

<ins>3 Room Top 3 Highest</ins>
```
PUNGGOL              358000.0
SENGKANG             340000.0
SEMBAWANG            290000.0
```

<ins>3 Room Top 3 Lowest</ins>
```
LIM CHU KANG          64250.0
JURONG WEST          145000.0
WOODLANDS            151000.0
```

<ins>4 Room Top 3 Highest</ins>
```
QUEENSTOWN           450000.0
PUNGGOL              440000.0
SENGKANG             383000.0
```

<ins>4 Room Top 3 Lowest</ins>
```
LIM CHU KANG          47100.0
YISHUN               231000.0
WOODLANDS            238000.0
```

<ins>5 Room Top 3 Highest</ins>
```
CENTRAL AREA         800000.0
QUEENSTOWN           526000.0
BUKIT MERAH          500000.0
```

<ins>5 Room Top 3 Lowest</ins>
```
WOODLANDS            320000.0
YISHUN               333800.0
JURONG EAST          340000.0
```

<ins>Block No.</ins>
- Hard to track
- Added hbd_raw.csv to single out the blocks (testing)

### 3. Flat Type, Floor Area & Flat Model (Yue Zhong)
- To be Updated

## Version History
> Version Format: v*MAJOR*.*MINOR*.*PATCH*

### v0.0.0 Clean Data (2022/03/06)
- Combined all csv files into `hdb.csv`
- `2015 to 2016` & `2017` csv files have an extra column `remaining_lease`
- `hdb.csv` 826581 data entries

### v0.0.1 README Hotfix (2022/03/06)
- Fixed markdown headings issue

### v0.0.2 Clean Data Drop Columns (2022/03/07)
- Dropped `remaining_lease`, `street_name`, `storey_range` columns

### v0.0.3 README Update (2022/03/07)
- Added EDA
- Fixed typo

### v0.1.0 README Update (2022/03/27)
- Added Time Series EDA
- flat_type breakdown
- 3-5 Room Cluster
- 3-5 Room Median
- Testing Playground (To be removed)

### v0.1.1 Clean Data Update (2022/03/31)
- Added `remaining_lease` missing data
> `remaining_lease` = (`lease_commence_date` + 99) - `year`
- Removed `hdb_raw.csv` (for testing only)
- Added `year` and `month`
- Restored `street_name` and `storey_range` (for unit tracking)

### v0.2.0 ARIMA (2022/04/02)
- Added `ARIMA` model
- Best blk `Jurong 211 (3 ROOM)`
- Added fill missing data sequence 
- Added `auto_arima` params (failed)
- Added `LSTM` model (failed)