from soares_raiza import StationClass
from soares_raiza import TrackClass
from soares_raiza import Timestation
from soares_raiza import CarClass

"""
/***********************************************************************
 * Class: L
 * author: Raiza Soares
 * Description: The L class is the Line Class in the program. This class
 * has a nested iterator class. 
 **********************************************************************/
"""
class L:
    id = 0

    """
    /***********************************************************************
     * function: Init
     * author: Raiza Soares
     * Description: constructor- creates start and end station, and the track in 
     * between. Sets default direction to RIGHT
     **********************************************************************/
    """

    def __init__(self):
        self.__startSt = StationClass.Station("Start")
        self.__endSt = StationClass.Station("End")
        self.__startTrack = TrackClass.Track(0.75, 0.5)
        self.__time = 0
        self.__CarCount = 0
        self.__Direction = "RIGHT"
        self.__LineList = [self.__startSt, self.__startTrack, self.__endSt]
        self.setUpconnections()

    """
    /***********************************************************************
         * function: addStation
         * author: Raiza Soares
         * Description: Makes a new station and adjacent track 
         * and adds them in the right place in Linelist.
         **********************************************************************/
    """

    def addStation(self, st):
        le = len(self.__LineList)
        temp1 = self.__LineList.pop(le - 1)
        self.__LineList.append(st)
        tr = TrackClass.Track(0.75, 0.5)
        self.__LineList.append(tr)
        self.__LineList.append(temp1)
        self.setUpconnections()
    """
    /***********************************************************************
         * function: setUpconnections
         * author: Raiza Soares
         * Description: Sets the correct adjacent stations and tracks for each
         * station or track in line list.
         **********************************************************************/
        
    """
    def setUpconnections(self):
        for i in range(len(self.__LineList)):
            if i == 0:
                self.__LineList[i].setRandL(None, self.__LineList[i+1])
            elif i == len(self.__LineList) -1:
                self.__LineList[i].setRandL(self.__LineList[i - 1], None)
            else:
                self.__LineList[i].setRandL(self.__LineList[i-1], self.__LineList[i + 1])
    """
    /***********************************************************************
         * function: prints
         * author: Raiza Soares
         * Description: Helper to print line
         **********************************************************************/
        
    """
    def prints(self):
        starting = "-----------------------------------\n"
        print("Time: " + str(self.__time) + " min")
        print("Count: " + str(self.__CarCount) + " Direction: " + str(self.__Direction))
        print(starting, end="")

    """
        /***********************************************************************
             * function: addcar
             * author: Raiza Soares
             * input: Behavior type of car
             * Description: Calls startstartion's add car so that the car can be 
             * added on to the start station
             **********************************************************************/

        """
    def addcar(self, ty):
        self.__CarCount = self.__CarCount + 1
        L.id = L.id + 1
        self.__startSt.addcar(ty, 0, L.id)

    """
        /***********************************************************************
             * function: printtime
             * author: Raiza Soares
             * Description: Helper to print time
             **********************************************************************/

    """
    def printtime(self):
        print("Time:  " + str(self.__time))

    """
        /***********************************************************************
             * function: update
             * author: Raiza Soares
             * Description: Calls the corresponding update on each of the stations
             * and tracks in order, starting at Start station. 
             **********************************************************************/

        """
    def update(self):
        self.__time = self.__time + 0.5
        for i in self.__LineList:
            i.update(self.__Direction)
        if self.__Direction == "RIGHT":
            if self.__LineList[len(self.__LineList) - 1].getcarcountst() == self.__CarCount:
                self.__Direction = "LEFT"
        else:
            if self.__LineList[0].getcarcountst() == self.__CarCount:
                self.__Direction = "RIGHT"

    """
        /***********************************************************************
             * function: iter
             * author: Raiza Soares
             * Description: iterator for the LineList
             **********************************************************************/

        """
    def __iter__(self):  # GRADING: INTER_ALL
        self.__index = -1
        return self

    def __next__(self):
        try:
            self.__index += 1
            return self.__LineList[self.__index]
        except:
            raise StopIteration()

    """
        /***********************************************************************
             * function: callStationIter
             * author: Raiza Soares
             * Description: Calls the nested class iterator
             **********************************************************************/

        """
    def callStationIter(self):
        return self.StationIter(2, self.__LineList)

    """
    /***********************************************************************
    * Class: StationIter
    * author: Raiza Soares
    * Description: Nested class to print out only stations.
    **********************************************************************/

        """
    class StationIter:
        def __init__(self, skip, array):
            self.__skip = skip
            self.__array = array

        # same as before
        def __iter__(self):  # GRADING: INTER_STATION
            self.__index = -2
            return self

        # same as before
        def __next__(self):
            try:
                self.__index += self.__skip  # equivalent to next()
                return self.__array[self.__index]  # equivalent to get()
            except:
                raise StopIteration()







