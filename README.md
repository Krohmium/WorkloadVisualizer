# WorkloadVisualizer 
WorkloadVisualizer is a simple Python PoC to visualize workload before deadlines.
So far, you can define deadline dates and the number of days needed for preparation before each deadline. The script will accumulate each day's workload, increasing the count when preparation days overlap. The script generates a histogram from this data to see where the workload is high so you can plan accordingly. 

# Further Plans
* Add option to  generate a preparation plan that shifts preparation to earlier dates if a certain threshold of workload is met (maybe with different algorithms to choose)
* Add an interface that allows adding data in a more userfriendly way
* Add a save file for data
