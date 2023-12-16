def read_file() -> list:
    with open(f"{__file__.rstrip('main.py')}input.txt", "r") as f:
        return [str(line) for line in f.readlines()]


def part_1(inp):
    run_order = ''
    tasks = []
    for line in inp:
        _, a, _, _, _, _, _, b, _, _ = line.split()
        tasks.append([a, b])
    while True:
        a_set = set([a for a, _ in tasks])
        b_set = set([b for _, b in tasks])
        task_to_start = list(sorted(a_set.difference(b_set)))[0]
        run_order += task_to_start
        tasks = [v for v in tasks if v[0] != task_to_start]
        if (len(a_set) == 1) and (len(b_set) == 1):
            run_order += b_set.pop()

        if tasks == []:
            break
    return run_order


def part_2(inp):
    max_time = 2000
    worker_n = 5
    workers = {k: [None] * max_time for k in range(worker_n)}
    time_add = 60
    run_order = ''
    curr_time = 0
    tasks = []
    tasks_set = set()
    for line in inp:
        _, a, _, _, _, _, _, b, _, _ = line.split()
        tasks.append([a, b])
        tasks_set.add(a)
        tasks_set.add(b)

    while True:
        done_task = set.union(*[set(v[:curr_time]) for v in workers.values()])
        undone_task = set.union(*[set(v[curr_time:])
                                  for v in workers.values()])
        done_task = done_task.difference(undone_task)

        for t in done_task:
            tasks = [v for v in tasks if t != v[0]]
            if t in tasks_set:
                tasks_set.remove(t)

        a_set = set([a for a, _ in tasks])
        b_set = set([b for _, b in tasks])
        available_tasks = a_set.difference(b_set)
        running_tasks = set([v[curr_time] for k, v in workers.items()])
        to_start_tasks = available_tasks.difference(
            running_tasks).difference(done_task)
        if len(tasks_set) == 1:
            to_start_tasks = tasks_set
        # print("!", curr_time, available_tasks,
        #       running_tasks, done_task, to_start_tasks, tasks_set)
        for task_to_start in list(sorted(to_start_tasks)):
            avail_workers = [
                k for k, v in workers.items() if v[curr_time] is None]
            if avail_workers:
                worker_id = min(avail_workers)
                task_time = (ord(task_to_start) - ord('A')) + time_add + 1
                for i in range(curr_time, curr_time + task_time):
                    workers[worker_id][i] = task_to_start

        curr_time += 1
        # print(workers)

        if tasks == []:
            max_time = 0
            for k, v in workers.items():
                while v and v[-1] is None:
                    del v[-1]
                max_time = max(max_time, len(v))
            return max_time
            break
    return run_order


def main():
    inp = read_file()
    res_1 = part_1(inp)
    print(f"res_1: {res_1}")
    res_2 = part_2(inp)
    print(f"res_2: {res_2}")


if __name__ == '__main__':
    main()
