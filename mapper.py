#!/usr/bin/env python

import sys
import csv

for line in sys.stdin:
 bad,loan,mortgage_due,value,reason,job,job_years,deg_reports,delinq,cred_line_age,recent_inquiries,credit_lines,debt_income = line.split(",")

 if int(bad) == 1:
  if str(reason) == "NULL" or reason == None:
	  print("Unknown" + "\t" + "1")
  else:
    print(str(reason) + "\t" + "1")
