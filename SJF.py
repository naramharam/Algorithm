def findWaitingTime(processes, n, bt, wt):

    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def findavgTime(processes, n, bt):
    wt = [0] * n
    total_wt = 0

    findWaitingTime(processes, n, bt, wt)

    print("Processes Burst time " + " Waiting time ")

    for i in range(n):
        total_wt = total_wt + wt[i]
        print(" " + str(i + 1) + "\t\t\t" +
              str(bt[i]) + "\t\t\t " +
              str(wt[i]))

    print(" Total waiting time = " + str(total_wt))
    print("Average waiting time = " + str(total_wt / n))


if __name__ == "__main__":
    processes = [1, 2, 3]
    n = len(processes)

    burst_time = [15, 9, 11]
    findavgTime(processes, n, burst_time)