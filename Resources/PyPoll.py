import csv 
import os

# Assign a variable for the file to load and the path
file_to_load =os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Create options/votes
candidate_options = []
candidate_votes = {}

# Initialize arrays for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

county_options=[]
county_votes={}

largest_county=""
largestCounty_count=0


# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1

        # Get the candidate name and county name from each row
        candidate_name = row[2]
        county_name = row[1]

        # If the county does not match any existing county, add it to the list of counties
        if county_name not in county_options:

            # Add it to the list
            county_options.append(county_name)

            #Begin tracking that county's vote
            county_votes[county_name] = 0

        # Add a vote to county's count
        county_votes[county_name] += 1

        # If the candidate does not match any existing candidate, add to lits of candidates
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
    # Save the results to our text file
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal
        election_results = (
            f"/nElection Results/n"
            f"-------------------------/n"
            f"Total Votes: {total_votes:,}/n"
            f"-------------------------/n" 
            f"/n"
            f"County Votes:/n")
        print(election_results, end="")

        # Save the final vote count to the text file
        txt_file.write(election_results)

        #Iterate through county data
        for county in county_votes:

            # Retrieve votes from each county and percentage
            countyVotes = county_votes[county]
            countyVote_percentage = int(countyVotes) / int(total_votes) * 100

            #Print each county's name, voter turnout, and percentage of turnout to terminal
            county_results = (
                f"{county}: {countyVote_percentage:.1f}% ({countyVotes:,})/n")
            
            print(county_results)

            # Save the candidate results to our text file
            txt_file.write(county_results)

            # Determine county with largest vote count
            if (countyVotes > largestCounty_count):
                largestCounty_count = countyVotes
                largest_county = county

            # Set the county with largest county count to summary
            largest_county_summary = ("/n"
                f"---------------------/n"
                f"Largest County Turnout: {largest_county}/n"
                f"---------------------/n")
        print(largest_county_summary)

        # Save the largest county name to text file
        txt_file.write(largest_county_summary)

        # Iterate through candidate list
        for candidate in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes[candidate]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})/n")

            # Print each candidate's voter count and percentage to the terminal
            print(candidate_results)

            # Save the candidate results to our text file
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and winning candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate

        #print(winning_candidate_summary)
        winning_candidate_summary = (
            f"-------------------------/n"
            f"Winner: {winning_candidate}/n"
            f"Winning Vote: {winning_count:,}/n"
            f"Winning Percentage: {winning_percentage:.1f}/n"
            f"-------------------------/n")
            
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
    