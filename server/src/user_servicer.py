import user_pb2 as model
import user_pb2_grpc as service


class UserServicer(service.UserService):
    def __init__(self):
        ...

    def GetUser(self, request, context):
        match request.Id:
            case 1:
                return model.GetUserResponse(Name="taro")
            case 2:
                return model.GetUserResponse(Name="jiro")
            case _:
                return model.GetUserResponse(Name="not found")
