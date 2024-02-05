#!/bin/bash

sleep 10

/opt/mssql-tools/bin/sqlcmd -S sqlserver -U sa -P ${SQL_SERVER_PASS} -d master -i /tmp/create_tables.sql
/opt/mssql-tools/bin/sqlcmd -S sqlserver -U sa -P ${SQL_SERVER_PASS} -d master -i /tmp/seed.sql