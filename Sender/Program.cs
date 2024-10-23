using Common;
using Grpc.Net.Client;
using GrpcAgent;

namespace Sender
{
    internal class Program
    {
        static async Task Main(string[] args)
        {
            Console.WriteLine("Publisher");

            var channel = GrpcChannel.ForAddress(EndpointsConstants.BrokerAddress);
            var client = new Publisher.PublisherClient(channel);

            while (true)
            {
                Console.Write("Enter topic: ");
                var topic = Console.ReadLine().ToLower();

                Console.Write("Enter content: ");
                var content = Console.ReadLine();

                var request = new PublishRequest() { Topic = topic, Content = content };

                try
                {
                    var reply = await client.PublishMessageAsync(request);
                    Console.WriteLine($"Publish reply: {reply.IsSuccess}");
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Error publishing the message. {e.Message}");
                }
            }

        }
    }
}
