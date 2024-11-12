class Candidate:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

    def get_name(self):
        return self.name

    def get_votes(self):
        return self.votes

    def add_votes(self, additional_votes):
        self.votes += additional_votes


class Elections:
    def __init__(self, num_of_voters):
        self.candidates = []
        self.num_of_voters = num_of_voters

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def total_votes_cast(self):
        return sum(candidate.get_votes() for candidate in self.candidates)

    def get_candidates(self):
        return self.candidates

    def display_results(self):
        total_votes_cast = self.total_votes_cast()
        total_possible_votes = self.num_of_voters

        print("Election Results:")
        for candidate in self.candidates:
            votes = candidate.get_votes()
            percent_of_cast_votes = (votes / total_votes_cast) * 100 if total_votes_cast > 0 else 0
            percent_of_possible_votes = (votes / total_possible_votes) * 100 if total_possible_votes > 0 else 0
            print(f"{candidate.get_name()} - Votes: {votes} "
                  f"({percent_of_cast_votes:.2f}% of cast votes, {percent_of_possible_votes:.2f}% of possible votes)")

    def get_winner(self):
        total_votes_cast = self.total_votes_cast()
        if total_votes_cast == 0:
            return None
        return max(self.candidates, key=lambda candidate: candidate.get_votes())

    def has_winner_with_51_percent(self):
        total_votes_cast = self.total_votes_cast()
        for candidate in self.candidates:
            if total_votes_cast > 0 and (candidate.get_votes() / total_votes_cast) * 100 >= 51:
                return candidate
        return None


class Corruption:
    def __init__(self, num_of_voters, candidates):
        self.num_of_voters = num_of_voters
        self.candidates = candidates

    def count_spare_votes(self):
        total_votes_cast = sum(candidate.get_votes() for candidate in self.candidates)
        spare_votes = self.num_of_voters - total_votes_cast if self.num_of_voters > total_votes_cast else 0
        return spare_votes

    def calculate_bribes_for_all(self):
        total_possible_votes = self.num_of_voters
        majority_votes = int(total_possible_votes * 0.51) 

        results = {}
        spare_votes = self.count_spare_votes()

        for candidate in self.candidates:
            current_votes = candidate.get_votes()
            if current_votes >= majority_votes:
                needed_grechka = 0
            else:
                needed_grechka = majority_votes - current_votes

            results[candidate.get_name()] = {
                "needed_grechka": needed_grechka
            }

        return results, spare_votes


def main():
    num_of_voters = int(input("Enter total number of voters: "))
    elections = Elections(num_of_voters)

    for i in range(5):
        name = input(f"Enter candidate name {i+1}: ")
        votes = int(input(f"Enter number of votes for {name}: "))
        candidate = Candidate(name, votes)
        elections.add_candidate(candidate)

    elections.display_results()

    corruption = Corruption(num_of_voters, elections.get_candidates())
    winner = elections.has_winner_with_51_percent()

    if winner:
        print(f"\nThe winner with 51% of the votes is {winner.get_name()} with {winner.get_votes()} votes.")
    else:
        print("\nNo candidate has 51% of the cast votes.")
        print("Calculating the amount of grechka needed for each candidate to win...")

    bribe_results, spare_votes = corruption.calculate_bribes_for_all()

    print(f"\nSpare votes available for bribing: {spare_votes}\n")
    for candidate_name, data in bribe_results.items():
        print(f"{candidate_name}:")
        print(f"  Needed grechka: {data['needed_grechka']} kg")

    for candidate_name, data in bribe_results.items():
        if data["needed_grechka"] <= spare_votes:
            print(f"\nIt is possible to bribe enough voters for {candidate_name} to reach 51%.")
        else:
            print(f"\nNot enough spare votes available to bribe for {candidate_name} to reach 51%.")


if __name__ == "__main__":
    main()
