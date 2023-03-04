#!/usr/bin/env python3
from brain_games.engine import run_engine
from brain_games.games.game_check_prime import check_prime, DESCRIPTION


def main():
    run_engine(check_prime, DESCRIPTION)


if __name__ == '__main__':
    main()
