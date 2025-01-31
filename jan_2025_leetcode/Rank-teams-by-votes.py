'''
Problem :

We need to rank the teams based on the votes given by the team members. 
The team members are given in the form of a string where each character represents a 
team member's vote. The team members are ranked based on the votes given by them. 
The team with the highest votes will be ranked first, and the team with the lowest 
votes will be ranked last. If two teams have the same number of votes, then the team 
with the lexicographically smaller team name will be ranked higher. We need to return 
the ranking of the teams based on the votes given by the team members.

votes : List[str]
return : str

Example 1:

Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
Explanation: 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.
Example 2:

Input: votes = ["WXYZ","XYZW"]
Output: "XWYZ"
Explanation:
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position. 
Example 3:

Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
Explanation: Only one voter, so their votes are used for the ranking.
'''
from typing import List
from functools import cmp_to_key

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""
        
        teams = list(votes[0])  # Extract the team names from the first vote
        num_teams = len(teams)
        
        # Initialize a dictionary to hold the vote counts for each position for each team
        vote_counts = {team: [0] * num_teams for team in teams}
        
        # Populate the vote counts based on each vote
        for vote in votes:
            for position, team in enumerate(vote):
                vote_counts[team][position] += 1
        
        # Define a comparator function to sort the teams based on the problem's criteria
        def compare(team_a, team_b):
            for pos in range(num_teams):
                a_count = vote_counts[team_a][pos]
                b_count = vote_counts[team_b][pos]
                if a_count != b_count:
                    return b_count - a_count  # Higher count comes first
            # If all counts are equal, sort alphabetically
            return 1 if team_a > team_b else -1
        
        # Sort the teams using the custom comparator
        sorted_teams = sorted(teams, key=cmp_to_key(compare))
        
        # Join the sorted teams into a string and return
        return ''.join(sorted_teams)

if __name__ == "__main__":
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    s = Solution()
    print(s.rankTeams(votes))