import time
import os
from pathlib import Path
import datetime
import subprocess
import json
import re
from tabulate import tabulate


def create_markdown_from_json(json_object):
    headers = [
        'Year',
        'Day',
        'Interpreter name',
        'Elapsed time [s]',
        'Check execution time']
    table = []
    for path_name, path_value in json_object.items():
        _, year, day, _ = str(path_name).split("/")
        year = int(year)
        day = int(day[4:])
        r_name = None
        r_elapsed_time_s = None
        r_exec_time = None
        if path_value:
            for c_name, c_value in path_value.items():
                r_name = c_name
                r_elapsed_time_s = c_value['elapsed_time_s']
                r_exec_time = datetime.datetime.fromtimestamp(
                    c_value['exec_time'])
                row = [
                    year,
                    day,
                    r_name,
                    r_elapsed_time_s,
                    r_exec_time
                ]
                table.append(row)
        else:
            row = [
                year,
                day,
                r_name,
                r_elapsed_time_s,
                r_exec_time
            ]
            table.append(row)
    table = list(sorted(table))
    with open("README.md", "w") as f:
        f.write(tabulate(table, headers, tablefmt="github", floatfmt="010.6f"))


def find_all_mains():
    mains = {}
    working_dir = Path()
    for path in working_dir.glob(f"../2*/**/main.py"):
        mains[str(path)] = {}
    return dict(sorted(mains.items()))


def read_log_file():
    runtimes = {}
    if os.path.exists('refresh_all_runtimes.json'):
        with open('refresh_all_runtimes.json', 'r') as f:
            runtimes = json.load(f)
    return runtimes


def save_log_file(runtimes):
    with open('refresh_all_runtimes.json', 'w') as f:
        json.dump(runtimes, f, indent=4)


def get_answer_from_readme(m_path):
    r_path = str(m_path).replace('main.py', 'README.md')
    readme_str = Path(r_path).read_text()
    answers = re.findall(
        r'Your puzzle answer was (.*)\.',
        readme_str,
        flags=re.MULTILINE)
    return answers


def get_python_3_version():
    p = subprocess.run(
        "python3 --version",
        shell=True,
        capture_output=True,
        check=True)
    python_3_version = p.stdout.decode().split()[1]
    return python_3_version


def get_pypy_3_version():
    p = subprocess.run(
        "pypy3 --version",
        shell=True,
        capture_output=True,
        check=True)
    pypy_3_version = p.stdout.decode().split()
    pypy_3_version = f"{pypy_3_version[1]} ({pypy_3_version[8]})"
    return pypy_3_version


def run_one_day(mains, m, year, day, readme_answers, min_time_from_last_run,
                interpreter_name_version, interpreter_command, timeout):
    if interpreter_name_version not in mains[m]:
        mains[m][interpreter_name_version] = {
            'exec_time': 0,
            'elapsed_time_s': 0,
        }
    tmp_exec_time_epoch = mains[m][interpreter_name_version]['exec_time']
    tmp_exec_time = datetime.datetime.fromtimestamp(tmp_exec_time_epoch)
    tmp_compare_time_epoch = (
        datetime.datetime.now() -
        min_time_from_last_run).timestamp()
    tmp_compare_time = datetime.datetime.fromtimestamp(
        tmp_compare_time_epoch)
    if tmp_exec_time_epoch > tmp_compare_time_epoch:
        print(f"\t{interpreter_name_version} - Will skip {year=} {day=} (last refresh was: {tmp_exec_time})")  # noqa
        return False

    print(f"\t{interpreter_name_version} - Will refresh runtime for {year=} {day=} (last refresh was: {tmp_exec_time}) ...")  # noqa
    p = None
    try:
        start_time = time.time_ns()
        p = subprocess.run(
            f"{interpreter_command} {m}",
            shell=True,
            capture_output=True,
            check=True,
            timeout=timeout)
        finish_time = time.time_ns()
        elapsed_time_s = (finish_time - start_time) / (10**9)
        elapsed_time_s_str = f"{elapsed_time_s:010.6f}"

        process_answers = p.stdout.decode()
        process_answers = re.split(
            r'res_1:|res_2:', process_answers, flags=re.MULTILINE)
        process_answers = [c.strip()
                           for c in process_answers if c.strip() != '']
        for i in range(2):
            try:
                if str(process_answers[i]) == str(readme_answers[i]):
                    print(f"\t\tAnswer for part {i + 1} matching: {process_answers[i]}")  # noqa
                else:
                    print(f"\t\tAnswer for part {i + 1} DOES NOT matching: {process_answers[i]=} {readme_answers[i]=}")  # noqa
            except IndexError as e:
                print(f"\t\tNo answer for part {i + 1}? ({process_answers[i]=})")  # noqa
        mains[m][interpreter_name_version] = {
            'exec_time': datetime.datetime.now().timestamp(),
            'elapsed_time_s': elapsed_time_s_str,
        }
    except subprocess.CalledProcessError as e:
        print(
            f"\tCommand failed with code: {e.returncode}\n{e.stdout=}\n{e.stderr=}")  # noqa
        raise e
    except subprocess.TimeoutExpired as e:
        print(
            f"\tCommand timeout after {timeout} seconds: \n{e.stdout=}\n{e.stderr=}")  # noqa
        mains[m][interpreter_name_version] = {
            'exec_time': datetime.datetime.now().timestamp(),
            'elapsed_time_s': f'>{timeout}s',
        }
    if p:
        print(
            f"\tCommand success with code: {p.returncode}")  # noqa
    create_markdown_from_json(mains)
    save_log_file(mains)
    return True


def main():
    mains = find_all_mains()
    runtimes_log = read_log_file()
    mains.update(runtimes_log)
    python_3_version = get_python_3_version()
    python_3_version = f'python3 ({python_3_version})'

    pypy3_version = get_pypy_3_version()
    pypy3_version = f'pypy3 ({pypy3_version})'
    min_time_from_last_run = datetime.timedelta(minutes=60 * 24 * 31 * 365)
    for m in list(mains.keys())[:25]:
        print(f"Processing file: {m}")
        readme_answers = get_answer_from_readme(m)
        _, year, day, _ = m.split("/")
        year = int(year)
        day = int(day[4:])
        # Python 3
        run_one_day(
            mains=mains,
            m=m,
            year=year,
            day=day,
            readme_answers=readme_answers,
            min_time_from_last_run=min_time_from_last_run,
            interpreter_name_version=python_3_version,
            interpreter_command="python3",
            timeout=30
        )
        # Pypy 3
        run_one_day(
            mains=mains,
            m=m,
            year=year,
            day=day,
            readme_answers=readme_answers,
            min_time_from_last_run=min_time_from_last_run,
            interpreter_name_version=pypy3_version,
            interpreter_command="pypy3",
            timeout=15
        )


if __name__ == '__main__':
    main()
