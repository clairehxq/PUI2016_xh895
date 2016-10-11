## Cikibike Null Hypothesis project review

Very interesting! It is remarkable that the number of rides by age has such a well defined shape, with a slow rise and a fast decay. You could easily model it.

The null is properly formulated for the question.

The data has to be moved into the PUIDATA directory; data should not be kept in the same directory as code, and for the class it has to be stored in PUIDATA so that we avoiding having multiple copies of redundant data as we grade 90 notebooks. so you should not get data from the puidata dir, which is your own so it only hosts data you downloaded in it, but put your data in that dir. If it is srill not clear please do ask me what I mean.

Imports should all be at the top (pep8) . I often leave them in the middle to show people the workflow but they should be moved.

**All figures should have captions that explain what I am looking at**.

The data is properly processed and it supports a test of means (t-test)  as well as more detailed analysis of the distribution of durations.

