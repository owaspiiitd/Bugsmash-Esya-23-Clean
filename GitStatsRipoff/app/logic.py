import git
import os
import subprocess
import json
import matplotlib.pyplot as plt
from collections import Counter
from typing import List, Dict
from collections import defaultdict
from pylint.lint import Run
from datetime import datetime



def get_top_contributors(repo: git.Repo) -> List[str]:
    """
    Returns a list of the top 10 contributors to a Git repository.
    """
    contributors = Counter()
    for commit in repo.iter_commits():
        contributors[commit.author.email] += 1
    top_contributors = [contributor for contributor in contributors.most_common(10)]
    return top_contributors

def get_lines_of_code_by_language(repo: git.Repo) -> Dict[str, int]:
    """
    Returns a dictionary containing the number of lines of code in each language in a directory.
    """
    local_dir = repo.working_dir
    lines_by_language = {}
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            filepath = os.path.join(root, file)
            output = subprocess.check_output(['cloc', '--json', filepath])
            if (output == b'') : continue
            data = json.loads(output)
            if 'header' in data: del data['header']
            if 'SUM' in data: del data['SUM']
            for language, stats in data.items():
                if language not in lines_by_language:
                    lines_by_language[language] = 0
                lines_by_language[language] += stats['code']
    return lines_by_language



def plot_commits_over_time(repo: git.Repo):
    """
    Plots the distribution of commits over time.
    """
    # Initialize a dictionary to store the distribution of commits by date
    commits_by_date = defaultdict(int)

    # Iterate over all commits in the repository
    for commit in repo.iter_commits():
        # Extract the commit date and increment the count for that date
        commit_date = commit.committed_datetime.date()
        commits_by_date[commit_date] += 1

    # Convert the dictionary to two lists for plotting
    dates = list(commits_by_date.keys())
    counts = list(commits_by_date.values())

    # Plot the distribution of commits over time
    plt.plot(dates, counts)
    plt.xlabel('Date')
    plt.ylabel('Number of Commits')
    plt.title('Distribution of Commits Over Time')
    plt.show()
    print(f"Plot saved to '{datetime.now()}_commits_over_time.png'")
    plt.savefig(f'{datetime.now()}_commits_over_time.png')


def find_code_smells(repo: git.Repo):
    """
    Finds code smells in a Git repository for python files using PyLint.
    """

    for blob in repo.tree().traverse():
        if blob.type == 'blob' and blob.name.endswith('.py'):
            with open(blob.abspath, 'r') as f:
                source = f.read()
                results = Run([blob.abspath], do_exit=False)
                num_code_smells = results.linter.stats.global_note
                print(f"{blob.abspath}: {num_code_smells} code smells found")