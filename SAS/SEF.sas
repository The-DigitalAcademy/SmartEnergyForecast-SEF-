/*Importing the dataset*/
proc import OUT = sef 
FILE ='/home/u62791206/SEF/myupdateddata.csv '
DBMS = CSV
REPLACE;
run;

/*Printing the dataset*/
 title 'Smart Energy Forecast';
proc print data = sef (obs=20);
run;
proc means;
run;
proc sgplot data=WORK.SEF;
	title height=14pt "Total PV Installed Capacity";
	vbar 'PV Installed Capacity'n / fillattrs=(color=CX00099b) datalabel 
		stat=percent;
	xaxis discreteorder=data reverse valuesrotate=diagonal;
	yaxis grid;
run;
proc sgplot data=WORK.SEF;
	title height=14pt "Total wind capacity installed";
	vbar 'Wind Installed Capacity'n / fillattrs=(color=CX000898) datalabel;
	yaxis grid;
run;
proc sgplot data=WORK.SEF;
	title height=17pt "Total CSP  capacity installed";
	vbar 'CSP Installed Capacity'n / fillattrs=(color=CX000898) datalabel 
		stat=percent;
	yaxis grid;
run;
proc sgplot data=WORK.SEF;
	title height=17pt "Total capacity installed";
	hbar 'Installed Eskom Capacity'n / fillattrs=(color=CX000898) datalabel 
		stat=percent;
	xaxis grid;
run;
proc sgplot data=WORK.SEF;
	title height=17pt "Total  Renewable Energy installed";
	vbar 'Total RE Installed Capacity'n / fillattrs=(color=CX009500) datalabel 
		stat=percent;
	xaxis discreteorder=data reverse;
	yaxis grid;
run;
proc sgplot data=WORK.SEF;
	title height=17pt "Total Other Renewable Energy installed";
	hbar 'Other RE Installed Capacity'n / fillattrs=(color=CX009500) datalabel 
		stat=percent;
	xaxis grid;
run;







