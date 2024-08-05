#!/usr/bin/env python3
"""tasks"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Args:
            max_delay: max wait
            n: spawn function
        Return:
            multiles tasks
    """
    delays: List[float] = []
    orderList: List[float] = []

    for i in range(n):
        delays.append(task_wait_random(max_delay))

    for o in asyncio.as_completed(delays):
        orderList.append(await o)

    return orderList
