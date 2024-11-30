import pickle
import os
from pathlib import Path
import datetime
import subprocess


def find_all_readmes():
    readmes = {}
    working_dir = Path()
    for path in working_dir.glob(f"./2*/**/*.md"):
        readmes[path] = None
    readmes = dict(sorted(readmes.items()))
    return readmes


def read_log_file():
    readmes = {}
    if os.path.exists('refresh_all_markdowns.log.pkl'):
        with open('refresh_all_markdowns.log.pkl', 'rb') as f:
            readmes = pickle.load(f)
    return readmes


def save_log_file(readmes):
    with open('refresh_all_markdowns.log.pkl', 'wb') as f:
        pickle.dump(readmes, f)


def main():
    readmes = find_all_readmes()
    readmes_log = read_log_file()
    readmes.update(readmes_log)

    for readme in readmes:
        year, day, _ = str(readme).split("/")
        year = int(year)
        day = int(day[4:])
        if (readmes[readme] is None) or (readmes[readme] <= (datetime.datetime.now() -
                                                             datetime.timedelta(minutes=60 * 24 * 31 * 365))):
            print(f"Will refresh {year=} {day=} (last refresh was: {readmes[readme]})")  # noqa
            try:
                p = subprocess.run(
                    f"SESSION_ID=$(<session.cookie) python3 -m aoc_to_markdown -y {
                        year} -d {day} -o {year} -i",
                    shell=True,
                    capture_output=True,
                    check=True)
            except subprocess.CalledProcessError as e:
                print(
                    f"Command failed with code: {e.returncode}\n{e.stdout=}\n{e.stderr=}")  # noqa
                raise e
            print(
                f"Command success with code: {p.returncode}")  # noqa
            readmes[readme] = datetime.datetime.now()
            save_log_file(readmes)
        else:
            print(f"Will skip {year=} {day=} (last refresh was: {readmes[readme]})")  # noqa


if __name__ == '__main__':
    main()
