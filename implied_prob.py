from sys import argv
import numpy as np


def implied_prob_american(odds_a, odds_b):
    """Both odds are in American odds format
    Returns implied probabilities in decimal format
    if odds are postitive (e.g. +200) input as 200"""

    def odds(line):
        if line > 0: # Underdog
            return 1 - (line / (100 + line))
        else: # Favorite
            line = np.abs(line)
            return line / (100 + line)

    implied_prob_a = odds(odds_a)
    implied_prob_b = odds(odds_b)
    return implied_prob_a, implied_prob_b


def implied_prob_decimal(odds_a, odds_b):
    
    def odds(line):
        return 1 / line

    return odds(odds_a), odds(odds_b)
    

def main():
    """Main function"""
    if len(argv) != 4:
        print("Usage: python implied_prob.py <odds_a> <odds_b> <type>")
        exit(1)

    odds_a = float(argv[1])
    odds_b = float(argv[2])
    if argv[3] == "American":
        implied_prob_a, implied_prob_b = implied_prob_american(odds_a, odds_b)
        print("Implied probability of A winning: {:.4f}".format(implied_prob_a))
        print("Implied probability of B winning: {:.4f}".format(implied_prob_b))
    
    elif argv[3] == "Decimal":
        implied_prob_a, implied_prob_b = implied_prob_decimal(odds_a, odds_b)
        print("Implied probability of A winning: {:.4f}".format(implied_prob_a))
        print("Implied probability of B winning: {:.4f}".format(implied_prob_b))
    
    else:
        print('<type> must be either "American" or "Decimal"')
        exit(1)


if __name__ == '__main__':
    main()