from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # graph[i] 表示：
        # 学完 course i 之后，可以解锁哪些课程
        graph = [[] for _ in range(numCourses)]

        # indegree[i] 表示：
        # course i 还有几个前置课没完成
        indegree = [0] * numCourses

        # 遍历所有前置关系
        for course, prereq in prerequisites:
            # prereq -> course
            # 学完 prereq，可以解锁 course
            graph[prereq].append(course)

            # course 多了一个前置课 prereq
            indegree[course] += 1

        # dq 里面放当前可以直接学的课
        dq = deque()

        for i in range(numCourses):
            # 如果 course i 没有任何前置课
            if indegree[i] == 0:
                dq.append(i)

        # count 表示已经成功学掉几门课
        count = 0

        # 只要还有可以学的课
        while dq:
            # 取出一门当前可以学的课
            current = dq.popleft()
            # 学掉它
            count += 1

            next_courses = graph[current]
            for next_course in next_courses:
                # next_course 少了一个未完成前置课
                indegree[next_course] -= 1
                # 如果 next_course 的所有前置课都完成了
                if indegree[next_course] == 0:
                    dq.append(next_course)

        # finally, if all done we should have all zeros

        for i in indegree:
            print(i)
            if i != 0:
                return False

        return True