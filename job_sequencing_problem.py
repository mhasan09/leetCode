class Solution:
    def JobScheduling(self, jobs, n):
        jobs = sorted(jobs, key=lambda x:x[2], reverse=True)
        max_deadline = jobs[0][1]
        for i in range(n):
            max_deadline = max(max_deadline, jobs[i][1])
        slot = [-1] * max_deadline
        count_jobs, job_profit = 0, 0
        print(jobs)
        for i in range(len(jobs)):
            for j in range(jobs[i][1], 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    count_jobs += 1
                    job_profit += jobs[i][2]
                    break
        return count_jobs, job_profit


print(Solution().JobScheduling([(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)], 4))
