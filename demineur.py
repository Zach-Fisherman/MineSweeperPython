from tkinter import *
from math import *
import random as r

# Specification of a MineField :
# A MineField is a two-dimensional Field structure of size AxB
#  A Field is a structure wich contains:
#   Boolean IsMine : determine whether the Field is a mine or not
#   Boolean IsRevealed : Determine whether the Field has been revealed or not.
#   Integer SurroundingMine : determine how many mine are arround the Field.
# Float Difficulty: value between 0.0 and 1.0 determining the percentage of mine
# The total ammount of mine on a MineField is determined by doing floor(float(A*B)*C)
# The Player must find every Mine on the terrain
# To do so, the player has two tools:
#  Reveal: will reveal the case
#   If the case is a mine, the game end and all field are revealed ( bombs are symbolized by "✹")
#   If there is no mine arround the case, a function Reveal all case arround it iteratively until they arrive to a case adjacent to a mine.
#   Else, the number of mine arround that Field is revealed
#
#  "⚑": Permit to flag a Field as a supposed Mine
#
# Optional :
# Adding a time to see how fast a game of MineSweeper is solved
# Make it so the first click done by the Player nor the Fields arround to it can be mine.
class Field:
    """
    Class of the Minefield.
    ...
    Attributes
    ----------
    IsMine: Boolean
        Determine if the field is mined (default is False)
    IsRevealed: Boolean
        Determine if the Field has been revealed (default is False)
    SurroundingMine Integer:
        How many mine are arround the Field (default is 0)

    Methods
    ----------
    ReturnInfo: []
        return the value contained in the Field class
    """
    def __init__(self):
        self.IsMine=False
        self.IsRevealed=False
        self.SurroundingMine=0

    def ReturnInfo(self):
        """
        Return the Field Values (debug feature)
        """
        return [self.IsMine,self.IsRevealed,self.SurroundingMine]

class Minefield():
    """
    A Class used to generate a MineField
    ...
    Attributes
    ----------
    size : Integer[]
        list wich tells how big the structure is
    difficulty : float
        a float used to determine the number of mine on the MineField
    struct : Field[][]
        Two dimensional structure of Field

    Methods
    ----------
    PrintRevealedField()
        Prints the revealed field, used to debug the program

    fillMinefield(FirstCase int[])
        place the mine in the minefield, the case arround the first click are not containing any mine

    """
    def __init__(self,size,difficulty):
        self.size=size
        self.difficulty=difficulty
        self.minefield=[]
        for i in range(self.size[0]):
            self.minefield.append([])
            for j in range(self.size[1]):
                self.minefield[-1].append(Field())
        """
        Parameters
        ----------
        size: Integer[]
            Dimension of the MineField
        difficulty: Float
            Float used to determine the number of Mine on a minefield
        minefield Field[][]:
            Two dimensional Field structure
        """

    def fillMinefield(self,FirstCase):
        def BlackListField(FC):
            # Start by defining wich case we don't put bomb in
            # No need to exempt case that are out of bound, since there is no way for the program to look field that are out of bound
            # BL_Mine (Blacklist Mine) will be the table containing the list of field wich can't have mine
            BLMinefield =[]
            BLField=[]
            for i in range(FirstCase[0]-1,FirstCase[0]+2):
                for j in range(FirstCase[1]-1,FirstCase[1]+2):
                    BLField.append(i)
                    BLField.append(j)
                    BLMinefield.append(BLField)
                    BLField=[]
            return BLMinefield
            """
            Return a List of Field that can't contain a mine
            ...
            Parameters
            ----------
            FC: Integer[]
                Coordinate of the first revealed Field
            """

        def IsOutOfBound(FC):
            if (FC[0]<0 or FC[0]>self.size[0]) or (FC[1]<0 or FC[1]>self.size[1]):
                    return True
            return False
            """
            Return whether the coordinate checked for is out of the minefield or not
            ...
            Parameters
            ----------
            FC: Integer[]
                Coordinate of the Field checked
            """
        def MineArround(FC):
            NbrMine=0
            for i in range(FC[0]-1,FC[0]+2):
                for j in range(FC[1]-1,FC[1]+2):
                    if not IsOutOfBound([i,j]):
                        if self.minefield[i][j].IsMine:
                            NbrMine+=1
            return NbrMine
            """
            Return the number of mine arround the Field Checked
            ...
            Parameters
            ----------
            FC: Integer[]
                Coordinate of the Field Checked
            """
        def UpdateNbrMine():
            for i in range(self.size[0]-1):
                for j in range(self.size[1]-1):
                    if not self.minefield[i][j].IsMine:
                        self.minefield[i][j].SurroundingMine = MineArround([i,j])
            """
            Update the Field value field.SurroundingMine accross the Minefield structure table
            """

        NbrMine = int(ceil(self.difficulty*(self.size[0]*self.size[1])))
        PlacedMine =0
        BLMF = BlackListField(FirstCase)

        while NbrMine != PlacedMine:
            RandField= [r.randint(0,self.size[0]-1),r.randint(0,self.size[1]-1)]
            if RandField not in BLMF:
                if not self.minefield[RandField[0]][RandField[1]].IsMine:
                    self.minefield[RandField[0]][RandField[1]].IsMine = True
                    PlacedMine+=1

        UpdateNbrMine()

        """
        Place the mine in the MineField
        ...
        Parameters
        ----------
        FirstCase: Integer[]
            a integer table of length 2, they are the coordinate of the first revealed case

        Methods
        ----------
        BlackListField: Integer [][]
            Return a List of Field that can't contain a mine

        IsOutOfBound: Boolean
            Return whether the coordinate checked for is out of the minefield or not

        MineArround: Integer
            Return the number of mine arround the Field Checked

        UpdateNbrMine: None
            Update the Field value field.SurroundingMine accross the Minefield structure table
        """

    def printRevealedField(self):
        infoField=[]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                infoField= self.minefield[i][j].ReturnInfo()
                if infoField[0]:
                    print("✹",end='')
                else:
                    print(str(infoField[2]),end='')
                print("\t",end='')
            print()
        """
        Minefield Method printing a revealed field, permits to debug the program.
        """




TestField = Minefield([10,10],0.2)
TestField.fillMinefield([3,5])
TestField.printRevealedField()

# #Create & Configure root
# root = Tk()
# Grid.rowconfigure(root, 0, weight=1)
# Grid.columnconfigure(root, 0, weight=1)
#
# #Create & Configure frame
# frame=Frame(root)
# frame.grid(row=0, column=0, sticky=N+S+E+W)
#
# #Create Style
# style = ttk.Style()
# style.map("C.FieldButton",
#     )
#
# #Create a 5x10 (rows x columns) grid of buttons inside the frame
# for row_index in range(10):
#     Grid.rowconfigure(frame, row_index, weight=1)
#     for col_index in range(10):
#         Grid.columnconfigure(frame, col_index, weight=1)
#         btn = Button(padding=) #create a button inside frame
#         btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)
#
# root.mainloop()