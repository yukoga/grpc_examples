import grpc
import user_service_pb2
import user_service_pb2_grpc
import order_service_pb2
import order_service_pb2_grpc


def get_user_info(user_id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        request = user_service_pb2.UserRequest(user_id=user_id)
        response = stub.GetUser(request)
        return response


def get_order_info(user_id):
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = order_service_pb2_grpc.OrderServiceStub(channel)
        request = order_service_pb2.OrderRequest(user_id=user_id)
        response = stub.GetOrder(request)
        return response


def run():
    user_id = input('Enter user_id: ')
    user_info = get_user_info(user_id)
    order_info = get_order_info(user_id)
    print('User Info: ', user_info)
    print('Order Info: ', order_info)


if __name__ == '__main__':
    run()
