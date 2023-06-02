def vote(name):
    if name in candidates:
        vote_count[name] = vote_count.get(name, 0) + 1
        return True
    else:
        return False

def print_winner():
    max_votes = max(vote_count.values())
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
    for winner in winners:
        print(winner)
    print()


# List of candidates
candidates = ["Candidate A", "Candidate B", "Candidate C"]

# Dictionary to store vote counts
vote_count = {}
 
# Voting process
while True:
    vote_input = input("Enter the name of the candidate (or 'done' to finish voting): ")
    if vote_input == "done":
        break
    success = vote(vote_input)
    if not success:
        print("Invalid ballot. Please enter a valid candidate name.")

# Printing the winners
print("Vote count:")
print(vote_count)
print("Winner(s):")
print_winner()
