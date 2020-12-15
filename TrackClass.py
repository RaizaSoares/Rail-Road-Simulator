from soares_raiza import CarClass
from soares_raiza import StationClass

"""
/***********************************************************************
 * Class: Track
 * author: Raiza Soares
 * Description: The Station track. Hnadles the cars in the track
 **********************************************************************/
"""
class Track:

    def __init__(self, l, s):
        self.__length = l
        self.__speed = s
        self.__carlist = list()
        self.__loccupied = 0
        self.__trackfull= False
        self.__left = None
        self.__right = None
        self.__carCurr= None

    """
                /***********************************************************************
                 * function: str
                 * author: Raiza Soares
                 * Description: Overrides the str function and prints the cars in track
                **********************************************************************/

                """
    def __str__(self):
        emp = "    "
        for i in self.__carlist:
            emp += "{:10}".format(str(i) )
        return emp

    """
            /***********************************************************************
             * function: setRandL
             * author: Raiza Soares
             * Description: Sets the left and right station
            **********************************************************************/

            """
    def setRandL(self, l, r):
        self.__left = l
        self.__right = r

    """
        /***********************************************************************
         * function: update
         * author: Raiza Soares
         * input: direction
         * Description: Puts the car in the next station if the location of the
         * car goes over the track length.
        **********************************************************************/

        """
    def update(self, direction):
        for i in self.__carlist:
            i.updatenumcars(len(self.__carlist) - 1)
            i.update()

        temp = []
        if self.__carlist:

            for j in self.__carlist:
                if self.__carlist and j.getLocation() >= 0.75:  # check to see if its over 0.75
                    c = j
                    temp.append(j)
                    c.updatetozero()
                    if direction == "RIGHT":
                        if self.__right is not None:
                            self.__right.addcartost(c)
                    else:
                        if self.__left is not None:
                            self.__left.addcartost(c)

            for j in temp:
                self.__carlist.remove(j)

    """
            /***********************************************************************
             * function: addcartotrack
             * author: Raiza Soares
             * Description: Puts a car into the track list
            **********************************************************************/

            """
    def addcartotrack(self, c):
        self.__carlist.append(c)




