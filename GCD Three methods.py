#Program to generate random numbers and find 
#their GCD using three different algorithms,
#with their results and statistics stored 
#in the form of a excel sheet.
#
###########################


import random
import timeit
import xlsxwriter
import numpy as np
import xlrd
import subprocess

mylist = []
mylist2 = []
mylist3 = []

# Creating the required workbooks and adding worksheets for each of them
workbook1 = xlsxwriter.Workbook('Original_Euclid_Results.xlsx')
worksheet1 = workbook1.add_worksheet()

workbook2 = xlsxwriter.Workbook('Second_Euclid_Results.xlsx')
worksheet2 = workbook2.add_worksheet()

workbook3 = xlsxwriter.Workbook('Brute_Force_Results.xlsx')
worksheet3 = workbook3.add_worksheet()

workbook4 = xlsxwriter.Workbook('Original_Euclid_Statistics.xlsx')
worksheet4 = workbook4.add_worksheet()

workbook5 = xlsxwriter.Workbook('Second_Euclid_Statistics.xlsx')
worksheet5 = workbook5.add_worksheet()

workbook6 = xlsxwriter.Workbook('Brute_Force_Statistics.xlsx')
worksheet6 = workbook6.add_worksheet()


# Implementation of Original Euclid Alogorithm for computing the GCD
def gcd(a,b):
  remainder  = 1
  while(0 != remainder):
    quotient = a//b
    remainder = a - quotient * b
    a = b
    b = remainder
  return a

