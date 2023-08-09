import os
import csv

#open csv
csvpath=os.path.join("Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    print("Header" + str(csvheader))

    #set variables
    votes = []
    county = []
    candidates = []
    Charles_Casper_Stockham = []
    Diana_DeGette = []
    Raymon_Anthony_Doane = []

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    
    total_votes = len(votes)
    print(len(votes))

    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidates)

        elif candidate == "Diana DeGette":
            Diana_DeGette.append(candidates)

        else:
            Raymon_Anthony_Doane.append(candidates)

    print(len(Charles_Casper_Stockham))
    print(len(Diana_DeGette))
    print(len(Raymon_Anthony_Doane))

    Charles_Casper_Stockham_percent = round(len(Charles_Casper_Stockham) / (total_votes) * 100, 3)
    Diana_DeGette_percent = round(len(Diana_DeGette) / (total_votes) * 100, 3)
    Raymon_Anthony_Doane_percent = round(len(Raymon_Anthony_Doane) / (total_votes) * 100, 3)

    print(Charles_Casper_Stockham_percent)
    print(Diana_DeGette_percent)
    print(Raymon_Anthony_Doane_percent)


    if Charles_Casper_Stockham_percent > Diana_DeGette_percent and Raymon_Anthony_Doane_percent:
        winner = "Charles Casper Stockham"

    elif Diana_DeGette_percent > Charles_Casper_Stockham_percent and Raymon_Anthony_Doane_percent:
        winner = "Diana DeGette"

    else :
        winner = "Raymon Anthony Doane"

    print(winner)

    file = open("results.txt", "w")
    file.write("Election Results" + "\n")
   
    file.write("-------------------------" + "\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------" + "\n")
    
    file.write("Charles Casper Stockham: " + str(Charles_Casper_Stockham_percent) + "% (" + str(len(Charles_Casper_Stockham)) + ")" + "\n")
    file.write("Diana DeGette: " + str(Diana_DeGette_percent) + "% (" + str(len(Diana_DeGette)) + ")" + "\n")
    file.write("Raymon Anthony Doane: " + str(Raymon_Anthony_Doane_percent) + "% (" + str(len(Raymon_Anthony_Doane)) + ")" + "\n")
    
    file.write("-------------------------" + "\n")
    file.write("Winner: " + str(winner) + "\n")
    file.write("-------------------------" + "\n")
    
    file.close()

