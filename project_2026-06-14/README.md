# Daily Project - 2026-06-14

## Overview

Today's project is a command-line **Secret Santa Generator**. It ensures secure and random pairings for a group of people, guaranteeing that no participant is assigned to themselves (a valid derangement).

## Features

- Takes a list of unique names as input via the CLI.
- Automatically pairs each participant with exactly one other participant.
- Employs `secrets.SystemRandom().shuffle()` to perform a cryptographically secure shuffle.
- Enforces validity constraints: prevents self-pairing and requires at least two participants with unique names.

## Usage

You can run the script from the command line by passing the list of names:

```bash
python3 cli.py Alice Bob Charlie David Eve
```

Output Example:
```
Secret Santa Assignments:
-------------------------
David      ->  Charlie
Charlie    ->  Alice
Alice      ->  Eve
Eve        ->  Bob
Bob        ->  David
```

## Running Tests

To verify the core logic, run the unit tests provided:

```bash
PYTHONPATH=. python3 -m unittest test_secret_santa.py
```
