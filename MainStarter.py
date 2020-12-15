"""
*@file
 *
 *@brief The MainStarter class has main in it that runs the whole program.
 * You are able to do 6 things with the train line as detailed in the
 * description below.
 *
 * @author  Raiza Soares
 * @mainpage Program - Python
 *
 * @description The program starts with displaying the menu. The user can
 * choose from the following options:
 *          1) Show Train Line
 *          2) Add Train Car
 *          3) Update with Debug Info
 *          4) Show Station Details
 *          5) Make Test Line
 *          6) Make Custom Line
 *          0) Quit
 * 1) Displays the train line at that point in time. Implemented using
 * the strategy pattern. 2) Adds a cautious, normal, or rushhour
 * car to the start station. The different behaviors of the cars were
 * implemented using the strategy pattern. 3) Updates the location of
 * the cars depending on their speed and the station they are at. The order
 * of updates occurs in only one direction. 4) Displays only station
 * information. 5) Adds on a station with release time 1.5 to the current
 * line. 6) Make a new line and replace the old one with it. Add on
 * as many stations as needed.
 *
 * @KnownBugs None
 *
 * @To_Do None
 *
 * Note: Use original set of tests
"""

from soares_raiza import Line
from soares_raiza import Strategycartypes
from soares_raiza import Timestation
from soares_raiza import StationClass
"""
/***********************************************************************
     * Class: Main
     * author: Raiza Soares
     * Description: Has a meu that a user can pick from and does
     * specific tasks based on the options chosen. Always reprints the menu
     * until the user quits the program. Handles bad input.
     **********************************************************************/
"""
def main():
    menu = "\n" \
           "1) Show Train Line\n" \
           "2) Add Train Car\n" \
           "3) Update with Debug Info\n" \
           "4) Show Station Details\n" \
           "5) Make Test Line \n" \
           "6) Make Custom Line \n" \
           "0) Quit\n"

    templine = Line.L()

    choice = -1

    while choice != 0:
        print(menu)
        stopmins = ""
        try:
            choice = input("Choice: ")

            # strips out blank lines in input
            while choice == '':
                choice = input()

            if choice == '1':
                templine.prints()
                for i in templine:  # GRADING: LOOP_ALL
                    print(i)

            elif choice == '2':
                carType = input("Which type: 0-->Cautious, 1-->Normal, 2-->Rush hour: ")
                if carType.isnumeric() and int(carType) < 3 and int(carType) >= 0:
                    # GRADING: SET_BEHAVIOR
                    if carType == '0':
                        c = Strategycartypes.Cautious()
                    elif carType == '1':
                        c = Strategycartypes.Normal()
                    else:
                        c = Strategycartypes.Rushhour()
                    templine.addcar(c)
                else:
                    print("Invalid Option")

            elif choice == '3':
                templine.update()
                templine.printtime()
                for i in templine:
                    print(i)

            elif choice == '4':
                for i in templine.callStationIter():  # GRADING: LOOP_STATION
                    print(i)

            elif choice == '5':
                statone = Timestation.TimeSt("1", 1.5)
                templine.addStation(statone)


            elif choice == '6':
                templine = Line.L()
                print("Number of stations: ")
                numstations = input()
                if numstations.isnumeric():
                    for i in range(int(numstations)):
                        print("----Station " + str(i + 1) + "----\n   Length of stop time in minutes: ", end="")
                        stopmins = input()
                        stopmins= float(stopmins)
                        if stopmins > 0 and stopmins % 0.5 == 0:
                            if i != int(numstations) - 1:
                                n = input("   Name of station: \n")
                            else:
                                n = input("   Name of station: ")
                            templine.addStation(Timestation.TimeSt(n, stopmins))
                        else:
                            print("Stop time must be positive and an increment of 0.5 min. Got: " + str(stopmins))

                else:
                    print("Invalid Option")

            elif choice == '0':
                choice = 0
            else:
                print("Invalid Option")

        except ValueError:
            print("Stop time must be a number. Got: " + str(stopmins))


if __name__ == '__main__':
    main()


