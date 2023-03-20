# Week 4 — Postgres and RDS

## Homework Task Performed for Week 4

- **Install Postgres on Docker**
** **
```
 db:
    image: postgres:13-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - '5432:5432'
    volumes: 
      - db:/var/lib/postgresql/data   
```

- **Created RDS Instance for Postgres (Used Console not CLI as having connectivity issue)**
** **

![RDS](https://user-images.githubusercontent.com/125117631/226366083-45544e7d-7386-4a66-a0d7-b191e7b75876.png)

- **Checked RDS Instance connectivity via SQLectron and eventually stopped**
** **

![Db Connectivity test vis SQLectron](https://user-images.githubusercontent.com/125117631/226370288-63bc38cd-0e89-43dc-bcde-4e578a2d9abc.png)

- **Created Bash script for connecting, loading schema & populating data on Postgres for Dev and Prod**
** **

***Create Database Cruddur***
```
#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-create"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"


NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "create database cruddur;"
```

***Drop Database Cruddur***
```
#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-drop"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"


NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "drop database cruddur;"
```

***Automated Database Creation, Schema loading and Seeding***
```
#! /usr/bin/bash
set -e # stop if it fails at any point

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-setup"
printf "${CYAN}==== ${LABEL}${NO_COLOR}\n"

bin_path="$(realpath .)/bin"

source "$bin_path/db/drop"
source "$bin_path/db/create"
source "$bin_path/db/schema-load"
source "$bin_path/db/seed"
```

- **Created Lambda function that populates RDS, post Cognito user confirmation**
** **
![Lambda Cognito](https://user-images.githubusercontent.com/125117631/226369188-ab8f85d3-1b5b-4b63-8378-22fb56485720.png)

- **Posted messages on the app. Also confirmed that they are showing in on RDS**
** **
***Added messages on Cruddur***

![Cruddur](https://user-images.githubusercontent.com/125117631/226369527-aa262d63-bba4-4bf7-8269-bc47eade67e7.png)

***Verified RDS to see if posted message is available on Prod RDS***

```./bin/db-connect prod``` 

```SELECT * FROM activities;```

![Inside RDS](https://user-images.githubusercontent.com/125117631/226369557-b250993f-fb81-4911-b00e-f7eb610283b1.png)

