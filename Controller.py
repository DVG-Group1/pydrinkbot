import asyncio
import queue

# TODO: drink config file
# TODO: GPIO pin config


async def asyncPin(pin, delay):
    """
    open the pin, then use non-blocking sleep to wait for specified time
    then deactivate pin

    delay -- the time to leave the pin open in seconds
    """
    print('activating pin {}'.format(pin))
    await asyncio.sleep(delay)
    print('deactivating pin {}'.format(pin))
    return


async def make(drinkPins):
    # creates tasks for each of the pins in the recipe, then executes the loop
    pins = drinkPins
    tasks = []
    for pin in pins:
        task = asyncio.ensure_future(asyncPin(*pin))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print('Drink Done!')
    return


def makeNext(drinkQueue):
    # pulls next drink in queue and calls make()
    if not drinkQueue.empty():
        drink = drinkQueue.get()
        print('Now making "{}"...'.format(drink['name']))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(make(drink['pins']))
        loop.close()
    else:
        print('Oops! There aren\'t any drinks in the queue!')


if __name__ == '__main__':

    drink = {
        'pins': [
            (1, 8),
            (2, 5),
            (8, 3)
        ],
        'name': 'some_drink'
    }
    drinkQueue = queue.Queue()
    drinkQueue.put(drink)
    makeNext(drinkQueue)
