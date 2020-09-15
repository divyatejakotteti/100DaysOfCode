'''Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 

Input Format::

	A single string that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ).
'''

time=input().strip()
hh,mm,ss=map(int,time[:-2].split(':'))
hh=hh% 12 +(time[-2:]=='PM')*12
print('%02d:%02d:%02d')%(hh,mm,ss)