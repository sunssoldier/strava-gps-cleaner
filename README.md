# strava-gps-cleaner
remove outliers from your strava rides

## Inspiration
Rides with GPS noise as shown below, which distort ride statistics significantly, including segments.
![alt text](https://github.com/sunssoldier/strava-gps-cleaner/blob/master/inspiration.jpg)

## Solution
Using DBSCAN algorithm given a couple of Hyperparameters (epsilon, minimum cluster size), we are able to cluster all of the data points near to each other. Data is recorded at a relatively high frequency and hence close proximity. Outlier data points are far away from the stream of good data points, and are classified eaither as noise, or other small clusters, by the algorithm. The hyperparameter tuning could be improved, however just running the algorithm with nominal values easily filters out the outliers. 

## Results
Actual raw path recorded by phone GPS is in red, while the corrected path (outliers filtered out) in in blue.
![alt text](https://github.com/sunssoldier/strava-gps-cleaner/blob/master/strava_outliers_filtered.png)
