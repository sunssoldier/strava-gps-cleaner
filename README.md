# strava-gps-cleaner
remove outliers from your strava rides

## Inspiration
Rides with GPS noise as shown below, which distort ride statistics significantly, including segments.
![alt text](https://github.com/sunssoldier/strava-gps-cleaner/blob/master/inspiration.jpg)

## Solution
Using DBSCAN algorithm given a couple of Hyperparameters (epsilon [distance between data points], minimum cluster size), we are able to cluster all of the data points near each other. Data is recorded at a relatively high frequency and hence close proximity, given bicycle speeds. Outlier data points are far away from the stream of good data points, and are classified either as noise, or other small clusters, by the algorithm. The hyperparameter tuning will be improved, however just running the algorithm with nominal values easily filters out the outliers. 

## Results
Actual raw path recorded by phone GPS is in red, while the corrected path (outliers filtered out) in blue. This will correct some of the ride statistics such as ride length, top speed, average speed, power calculations and calories burnt.
![alt text](https://github.com/sunssoldier/strava-gps-cleaner/blob/master/strava_outliers_filtered.png)
