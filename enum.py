# enum
class Multiplier(object):
	NONE = 0
	DOUBLE_LETTER = 1
	DOUBLE_WORD = 2
	TRIPLE_LETTER = 3
	TRIPLE_WORD = 4


class BoardPositionState(object):
	EMPTY = 0
	PENDING = 1
	FULL = 2


class ErrorCodes(object):
    SWAP = 0
