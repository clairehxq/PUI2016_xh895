
finished 15:44 September 19th, 2016
Worked with Mona(NM2773) and Kaylyn(kal573). They both have helped me a lot but we did our assignments on our own.\

Assignment 1:
1. requested API key to access the data
2. used urllib2.urlopen to open the link and stored data.
3. used read json and DataFrame command within pandas package to convert the data to a dataframe.
4. manipulate data: locate the latitude and longitude index we need.
5. export location index with literations

Assignment 2:
the former part is basically the same as assignment 1. Assignment 2 also asks us to export a csv file. With that, we first had to let the terminal know the file name. In the script, file name is a system argument variable.
Right after step 5 in assignment 1, I created an array with a known number of columns which is the exact number of index we needed. We also knew column names. 
Used literations to generate the array with values appended.
To export a csv file, I used df.to_csv(filename). 

Assignment 3:
1. Check environmental variable and see if it's working.
2. find out the path of needed data. With that I used 'cd' and 'ls' command within jupyter cell to locate.
3. used pd.read_csv and pd.DataFrame to store and convert the data to a dataframe.
4. imported numpy and used '%pylab inline' to make sure the plot can be viewed.
5. used 'plt.scatter(x,y)' to plot the dataframe.
6. used plt.xlable, plt.ylable, plt.title, plt.show to append axes names, plot name and to show the plot.


