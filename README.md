# Rail-Road-Simulator
Used Python's inbuilt iterator support and strategy pattern to simulate the working of a train line. 
 The MainStarter class has main in it that runs the whole program.
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
