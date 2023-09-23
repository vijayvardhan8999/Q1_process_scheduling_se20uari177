def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    waiting_time[0] = 0
    turnaround_time[0] = processes[0][2]  # Burst time of the first process

    for i in range(1, n):
        waiting_time[i] = turnaround_time[i - 1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]

    return waiting_time, turnaround_time

def sjf(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    processes.sort(key=lambda x: x[2])  # Sort by burst time (shortest first)

    waiting_time[0] = 0
    turnaround_time[0] = processes[0][2]

    for i in range(1, n):
        waiting_time[i] = turnaround_time[i - 1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]

    return waiting_time, turnaround_time

def ps(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    processes.sort(key=lambda x: x[3])  # Sort by priority (lowest priority first)

    waiting_time[0] = 0
    turnaround_time[0] = processes[0][2]

    for i in range(1, n):
        waiting_time[i] = turnaround_time[i - 1]
        turnaround_time[i] = waiting_time[i] + processes[i][2]

    return waiting_time, turnaround_time

from collections import deque

def rr(processes, quantum):
    n = len(processes)
    remaining_time = [process[2] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    queue = deque()
    current_time = 0

    while True:
        
        for i in range(n):
            if remaining_time[i] > 0:
                all_done = False
                if remaining_time[i] <= quantum:
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - processes[i][2]
                    turnaround_time[i] = current_time
                    remaining_time[i] = 0
                else:
                    current_time += quantum
                    remaining_time[i] -= quantum
                    queue.append(i)
        all_done = True
        if all_done:
            break

        while queue:
            next_process = queue.popleft()
            if remaining_time[next_process] > 0:
                queue.append(next_process)
                break

    return waiting_time, turnaround_time

# Process format: (process_id, arrival_time, burst_time, priority)
processes = [(1, 0, 24, 3), (2, 4, 3, 1), (3, 5, 3, 4), (4, 6, 12, 2)]

print("FCFS:")
fcfs_waiting_time, fcfs_turnaround_time = fcfs(processes)
for i, process in enumerate(processes):
    print(f"Process {process[0]}: Waiting Time = {fcfs_waiting_time[i]}, Turnaround Time = {fcfs_turnaround_time[i]}")
fcfs_sum = 0
fcfs_turn_sum=0
for i, process in enumerate(processes):
    fcfs_sum += fcfs_waiting_time[i]
    fcfs_turn_sum += fcfs_turnaround_time[i]
print(f"average_waiting_time = {fcfs_sum/len(processes)},average_turnaround_time={fcfs_turn_sum/len(processes)}")


print("\nSJF:")
sjf_waiting_time, sjf_turnaround_time = sjf(processes)
for i, process in enumerate(processes):
    print(f"Process {process[0]}: Waiting Time = {sjf_waiting_time[i]}, Turnaround Time = {sjf_turnaround_time[i]}")
sjf_sum = 0
sjf_turn_sum=0
for i, process in enumerate(processes):
    sjf_sum += sjf_waiting_time[i]
    sjf_turn_sum += sjf_turnaround_time[i]
print(f"average_waiting_time = {sjf_sum/len(processes)},average_turnaround_time={sjf_turn_sum/len(processes)}")

print("\nPS:")
ps_waiting_time, ps_turnaround_time = ps(processes)
for i, process in enumerate(processes):
    print(f"Process {process[0]}: Waiting Time = {ps_waiting_time[i]}, Turnaround Time = {ps_turnaround_time[i]}")
ps_sum = 0
ps_turn_sum=0
for i, process in enumerate(processes):
    ps_sum += ps_waiting_time[i]
    ps_turn_sum += ps_turnaround_time[i]
print(f"average_waiting_time = {ps_sum/len(processes)},average_turnaround_time={ps_turn_sum/len(processes)}")

print("\nRR (Time Quantum = 4):")
rr_waiting_time, rr_turnaround_time = rr(processes, 4)
for i, process in enumerate(processes):
    print(f"Process {process[0]}: Waiting Time = {rr_waiting_time[i]}, Turnaround Time = {rr_turnaround_time[i]}")
rr_sum = 0
rr_turn_sum=0
for i, process in enumerate(processes):
    rr_sum += rr_waiting_time[i]
    rr_turn_sum += rr_turnaround_time[i]
print(f"average_waiting_time = {rr_sum/len(processes)},average_turnaround_time={rr_turn_sum/len(processes)}")

