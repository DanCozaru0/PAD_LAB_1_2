import grpc
import asyncio
import publish_pb2
import publish_pb2_grpc

async def run():
    print("Publisher in Python (async)")

    # Se creează un canal pentru a comunica cu brokerul (asincron)
    async with grpc.aio.insecure_channel('127.0.0.1:5001') as channel:
        client = publish_pb2_grpc.PublisherStub(channel)

        while True:
            # Citește topic și content de la utilizator
            topic = input("Enter topic: ").lower()
            content = input("Enter content: ")
            
            print("Simulating heavy processing...")
            await asyncio.sleep(5)
            # Creează request-ul pentru a publica mesajul
            request = publish_pb2.PublishRequest(topic=topic, content='(.fromPy) ' + content)

            try:
                # Trimite request-ul la broker și așteaptă răspunsul (asincron)
                reply = await client.PublishMessage(request)
                print(f"Publish reply: {reply.isSuccess}")
            except Exception as e:
                print(f"Error publishing the message: {e}")

if __name__ == '__main__':
    # Rulează funcția asincronă principală folosind asyncio
    asyncio.run(run())
