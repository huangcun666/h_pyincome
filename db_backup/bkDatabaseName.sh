#!/bin/bash

python /home/domizzi/db_backup/input_c.py

python /home/domizzi/db_backup/input_kf_gs.py

mysqldump -uroot -pdeng db_income2 > /home/domizzi/db_backup/db_income2_$(date +%Y%m%d_%H%M%S).sql
mysqldump -uroot -pdeng db_customer > /home/domizzi/db_backup/db_customer_$(date +%Y%m%d_%H%M%S).sql
