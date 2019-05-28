#set datafile separator "\t"

plot "meanE.dat" using 1 with points title 'Torque',\
    "meanE.dat" using 2 with points title 'Average Langevin'
set yrange[-10:10]
#set logscale xy
pause 1
reread
