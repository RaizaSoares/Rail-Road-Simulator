"""
/***********************************************************************
 * Class: CarType
 * author: Raiza Soares
 * Description: Handles the different car types based on the strategy pattern
 **********************************************************************/
"""


class CarType:

    def travel(self, count):
        pass


"""
/***********************************************************************
 * Class: Cautious
 * author: Raiza Soares
 * Description: Overrides travel and sets the speed of the car based 
 * on the number of other cars in the track.
 **********************************************************************/
"""


class Cautious(CarType):  # GRADING: CAUTIOUS
    def travel(self, count):
        if count >= 1:
            return 30 - 10
        else:
            return 30


"""
/***********************************************************************
 * Class: Normal
 * author: Raiza Soares
 * Description: Overrides travel and sets the speed of the car based 
 * on the number of other cars in the track.
 **********************************************************************/
"""


class Normal(CarType):  # GRADING: NORM
    def travel(self, count):
        if count >= 2:
            return 30 - 10
        else:
            return 30


"""
/***********************************************************************
 * Class: Cautious
 * author: Raiza Soares
 * Description: Returns speed limit no matter what.
 **********************************************************************/
"""


class Rushhour(CarType):  # GRADING: RUSH
    def travel(self, count):
        return 30
