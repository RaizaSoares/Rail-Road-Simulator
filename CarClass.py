from soares_raiza import Strategycartypes
"""
/***********************************************************************
 * Class: Car
 * author: Raiza Soares
 * Description: The Car class. Handles the location and speed of a car 
 * based on behavior
 **********************************************************************/
"""
class Car:
    def __init__(self, idcar, l, b): #b is Subtype of CarType
        self.__id = idcar
        self.__loc = l
        self.__behavior = b
        self.__numcarstrack = None

    """
                /***********************************************************************
                 * function: str
                 * author: Raiza Soares
                 * Description: Overrides the str function and prints the car with desired formating
                **********************************************************************/

                """
    def __str__(self):
        return "{}: {:.2f}".format(self.__id, self.__loc)

    """
            /***********************************************************************
             * function: update
             * author: Raiza Soares
             * Description: Updates the location of the car
            **********************************************************************/

            """
    def update(self):
        self.__loc = self.__loc + self.__behavior.travel(self.__numcarstrack) * 0.50/60.00  # GRADING: USE_BEHAVIOR

    """
    /***********************************************************************
     * function: getLocation
     * author: Raiza Soares
     * Description: sends the location of the car
     **********************************************************************/

    """
    def getLocation(self):
        return self.__loc

    """
     /***********************************************************************
      * function: updatetozero
      * author: Raiza Soares
      * Description: changes the location of the car to 0.
      **********************************************************************/

     """
    def updatetozero(self):
        self.__loc = 0

    """
     /***********************************************************************
      * function: updatenumcars
      * author: Raiza Soares
      * Description: gets the number of other cars on the track
      **********************************************************************/

     """
    def updatenumcars(self, n):
        self.__numcarstrack = n
