
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



/* Create the graph */
proc sgplot data=WORK.SEF;
  title "Residual Forecast Over Time";
  xaxis label="Residual Demand";
  yaxis label="Residual Forecast";
  series x='Residual Demand'n y='Residual Forecast'n / markers;
run;


proc sgplot data=WORK.SEF;
  title "Monthly Planned and Unplanned Power Cuts";
  yaxis label="Total Cuts";
  xaxis label="Month" display=(nolabel);
  series x='Date Time Hour Beginning'n y="Total OCLF"n / markers legendlabel="Total OCLF";
  series x='Date Time Hour Beginning'n y="Total PCLF"n / markers legendlabel="Total PCLF";
  series x='Date Time Hour Beginning'n y="Total UCLF"n / markers legendlabel="Total UCLF";
run;

proc sgplot data=WORK.SEF;
  title "Monthly Demand";
  yaxis label="Demand";
  xaxis label="Month" display=(nolabel);
  series x='Date Time Hour Beginning'n y="Manual Load_Reduction(MLR)"n / markers legendlabel="Manual Load Reduction";
  series x='Date Time Hour Beginning'n y="ILS Usage"n / markers legendlabel="ILS Usage";
  series x='Date Time Hour Beginning'n y="IOS Excl ILS and MLR"n / markers legendlabel="IOS Excl ILS and MLR";
run;


proc sgplot data=work.sef;
   title "Monthly power generated per station ";
   yaxis label="Demand";
   xaxis label="Month" display=(nolabel);
   series x='Date Time Hour Beginning'n y='Palmiet Gen Unit Hours'n / markers legendlabel="Palmiet Gen Unit Hours";
   series x='Date Time Hour Beginning'n y='Ingula Gen Unit Hours'n / markers legendlabel="Ingula Gen Unit Hours";
   series x='Date Time Hour Beginning'n y='Drakensberg Gen Unit Hours'n / markers legendlabel="Drakensberg Gen Unit Hours";
   
run;

proc sgplot data=work.sef;
   title "Hourly Contracted PV";
   yaxis label="Time";
   xaxis label="PV";
   series y='Date Time Hour Beginning'n x='PV'n / markers legendlabel='PV';
  
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








