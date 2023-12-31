import os
from datetime import datetime, timedelta

# Set up Git configuration
os.system('git config --global user.email "samikhakumari0657@gmail.com"')
os.system('git config --global user.name "smitawom"')


def makeCommits(year: int):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 6, 1)
    current_date = start_date

    # Ensure we're in the correct directory
    os.chdir('https://github.com/smitawom/sworn.git')

    # Check if the branch exists, if not create it
    os.system('git checkout -b main || git checkout main')

    while current_date <= end_date:
        # Create a commit on the current date
        with open('data.txt', 'a') as file:
            file.write(f'{current_date.strftime("%Y-%m-%d %H:%M:%S")} <- this was the commit for the day!!\n')

        # Staging
        os.system('git add data.txt')

        # Commit with the specific date
        os.system(
            f'GIT_COMMITTER_DATE="{current_date.strftime("%Y-%m-%d %H:%M:%S")}" git commit --date="{current_date.strftime("%Y-%m-%d %H:%M:%S")}" -m "Commit on {current_date.strftime("%Y-%m-%d")}"')

        # Move to the next date (next day)
        current_date += timedelta(days=1)

    # Push changes to the remote repository once at the end
    os.system('git push origin main')


# Start the commit process for the year 2024
makeCommits(2024)
