#from tkinter import *

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
    """
    def __init__(self,size,difficulty):
        self.size=size
        self.difficulty=difficulty
        self.struct=[]
        for i in range(self.size[0]):
            self.struct.append([])
            for j in range(self.size[1]):
                self.struct[-1].append(self.Field())

        """
        Parameters
        ----------
        size= Integer[]
            Dimension of the MineField
        difficulty = Float
            Float used to determine the number of Mine on a minefield
        """

    class Field:
        """
        Inner Class of the Minefield.
        ...
        Attributes
        ----------
        IsMine : Boolean
            Determine if the field is mined (default is False)
        IsRevealed : Boolean
            Determine if the Field has been revealed (default is False)
        SurroundingMine Integer:
            How many mine are arround the Field (default is 0)
        """
        def __init__(self):
            self.IsMine=False
            self.IsRevealed=False
            self.SurroundingMine=0

        def ReturnIsMine(self):
            """
            Return the Field Values (debug feature)
            """
            return [self.IsMine,seld,IsRevealed,self.SurroundingMine]


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