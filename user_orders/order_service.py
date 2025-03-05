from concurrent import futures
import grpc
import order_service_pb2
import order_service_pb2_grpc


class OrderService(order_service_pb2_grpc.OrderServiceServicer):
    def GetOrder(self, request, context):
        if request.user_id == "123":
            return order_service_pb2.OrderResponse(order_id="order123", user_id=request.user_id, product_name="Book", quantity=1)
        else:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid user ID")
            return order_service_pb2.OrderResponse(user_id=request.user_id)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_service_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
