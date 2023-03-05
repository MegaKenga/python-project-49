#!/usr/bin/env python3
from brain_games.engine import run_engine
from brain_games.games.game_check_progression import check_progression
from brain_games.games.game_check_progression import DESCRIPTION


def main():
    run_engine(check_progression, DESCRIPTION)


if __name__ == '__main__':
    main()
