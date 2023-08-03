
This folder contains files for KWCC_Prospect_Generator_version0 as well as the original virtual environment used to generate the preliminary prospect lists used to green light the project. As this is an early concept version of the software, it has the following known issues:\

1. The software works by creating a .xlsx, thus, there is nothing in place to aggregate the pull-areas without overlap

2. The software works by searching for places using keywords iterated in a list. This makes it inefficient by calling more API requests for results that have already populated, and removing duplicates thereafter.

3. The software does not create exhaustive lists. Some small and large clients are left off the list for reasons unknown (as of 03-08-2023)