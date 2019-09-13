class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """

        #return obvious cases
        if len(self._list) == 0 or len(self._list) == 1:
            return self._list

        #################### Optimization - Stretch #########################################
        #    Check and resolve case where list is  reverse sorted     #
        #   Rotate all items (circular) untils all items are sorted - return the list
        #
        #   side effects if items are not reverse sorted:    
        #   worst case: 2nd card is greater than first card-> no change in list
        #   average case: partially reverse sorted at the beginning-> will get closer to a sorted list
        #   in both case Bubble sort will take over next, possibly starting from a better sorted list
        
        #################### Optimization ####################################################
        
        #light on: Will assume that list is reverse sorted from here
        self.set_light_on()

        while(self.light_is_on()):

            while self.can_move_right():
                self.swap_item()
                self.move_right()

                #This is the last swap
                if not self.can_move_right():
                
                    #2 last items were not reverse sorted = keep that order
                    if(self.compare_item() == -1):
                        self.move_left()
                        self.swap_item()

                    #sort last two items  
                    else:
                        self.swap_item()
                        self.move_left()
                        self.swap_item()
                    
                    return self._list

                #signals a situation where this is not reverse sorted - exit loop
                if(self.compare_item() == -1):

                    #will stop the optimization phase
                    self.set_light_off()
                    break
                else:
                    self.swap_item()

            
            #return item on hand to an empty spot to the left
            #case1: have reached the end of the list - rotating last element to beginning of the pass   
            #case2: Met case where not reverse sorted - return item on hand right to the left where it came from
            while True:
                self.move_left()
                if self.compare_item() == None:
                    self.swap_item()
                    break

                    
        ################################################################################
        #          End of Optimization Code - Start Bubble sort next                   #
        ################################################################################

        self.set_light_on()

        #light on: While there were swaps in the previous pass
        while(self.light_is_on()):

            
            #start with signaling that we have not done any swaps yet for this coming pass
            self.set_light_off()

            #if at end of list move back to beginning
            while(self.can_move_left()):
                self.move_left()

            #while not at end of list move right
            while(self.can_move_right()):

                #grab current card
                self.swap_item()

                #move right
                self.move_right()

                #swap if card on hand is greater than card in the front
                if(self.compare_item() == 1):
                    self.swap_item()

                    #signals swaps have occurred
                    self.set_light_on()

                #move back left
                self.move_left()

                #place at this location the card that was there previously or card that was swapped on the right
                self.swap_item()

                self.move_right()

        return self._list

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)