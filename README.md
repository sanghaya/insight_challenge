General Approach:

Since we're not allowed to use additional database, I tried to keep the information read from the textfile efficiently as possible in the memory. As one solution, I used class using slots, which allocates memory for fixed attributes, instead of making dictionaries within a class.
For the medianvals_by_zip.txt, since we have to keep track of running median, I directly wrote in the output file as each input line was read.
For the medianvals_by_date.txt, since we only have to print the aggregated information, I wrote in the output file after I've seen all the data.

Outside dependencies:

I didn't use any outside dependency, all libraries that I used are built-in.

How to run:

Run the script ./run.sh

Runtime:

Since github only allows up to 100mb, I just have default text file as input.
But I've tried the code on bigger files, and here's the brief rundown of runtime for 3 files that I got from FEC.
The runtime seems roughly O(2n) where n is the number of rows in the input. I used cProfile to keep track of the performance.

50 MB: 10 secs
75 MB: 36 secs
350 MB: 150 secs

Comments:

This was a fun challenge! Thank you for making it :) Let me know if you have any questions and will be looking forward to hearing from the Insight Team soon.
