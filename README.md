# adjust_test

 - for searching metrics occurred before or after exact date, or occurred in 
 exact period of time, add date_to, date_from or both respectively, e.g.:
    ```bash
   &date_to=2017-06-06
   ```
   or
   ```bash
   &date_from=2017-06-06
   ```
   or
   ```bash
   &date_from=2017-05-31&date_to=2017-06-15
   ```
 - for searching exact channel, country or operating system add one or few parameters with value which 
 you are looking for, e.g.:
   ```bash
   &country=GB&os=android&channel=chartboost
   ```
 - for grouping one or more columns group_by with one or few parameters: date, channel, country, os, e.g.:
   ```bash
   &group_by=date,country,os
   ```
 - for sorting by any column in ascending order add parameter ordering with required column.
 For sorting by any column in descending order just add "-" before column name, e.g.:
    ```bash
   &ordering=-date
   ```

## Fill up db with data.
1. Download test dump to project.
2. Login to db:
```
psql -h 127.0.0.1 -p 54322 -U metrics_user metrics_db
```
3. Upload test dump to db:
```
COPY public.api_metric (date,channel,country,os,impressions,clicks,installs,spend,revenue) FROM '/tmp/dataset.csv' DELIMITER ',' CSV HEADER;
```