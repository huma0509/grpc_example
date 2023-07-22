using Api;
using Grpc.Core;

public class UserClient
{
    Api.UserService.UserServiceClient client;


    public UserClient(string ip = "localhost", int port = 50004)
    {
        var channel = new Channel($"{ip}:{port}", ChannelCredentials.Insecure);
        client = new Api.UserService.UserServiceClient(channel);
    }

    public void GetUser(int id)
    {
        var response = client.GetUser(new() { Id = id });
        Console.WriteLine(response.Name);
    }

}
