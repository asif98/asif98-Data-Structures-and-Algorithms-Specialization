# python3
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.

    workers = [[0,i] for i in range(n_workers)] #### [next_free_time, index] of a worker
    jobs.reverse()
    process_start = []
    while jobs :
        process_time = jobs.pop()
        next_free_time, next_worker = heapq.heappop(workers)
        heapq.heappush(workers, [next_free_time + process_time, next_worker])
        process_start.append([next_worker, next_free_time])

    return process_start


# n_workers = 4
# jobs = [1]*20
# print(assign_jobs(n_workers, jobs))



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
