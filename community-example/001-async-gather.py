import asyncio

async def bar(i):
  print('started', i)
  await asyncio.sleep(1)
  print('finished', i)

async def main():
  await asyncio.gather(*[bar(i) for i in range(10)])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()