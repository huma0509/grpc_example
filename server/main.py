from src.user_pb2_grpc import add_UserServiceServicer_to_server
from src.user_servicer import UserServicer
from concurrent import futures
import grpc

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

add_UserServiceServicer_to_server(UserServicer(), server)
server.add_insecure_port('localhost:50004')
server.start()
print('server started')
server.wait_for_termination()
