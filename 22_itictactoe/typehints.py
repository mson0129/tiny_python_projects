#!/usr/bin/env python3
""" Demonstrating type hints """

from typing import List, NamedTuple, Optional


class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False # quit은 type(bool)로 정의했으므로 True 또는 False 값만 허용해야 한다.
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


state = State(quit='False') # type(bool) 대신에 type(str) 'True'를 할당하고 있으며, 특히 규모가 큰 프로그램이라면 쉽게 실수할 수 있다. 이런 종류의 오류를 감지할 수 있게 해야 한다.

print(state)
