# python3
from collections import deque

def process_requests(buffer_size, n, requests):
    responses = [None]*n
    buffer = deque()  ######## [idx, finish_time]
    for idx, (arrived_at, time_to_process) in enumerate(requests) :
        while buffer and buffer[-1][1] <= arrived_at :
            buffer.pop()
        if len(buffer) < buffer_size :
            started_at = buffer[0][1] if buffer else arrived_at
            finish_time = started_at + time_to_process
            buffer.appendleft([idx, finish_time])
            responses[idx] = started_at
        else :
            responses[idx] = -1
    return responses

# buffer_size = 1
# n = 1
# requests = [(0,0)]
# print(process_requests(buffer_size, n, requests))

def main():
    buffer_size, n = map(int, input().split())
    requests = []
    for _ in range(n):
        arrived_at, time_to_process = map(int, input().split())
        requests.append((arrived_at, time_to_process))

    #buffer = Buffer(buffer_size)
    responses = process_requests(buffer_size, n, requests)

    for started_at in responses:
        print(started_at)


if __name__ == "__main__":
    main()





# python3
#
# from collections import namedtuple
#
# Request = namedtuple("Request", ["arrived_at", "time_to_process"])
# Response = namedtuple("Response", ["was_dropped", "started_at"])
#
#
# class Buffer:
#     def __init__(self, size):
#         self.size = size
#         self.finish_time = []
#
#     def process(self, request):
#         # write your code here
#         return Response(False, -1)
#
#
# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses
#
#
# def main():
#     buffer_size, n_requests = map(int, input().split())
#     requests = []
#     for _ in range(n_requests):
#         arrived_at, time_to_process = map(int, input().split())
#         requests.append(Request(arrived_at, time_to_process))
#
#     buffer = Buffer(buffer_size)
#     responses = process_requests(requests, buffer)
#
#     for response in responses:
#         print(response.started_at if not response.was_dropped else -1)
#
#
# if __name__ == "__main__":
#     main()
