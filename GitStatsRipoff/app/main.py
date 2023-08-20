import os
import git
import emoji
from termcolor import colored
from yaspin import yaspin
from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

from logic import get_top_contributors, get_lines_of_code_by_language
from logic import plot_commits_over_time, find_code_smells

r: git.Repo = None

def inputs() -> git.Repo:
    """
    For handling first time inputs, and also subsequent inputs
    """
    repository = prompt((f"{emoji.emojize(':link:')} Enter the link or path to the remote repository: "))
    clone_location = None

    # Prompt the user to enter a directory
    clone_location = prompt((f"{emoji.emojize(':file_folder:')} Enter a directory: "), completer=PathCompleter())

    if not os.path.exists(clone_location):
        os.makedirs(clone_location)

    config_options = []

    # continuously take in config files till you reach a blank line
    while True:
        # config is a string
        config = prompt((f"{emoji.emojize(':gear:')} Enter a config file (leave blank to continue): "))
        if not config:
            break
        config_options.append(config)

    # Clone the repository
    with yaspin(text=f"{emoji.emojize(':rocket:')} Cloning repository...", color="yellow"):
        r = git.Repo.clone_from(repository, clone_location, multi_options=config_options)

    return r

r = inputs()

while True:
    action = prompt(
        f"{emoji.emojize(':hammer_and_wrench:')} Select an action:\n"
        f"1) Get top contributors\n"
        f"2) Lines of code by language\n"
        f"3) Distribution of Commits over Time\n"
        f"4) Calculate Code Smells : Unused Variables, Unused imports, inconsistent naming, etc.\n"
        f"5) Input repository\n"
        f"6) Exit\n"
    )

    if action == "6":
        break

    if action == "5":
        r = inputs()
    else:
        if r is None:
            print(colored(f"Please input a repository first", "red"))
        else:
            if action == "1":
                op = get_top_contributors(r)
            elif action == "2":
                op = get_lines_of_code_by_language(r)
            elif action == "3":
                op = plot_commits_over_time(r)
            elif action == "4":
                op = find_code_smells(r)
            else:
                print(colored(f"Invalid action", "red"))
                continue

            if op is not None:
                print(colored(f"{emoji.emojize(':sparkles:')} {op}", "green"))