class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.Xrow = defaultdict(int)
        self.Xcol = defaultdict(int)
        self.Orow = defaultdict(int)
        self.Ocol = defaultdict(int)
        self.DiaL = defaultdict(int)
        self.DiaR = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = self.n
        if player == 1:
            self.Xrow[row] += 1
            self.Xcol[col] += 1
            if row == col:
                self.DiaL[1] += 1
            if row == n - 1 - col:
                self.DiaR[1] += 1
            if self.Xrow[row] == n or self.Xcol[col] == n or self.DiaL[1] == n or self.DiaR[1] == n:
                return 1
            return 0
        else:
            self.Orow[row] += 1
            self.Ocol[col] += 1
            if row == col:
                self.DiaL[2] += 1
            if row == n - 1 - col:
                self.DiaR[2] += 1
            if self.Orow[row] == n or self.Ocol[col] == n or self.DiaL[2] == n or self.DiaR[2] == n:
                return 2
            return 0










