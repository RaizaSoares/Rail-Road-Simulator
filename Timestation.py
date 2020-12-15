from soares_raiza import StationClass

"""
/***********************************************************************
 * Class: TimeSt
 * author: Raiza Soares
 * Description: The time station derives from station. Constructor.
 **********************************************************************/
"""


class TimeSt(StationClass.Station):
    def __init__(self, n, time):
        super().__init__(n)
        self.__time = time
        self.__currTime = time

    """
    /***********************************************************************
     * function: update
     * author: Raiza Soares
     * Description: Puts the car in the next track if the timer has run out
     * resets the timer everytime a car leaves.
    **********************************************************************/

    """
    def update(self, direction):
        if self._carlist:
            if self.__currTime > 0.5:
                self.__currTime = self.__currTime - 0.5  # subtract the time by 0.5
            else:                                         # If the time is less that 0.5, pop the car
                self.__currTime = self.__time
                c = self._carlist.pop(0)
                if direction == "RIGHT":
                    if self._right is not None:             # Add the popped car to the track depending on direction
                        self._right.addcartotrack(c)
                else:
                    if self._left is not None:
                        self._left.addcartotrack(c)

    """
        /***********************************************************************
         * function: str
         * author: Raiza Soares
         * Description: Overrides the str function in station class and prints 
         * the cars in time station
        **********************************************************************/

        """
    def __str__(self):
        print("----Station: " + self._name + "---- Cars:", end=" ")
        m = "<<-release: " + str(self.__currTime)
        emp = ""
        for i in self._carlist:
            emp += "{:11}".format(str(i))
        emp = emp + m
        return emp