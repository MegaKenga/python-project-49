#!/usr/bin/env python3
from brain_games.engine import run_engine
from brain_games.games.game_check_even import even_check, DESCRIPTION


def main():
    run_engine(even_check, DESCRIPTION)


if __name__ == '__main__':
    main()
