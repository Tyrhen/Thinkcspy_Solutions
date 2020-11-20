""" Chapter 15 Workthrough 'How to think like a CS'"""

from unit_tester import test

# P1 - P4
class point(object):
    """ creats x,y coordinates to represent a point in space with various functionality associated with point objects"""

    def __init__(self, x=0, y=0):
        """intitializes the x and y coordinates of a point value"""
        self.x = x
        self.y = y

    def __eq__(self, testpoint):
        """sets up how point values behave in equalities"""
        return (self.x == testpoint.x) == (self.y == testpoint.y)

    def __str__(self):
        """format how point values are printed"""
        return "{0},{1}".format(self.x, self.y)

    def reflect_x(self):
        """reflect point object across the x-axis"""
        if self.x > 0:
            self.x = -1 * self.x
        else:
            self.x = abs(self.x)
        return point(self.x, self.y)

    def slope_from_origin(self):
        """returns float value representing the slope between a point and the origin"""
        if self.x == 0:
            return False
        rise = self.y - 0
        run = self.x - 0
        slope = rise / run
        return slope

    def get_line_to(self, p2):
        """ returns the slope and y-intercept of the line that intersects 2 points"""
        if self.x == p2.x and self.y == p2.y:
            return False
        rise = p2.y - self.y
        run = p2.x - self.x
        slope = rise / run
        intercept = self.y - (slope * self.x)
        return (slope, intercept)

    def distance(self, p2):
        """computes the distance between two points in space"""
        dx = p2.x - self.x
        dy = p2.y - self.y
        dsquared = dx * dx + dy * dy
        result = dsquared ** 0.5
        result = "{0:.2f}".format(result)
        return result


# P6
class SMS_store(object):
    """creates a inbox-like object that stores message data"""

    def __init__(self, messages=[]):
        self.messages = messages

    def add_new_arrival(
        self, from_number, time_arrived, text_of_SMS, has_been_viewed=False
    ):
        """adds a new message to the SMS store"""
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.time_arrived = time_arrived
        self.text_of_SMS = text_of_SMS

        return self.messages.append(
            (
                self.has_been_viewed,
                self.from_number,
                self.time_arrived,
                self.text_of_SMS,
            )
        )

    def count(self):
        """returns the count of messages that are currently in the SMS store"""
        return len(self.messages)

    def get_unread_indexes(self):
        """returns a list of messages that have yet to be viewed"""
        unread = []
        for message in self.messages:
            if message[0] == False:
                unread.append(message)

        return unread

    def get_message(self, i):
        """ returns the message associated with a user-provided index"""
        if i in range(len(self.messages)):
            selected = self.messages[i]
            selected = selected[1:]
            viewed = (True,)
            result = viewed + selected

            return result
        else:
            return None

    def delete(self, i):
        """ deletes the message associated with a user-provided index"""
        if i in range(len(self.messages)):
            del self.messages[i]
            return self.messages
        else:
            return None

    def clear(self):
        """ deletes all messages currently in the SMS store"""
        self.messages.clear()
        return self.messages

    def print(self):
        print(self.messages)


def test_suite():

    # For point class object
    print("\n P1 Distance")
    test(point(0, 0).distance(point(6, 6)) == "8.49")
    test(point(2, 5).distance(point(1, 3)) == "2.24")

    print("\n P2 Reflect")
    test((point(3, 4).reflect_x()) == point(-3, 4))
    test((point(0, 0).reflect_x()) == point(0, 0))

    print("\n P3 Slope from Origin")
    test(point(-5, 4).slope_from_origin() == -0.8)
    test(point(0, 4).slope_from_origin() == False)

    print("\n P4 Slope + Intercept")
    test(point(4, 11).get_line_to(point(6, 15)) == (2.0, 3.0))
    test(point(6, -2).get_line_to(point(3, 4)) == (-2.0, 10.0))
    test(point(6, -2).get_line_to(point(6, -2)) == False)

    # for sms_store class object
    print("\n P6.1 add_new_arrival")
    inbox = SMS_store()
    inbox.add_new_arrival(754745774, "10:32AM", "text 1")
    test(inbox.messages == [(False, 754745774, "10:32AM", "text 1")])

    print("\n P6.2 message count")
    test(inbox.count() == 1)
    inbox.add_new_arrival(754745775, "10:42PM", "text 2")
    test(inbox.count() == 2)

    inbox.add_new_arrival(754745775, "10:43PM", "text 3", True)
    print("\n P6.2 get_unread")
    test(
        inbox.get_unread_indexes()
        == [
            (False, 754745774, "10:32AM", "text 1"),
            (False, 754745775, "10:42PM", "text 2"),
        ]
    )

    print("\n P6.3 get_message")
    test(inbox.get_message(1) == (True, 754745775, "10:42PM", "text 2"))
    test(inbox.get_message(5) == None)

    print("\n P6.4 delete_message")
    test(
        inbox.delete(1)
        == [
            (False, 754745774, "10:32AM", "text 1"),
            (True, 754745775, "10:43PM", "text 3"),
        ]
    )
    test(inbox.delete(5) == None)

    print("\n P6.5 clear_store")
    test(inbox.clear() == [])


test_suite()
