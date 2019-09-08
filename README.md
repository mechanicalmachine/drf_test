# adjust_test

To retrieve required data use url ```http://hostname:port/api/metrics/?``` with following bellow parameters.
Use '&' sign between parameters if you need to use some of them.
 - for searching metrics occurred before or after exact date, or occurred in 
 exact period of time, add date_to, date_from or both respectively, e.g.:
    ```bash
   date_to=2017-06-06
   ```
   or
   ```bash
   date_from=2017-06-06
   ```
   or
   ```bash
   date_from=2017-05-31&date_to=2017-06-15
   ```
 - for searching exact channel, country or operating system add one or few parameters with value which 
 you are looking for, e.g.:
   ```bash
   country=GB&os=android&channel=chartboost
   ```
 - for grouping one or more columns group_by with one or few parameters: date, channel, country, os, e.g.:
   ```bash
   group_by=date,country,os
   ```
 - for sorting by any column in ascending order add parameter ordering with required column.
 For sorting by any column in descending order just add "-" before column name, e.g.:
    ```bash
   ordering=-date
   ```
 - for showing only required fields add 'show' parameter with field name you need, e.g.:
    ```bash
   show=impressions_sum,clicks_sum
   ```

## Examples of common API use cases:
1. Show the number of impressions and clicks that occurred before the 1st of June 2017,
 broken down by channel and country, sorted by clicks in descending order. Hint:
    ```bash
    http://127.0.0.1:8000/api/metrics/?group_by=channel,country&show=impressions_sum,clicks_sum&ordering=-clicks_sum&date_to=2017-06-01
    ```
2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, 
sorted by date in ascending order.
    ```
    http://127.0.0.1:8000/api/metrics/?group_by=date&date_from=2017-05-01&date_to=2017-05-31&os=ios&ordering=-date&show=installs_sum
    ```
   
3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by 
revenue in descending order.
    ```bash
    http://127.0.0.1:8000/api/metrics/?group_by=os&date_from=2017-06-01&date_to=2017-06-01&show=revenue_sum&country=US&ordering=-revenue_sum
    ```

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
    ```bash
    http://127.0.0.1:8000/api/metrics/?group_by=channel&show=cpi,spend_sum&ordering=-cpi&country=CA
    ```
      
## Fill up db with data.
1. Download test dump to project dir.
2. Login to db:
```
psql -h 127.0.0.1 -p 54322 -U metrics_user metrics_db
```
3. Upload test dump to db:
```
COPY public.api_metric (date,channel,country,os,impressions,clicks,installs,spend,revenue) FROM '/tmp/dataset.csv' DELIMITER ',' CSV HEADER;
```
