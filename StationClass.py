from soares_raiza import CarClass
from soares_raiza import TrackClass

"""
/***********************************************************************
 * Class: Station
 * author: Raiza Soares
 * Description: The Station class. Hnadles the cars in the stations
 **********************************************************************/
"""


class Station:

    def __init__(self, n):
        self._name = n
        self._carlist = list()
        self.__nofurthertrack = False
        self.__carCurr = None
        self._left = None
        self._right = None

    """
            /***********************************************************************
                 * function: addcar
                 * author: Raiza Soares
                 * input: Behavior type of car, location of car, id of car
                 * Description: add's car to start station's list
                 **********************************************************************/

            """
    def addcar(self, ty, loc,  carid):
        newCar = CarClass.Car(carid, loc, ty)
        self._carlist.append(newCar)

    """
            /***********************************************************************
             * function: str
             * author: Raiza Soares
             * Description: Overrides the str function and prints the cars in station
            **********************************************************************/

            """
    def __str__(self):
        print("----Station: " + self._name + "---- Cars:", end=" ")
        emp = ""
        for i in self._carlist:
            emp += "{:11}".format(str(i))
        return emp

    """
        /***********************************************************************
         * function: setRandL
         * author: Raiza Soares
         * Description: Sets the left and right track
        **********************************************************************/

        """

    def setRandL(self, l, r):
        self._left = l
        self._right = r

    """
        /***********************************************************************
         * function: update
         * author: Raiza Soares
         * input: direction
         * Description: Puts the car in the next track if there is a next track
         * else does nothing.
        **********************************************************************/

        """
    def update(self, direction):
        if self._carlist:
            c = self._carlist[0]
            if direction == "RIGHT":
                if self._right is not None:
                    c = self._carlist.pop(0)
                    self._right.addcartotrack(c)
            else:
                if self._left is not None:
                    c = self._carlist.pop(0)
                    self._left.addcartotrack(c)

    """
        /***********************************************************************
         * function: addcartost
         * author: Raiza Soares
         * Description: Puts a car into the station list
        **********************************************************************/

        """
    def addcartost(self, c):
        self._carlist.append(c)

    """
        /***********************************************************************
         * function: getcarcountst
         * author: Raiza Soares
         * Description: returns how many cars there are in the station
        **********************************************************************/

        """

    def getcarcountst(self):
        return len(self._carlist)

