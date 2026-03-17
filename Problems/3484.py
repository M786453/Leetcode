import re
from copy import copy

class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.ss = [list([0])*26 for _ in range(rows)]

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        
        cell_row, cell_col = self.getCellCords(cell)
        
        self.ss[cell_row][cell_col] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """

        cell_row, cell_col = self.getCellCords(cell)
        
        self.ss[cell_row][cell_col] = 0
        

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """

        x,y = formula[1:].split("+")

        x_cords, y_cords = self.getCellCords(x), self.getCellCords(y)

        print(x_cords, y_cords)

        if x_cords:

            x_row, x_col = x_cords

            x = self.ss[x_row][x_col]
        
        if y_cords:

            y_row, y_col = y_cords

            y = self.ss[y_row][y_col]

        print(self.ss[168])
        print()
        print(self.ss[293])

        print(x,y)

        return int(x) + int(y)

    def getCellCords(self, cell):

        cell_col = re.match('\D',cell)

        if cell_col:
            cell_col = int(ord(cell_col.group())-65)
            cell_row = int(cell[1:])-1
            return (cell_row, cell_col)
        
        return None
        


# Your Spreadsheet object will be instantiated and called as such:
obj = Spreadsheet(657)
print(obj.setCell("U558",17217))
print(obj.getValue("=59437+H286"))
print(obj.setCell("C164",67231))
print(obj.setCell("Y294",75466))
print(obj.getValue("=Y169+Y294"))
print(obj.resetCell("F154"))
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)