# Implementation of the Second Euclid Algorithm to calculate the GCD
def gcd2(a,b):
  remainder = 1
  while(0 != remainder):
    remainder = a - b
    if (remainder > b):
      remainder = remainder - b
      if (remainder > b):
        remainder = remainder - b
        if (remainder > b):
          remainder = a - b * (a//b) 
    a = b
    b = remainder
  return a 

# Implementation of the Brute Force Algorithm to compute the GCD
def gcd_bruteforce(a,b):
  
  i = b
  while (i > 0):
    if(a % i != 0) or (b % i != 0):
      i = i - 1
    else:  
      return i
 
# The following will give the headings that are to be present in 
# the excel sheet that captures the randomly generated pairs of 
# numbers, their GCD and the total time taken to calculate.  
  
row = 0
col = 0
worksheet1.write(row, col, 'Number One')
worksheet1.write(row, col + 1 , 'Number Two')
worksheet1.write(row,col+2, 'Their GCD ')
worksheet1.write(row, col+3, 'Time Spent(Microseconds)')

worksheet2.write(row, col, 'Number One')
worksheet2.write(row, col + 1 , 'Number Two')
worksheet2.write(row,col+2, 'Their GCD ')
worksheet2.write(row, col+3, 'Time Spent(Microseconds)')

worksheet3.write(row, col, 'Number One')
worksheet3.write(row, col + 1 , 'Number Two')
worksheet3.write(row,col+2, 'Their GCD')
worksheet3.write(row, col+3, 'Time Spent(Microseconds)')


# the following is a for loop that iterates for 100 times 
# each time generating a pair of random numbers and calculating 
# the GCD by calling each of the three algorithms.

row = row + 1
for i in range (100):  
  a = random.randint(1,100)
  
  b = random.randint(1,100)
# Calculating the current time   
  start = timeit.default_timer()
# GCD using Original Euclid Algorithm
  result = gcd(a,b)
  print ('GCD of {} and {} is: {}'.format(a,b,result))
# Time elapsed for the first algorithm
  time_elapsed = timeit.default_timer() - start
  print ('Time taken in Euclid: ', time_elapsed)
  mylist.append(time_elapsed)
# Writing the results to an excel sheet
  worksheet1.write(row, col, a)
  worksheet1.write(row, col + 1 , b)
  worksheet1.write(row,col+2, result)
  worksheet1.write(row, col+3, time_elapsed)
# Following the prerequisite for brute for algorithm and 
# second euclid algorithm that a should be greater than b   
  if (b > a):
    temp = a
    a = b
    b = temp
  start = timeit.default_timer()
# GCD using Second Euclid Algorithm  
  result = gcd2(a,b)
  #print ('gcd using euclid improved :',result) 
  time_elapsed =   timeit.default_timer() - start
  print ('time taken for euclid improved: ',time_elapsed ) 
  mylist2.append(time_elapsed)
# Writing results into excel sheet
  worksheet2.write(row, col, a)
  worksheet2.write(row, col + 1 , b)
  worksheet2.write(row,col+2, result)
  worksheet2.write(row, col+3, time_elapsed)
  
  start = timeit.default_timer()
# Calculating GCD using the Brute Force method
  result = gcd_bruteforce(a,b)
  #print ('gcd using brute force :',result) 
  time_elapsed = timeit.default_timer() - start
  print ('time taken in brute force: ', time_elapsed,'\n')
  mylist3.append(time_elapsed)
# Writing the results into an excel sheet
  worksheet3.write(row, col, a)
  worksheet3.write(row, col + 1 , b)
  worksheet3.write(row,col+2, result)
  worksheet3.write(row, col+3, time_elapsed)  
  
  
  row = row + 1
workbook1.close()
workbook2.close()
workbook3.close()

# The following helps calculate the statistics and write to excel sheet
array1 = np.array(mylist)

worksheet4.write(0, 0, 'Statistics' )
worksheet4.write(0, 1, 'Microseconds')

# Calculating the maximum time taken
worksheet4.write(1, 0, 'Maximum Time' )
worksheet4.write(1, 1, np.max(array1))

# Calculating the minimum time taken
worksheet4.write(2, 0, 'Minimum Time')
worksheet4.write(2, 1, np.min(array1))

# Calculating the average time taken
worksheet4.write(3, 0, 'Average Time')
worksheet4.write(3, 1, np.mean(array1))

# Calculating the median time taken
worksheet4.write(4, 0, 'Median Time')
worksheet4.write(4, 1, np.median(array1))

workbook4.close()

array1 = np.array(mylist2)

worksheet5.write(0, 0, 'Statistics' )
worksheet5.write(0, 1, 'Microseconds')

# Calculating the maximum time taken
worksheet5.write(1, 0, 'Maximum Time' )
worksheet5.write(1, 1, np.max(array1))

# Calculating the minimum time taken
worksheet5.write(2, 0, 'Minimum Time')
worksheet5.write(2, 1, np.min(array1))

# Calculating the average time taken
worksheet5.write(3, 0, 'Average Time')
worksheet5.write(3, 1, np.mean(array1))

# Calculating the median time taken
worksheet5.write(4, 0, 'Median Time')
worksheet5.write(4, 1, np.median(array1))

workbook5.close()

array1 = np.array(mylist3)

worksheet6.write(0, 0, 'Statistics' )
worksheet6.write(0, 1, 'Microseconds')

# Calculating the maximum time taken
worksheet6.write(1, 0, 'Maximum Time' )
worksheet6.write(1, 1, np.max(array1))

# Calculating the minimum time taken
worksheet6.write(2, 0, 'Minimum Time')
worksheet6.write(2, 1, np.min(array1))

# Calculating the average time taken
worksheet6.write(3, 0, 'Average Time')
worksheet6.write(3, 1, np.mean(array1))

# Calculating the median time taken
worksheet6.write(4, 0, 'Median Time')
worksheet6.write(4, 1, np.median(array1))
  
workbook6.close()

#opening Euclid workbook and reading data
wb1= xlrd.open_workbook('Original_Euclid_Results.xlsx')
sh1= wb1.sheet_by_index(0)

#opening Euclid improved workbook and reading data
wb2= xlrd.open_workbook('Second_Euclid_Results.xlsx')
sh2= wb2.sheet_by_index(0)

#opening brute_force workbook and reading data
wb3= xlrd.open_workbook('Brute_Force_Results.xlsx')
sh3= wb3.sheet_by_index(0)

#initializing variables
count1=0
add1=0
sum1=0
count2=0
add2=0
sum2=0
count3=0
add3=0
sum3=0

#comparing time difference between two algorithms
for i in range(1,101):
    if sh1.cell_value(i,3) < sh3.cell_value(i,3):
        count1=count1+1
        add1= sh3.cell_value(i,3) - sh1.cell_value(i,3)
        sum1= sum1+add1
    if sh2.cell_value(i,3) < sh3.cell_value(i,3):
        count2=count2+1
        add2= sh3.cell_value(i,3) - sh2.cell_value(i,3)
        sum2= sum2+add2
    if sh2.cell_value(i,3) < sh1.cell_value(i,3):
        count3=count3+1
        add3= sh1.cell_value(i,3) - sh2.cell_value(i,3)
        sum3= sum3+add3
#creating a text file
f= open("conclusions.txt","w+")

stk1="1.Out of 100 pairs of integers, the original version of Euclid outperformed brute-force in {} pairs; and the average saved time for these {} pairs of integers was {} micro seconds.\n\n"
stk2="2.Out of 100 pairs of integers, the second version of Euclid outperformed brute-force in {} pairs; and the average saved time for these {} pairs of integers was {} micro seconds.\n\n"
stk3="3.Out of 100 pairs of integers, the second version of Euclid outperformed original version in {} pairs; and the average saved time for these {} pairs of integers was {} micro seconds."

#writing to textfile
f.write(stk1.format(count1,count1,sum1))
f.write(stk2.format(count2,count2,sum2))
f.write(stk3.format(count3,count3,sum3))

#closing textfile
f.close()


     





























