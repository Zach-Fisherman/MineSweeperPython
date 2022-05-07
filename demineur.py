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
#
#
# First Coordinate is the Vertical axis, and second is the horizontal axis
class Field():
    """
    Class of the Minefield.
    ...
    Attributes
    ----------
    IsMine: Boolean
        Determine if the field is mined (default is False)
    IsRevealed: Boolean
        Determine if the Field has been revealed (default is False)
    IsFlagged: False
        Determine if the field has been flagged or not ( default is False)
    SurroundingMine Integer:
        How many mine are arround the Field (default is 0)

    Methods
    ----------
    ReturnInfo: []
        return the value contained in the Field class (IsMine,IsRevealed ,IsFlagged ,SurroundingMine)
    """
    def __init__(self):
        self.IsMine=False
        self.IsRevealed=False
        self.IsFlagged=False
        self.SurroundingMine=0

    def ReturnInfo(self):
        """
        Return the Field Values (debug feature)
        """
        return [self.IsMine,self.IsRevealed,self.IsFlagged,self.SurroundingMine]

class Minefield():
    """
    A Class used to generate a MineField
    ...
    Attributes
    ----------
    Size : Integer[]
        list wich tells how big the structure is
    NbrMine : integer
        an integer saying the number of mine on the minefield
    Minefield : Field[][]
        Two dimensional structure of Field

    Methods
    ----------
    PrintRevealedField()
        Prints the revealed field, used to debug the program

    PrintVisibleField()
        Print the field as the player can see it, with mine and flag

    IsOutOfBound(FCoord int[])
        Return whether the coordinate is out of bound ( if we are searching a mine outside the field)

    FillMinefield(FirstCase int[])
        place the mine in the minefield, the case arround the first click are not containing any mine

    IterRevealFieldZero(FCoord int[])
        Permit to iteratively reveal all case with 0 mine arround them, also reveal the case adjacent to them if. 
        return 0 to exit the program 
    
    RevealField(FCoord int[])
        Reveal the case asked by the user.
    """
    def __init__(self,Size,Difficulty):
        self.Size=Size
        self.NbrMine= int(Difficulty*Size[0]*Size[1])
        self.Minefield=[]
        for i in range(self.Size[0]):
            self.Minefield.append([])
            for j in range(self.Size[1]):
                self.Minefield[-1].append(Field())
        """
        Parameters
        ----------
        Size: Integer[]
            Dimension of the Minefield
        NbrMine: Integer
            Number of mine that are on the Minefield
        Minefield Field[][]:
            Two dimensional Field structure
        mine
        """

    def PrintRevealedField(self):
        InfoField=[]
        for i in range(self.Size[0]):
            for j in range(self.Size[1]):
                InfoField= self.Minefield[i][j].ReturnInfo()
                if InfoField[0]:
                    print("✹",end='')
                else:
                    print(str(InfoField[3]),end='')
                print("\t",end='')
            print()
        """
        Minefield Method printing a revealed field, permits to debug the program.
        """

    def PrintVisibleField(self):
        InfoField=[]
        for i in range(self.Size[0]):
            for j in range(self.Size[1]):
                InfoField= self.Minefield[i][j].ReturnInfo()
                if(InfoField[1]):
                    if InfoField[0]:
                        print("✹",end='')
                    else:
                        print(str(InfoField[3]),end='')
                else:
                    print("▢",end='')
                print("\t",end='')
            print()
        """
        Minefield Method printing a field, permits to play the game
        """

    def IsOutOfBound(self, FCoord):
        if (FCoord[0]<0 or FCoord[0]>=self.Size[0]) or (FCoord[1]<0 or FCoord[1]>=self.Size[1]):
                return True
        return False
        """
        Return whether the coordinate checked for is out of the minefield or not
        ...
        Parameters
        ----------
        FCoord: Integer[]
            Coordinate of the Field checked
        """

    def FillMinefield(self,FirstCase):
        def BlackListField(FCoord):
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
            FCoord: Integer[]
                Coordinate of the first revealed Field
            """

        def MineArround(FCoord):
            NbrMine=0
            for i in range(FCoord[0]-1,FCoord[0]+2):
                for j in range(FCoord[1]-1,FCoord[1]+2):
                    if not self.IsOutOfBound([i,j]):
                        if self.Minefield[i][j].IsMine:
                            NbrMine+=1
            return NbrMine
            """
            Return the number of mine arround the Field Checked
            ...
            Parameters
            ----------
            FCoord: Integer[]
                Coordinate of the Field Checked
            """
        def UpdateNbrMine():
            for i in range(self.Size[0]):
                for j in range(self.Size[1]):
                    if not self.Minefield[i][j].IsMine:
                        self.Minefield[i][j].SurroundingMine = MineArround([i,j])
            """
            Update the Field value field.SurroundingMine accross the Minefield structure table
            """

        PlacedMine =0
        BLMF = BlackListField(FirstCase)

        while self.NbrMine != PlacedMine:
            RandField= [r.randint(0,self.Size[0]-1),r.randint(0,self.Size[1]-1)]
            if RandField not in BLMF:
                if not self.Minefield[RandField[0]][RandField[1]].IsMine:
                    self.Minefield[RandField[0]][RandField[1]].IsMine = True
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

    def IterRevealFieldZero(self, FCoord):
        CoordA=FCoord[0]
        CoordB=FCoord[1]
        if self.IsOutOfBound(FCoord):
            return 0

        InfoField= self.Minefield[CoordA][CoordB].ReturnInfo()
        self.Minefield[CoordA][CoordB].IsRevealed=True

        if InfoField[3]!=0 or InfoField[1]:
            return 0
        else:
            for i in range(CoordA-1,CoordA+2):
                for j in range(CoordB-1,CoordB+2):
                    if not (i==CoordA and j==CoordB):
                        self.IterRevealFieldZero([i,j])
        """
        Permit to iteratively reveal all case with 0 mine arround them, also reveal the case adjacent to them if.
        We return 0 to exit the program
        ...
        Parameters
        ----------
        FirstCase: Integer[]
            a integer table of length 2, they are the coordinate of the fields wich is iteratively revealed
        """

    def RevealField(self,FCoord):
        CoordA=FCoord[0]
        CoordB=FCoord[1]
        InfoField= self.Minefield[CoordA][CoordB].ReturnInfo()
        if not InfoField[0]:
            if not InfoField[2]:
                if InfoField[3]!=0:
                    self.Minefield[CoordA][CoordB].IsRevealed = True
                else:
                    self.IterRevealFieldZero(FCoord)
            else:
                print("You flagged this field and it shall not be revealed until you unflag it")
        else:
            #end the game if a bomb is found
            self.PrintRevealedField()
            return False
        """
        ...
        Parameters
        ----------
        FirstCase: Integer[]
            a integer table of length 2, they are the coordinate of the first revealed case
        """

    def FlagField(self,coord):
        # This function is used to flag or unflag a field
    
    def IsVictory(self):
        # this function is used to verify if all mine have been found.

    def LaunchGameText(self):
        self.PrintRevealedField()
        CField= input("Choose the first case you ll reveal like this : A;B \n A is the vertical coordinate while B is the horizontal one").split(";")
        CField[0] = int(CField[0])
        CField[1] = int(CField[1])

        self.FillMinefield(CField)
        self.PrintRevealedField()

        #make function to verify if the Minefield is solved
        #make a function to flag a case
        #make a loop while to let


TestField = Minefield([10,10],0.2)
TestField.FillMinefield([3,5])
TestField.RevealField([3,5])
TestField.PrintVisibleField()
print()
TestField.PrintRevealedField()