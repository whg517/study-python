from aiodocker import Docker


async def list_images():
    client = Docker()
    client.images.list()
