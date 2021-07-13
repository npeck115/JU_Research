# ImageComparison.py (rough draft)
#
# The program displays the total time in seconds that
# a user looked at the left-image and the right-image.
#
# Created by: Nathaniel Peck
# May 6, 2021

import csv

def main():
    # Initial User Prompt
    print()
    print("##############################")
    print("Image Comparison Tool")
    print()
    print("Please enter the following data.")
    
    # User inputs participant's data
    participant = int(input("Participant number: "))
    starting_id = int(input("Starting Fixation ID: "))
    ending_id = int(input("Ending Fixation ID: "))
    print()
    
    # User inputs the file's path and file's name
    # File must be a .csv
    print("Enter file's path and file's name.")
    print("Like this: C:\\filepath\\test.csv")
    filename = input("Enter here: ")
    print()
    
    # Coordinates of two images
    # Images share the same y-coordinates (top and bottom)
    top = 0.114
    bottom = 0.485
    
    left_image_left_side = 0.194
    left_image_right_side = 0.456
    right_image_left_side = 0.471
    right_image_right_side = 0.733
    
    # Time Durations
    # Caution: These are the only rough estimates.
    image_duration = 2
    pause_duration = 4
    
    # Arrays to store total time for each image 
    left_images = []
    right_images = []
    
    # Sum of image times
    sum_left = 0
    sum_right = 0
    
    # Timing of previous image block
    previous_time = 0
    
    # Try-Except catches "FileNotFoundError" 
    try:
        # Creates array of column headings
        with open(filename) as csv_file:
            heading_reader = csv.reader(csv_file, delimiter = ',')
            headings = next(heading_reader)
        
        with open(filename) as csv_file:
            
            # Reader for gathering data from csv file
            data_reader = csv.DictReader(csv_file)
            
            # Loop for reading each row of data
            for row in data_reader:
                fixation_id = int(row["CNT"])
                
                # Reads only id's within user inputted range
                if (fixation_id >= starting_id and fixation_id <= ending_id):
                    current_time = float(row[headings[3]])
                    x = float(row[headings[5]])
                    y = float(row[headings[6]])
                    fixation_duration = float(row[headings[8]])
                    
                    # Start timer at starting fixation id
                    if (fixation_id == starting_id):
                        timer = current_time
                        
                    # Checks if fixation is in an image
                    if (y > top and y < bottom):
                        # Checks if fixation is in left image
                        if (x > left_image_left_side and \
                            x < left_image_right_side and \
                            current_time <= (timer + image_duration) and \
                            current_time >= previous_time):
                            sum_left += fixation_duration
                            
                        # Checks if fixation is in right image
                        elif (x > right_image_left_side and \
                            x < right_image_right_side and  \
                            current_time <= (timer + image_duration) and \
                            current_time >= previous_time):
                            sum_right += fixation_duration
                            
                    elif (current_time >= (timer + image_duration)):
                        left_images.append(sum_left)
                        print("sum_left:", sum_left)
                        right_images.append(sum_right)
                        print("sum_right:", sum_right)
                        sum_left = 0
                        sum_right = 0
                        previous_time = timer + image_duration
                        timer += pause_duration
            
            # Sum the entire duration of left images
            sum_left = 0
            for i in range(len(left_images)):
                sum_left += left_images[i]
            
            #Sum the entire duration of right images
            sum_right = 0
            for i in range(len(right_images)):
                sum_right += right_images[i]
                    
    except FileNotFoundError:
        print("Error: File not found.")
    
    # Print output to user
    print("Participant " + str(participant) + "'s Data")
    print()
    print("Image Fixations:")
    print()
    print("\t\tLeft Image\tRight Image")
    
    # Image Counter
    counter = 0
    total_image_sets = 30    
    
    while (counter < total_image_sets):
        print("Image " + str(counter) + "\t" + str(left_images[i]) + \
              "\t" + str(right_images[i]))
        counter += 1
        
    print()
    print("Total Fixation of Left Image:", sum_left)
    print("Total Fixation of Right Image:", sum_right)
    print()    
    
    return 0

main()