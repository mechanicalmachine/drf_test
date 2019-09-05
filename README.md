# adjust_test

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