from concurrent import futures
import grpc
import user_service_pb2
import user_service_pb2_grpc

class UserService(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        user_id = request.user_id
        if user_id == "123":
            return user_service_pb2.UserResponse(user_id=request.user_id, user_name="Alice", user_email="alice@example.com")
        # else:
        #     return user_service_pb2.UserResponse(user_id=request.user_id, user_name="Unknown", user_email="")
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found!')
            return user_service_pb2.UserResponse(user_id=request.user_id, user_name="Unknown")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
