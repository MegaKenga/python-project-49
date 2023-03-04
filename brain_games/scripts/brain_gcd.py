#!/usr/bin/env python3
from brain_games.engine import run_engine
from brain_games.games.game_check_gcd import check_gcd, DESCRIPTION


def main():
    run_engine(check_gcd, DESCRIPTION)


if __name__ == '__main__':
    main()
