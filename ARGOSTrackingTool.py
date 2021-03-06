#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Rebecca Murphy (rgm37@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------
# =============================================================================
# Ask user for search date
user_date = input("Enter data to search for Sara: ")

#Create a variable pointing to the data file
file_name = './Data/Raw/sara.txt'

#Create  file object from the file
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary objects
date_dict = {}
coord_dict = {}

#Iterate through all lines in the lineList
for lineString in line_list[17:]:
    if lineString[0] in ('#', 'u'): continue
# =============================================================================

    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
  
   #if obs_lc not in ("1", "2", "3"):
       # continue
    obs_lat = lineData[6]
    obs_long = lineData[7]
    
    #Print the location of Sarah if lc is 1, 2, or 3
    if obs_lc in ("1", "2", "3"):
        #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, long:{obs_long}.")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_long)

#Create empty list to hold matching keys
matching_keys = []
#Loop through items in the date_dict, and collect keys for matching ones
for date_item in date_dict.items():
    #get the jey date of the item
   the_key, the_date = date_item
    #See if the date matches the user date
   if the_date == user_date:
       matching_keys.append(the_key)
       
# Reveal location for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    obs_date = date_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat}, long:{obs_long} on {user_date}.")