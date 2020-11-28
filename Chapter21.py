from unit_tester import test


class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):

        # Calculate total seconds to represent
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600  # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def to_seconds(self):
        """convert the entire time to seconds"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # P4-P5
    def increment(self, seconds):
        """ increment the time by a specific amount of seconds"""
        return MyTime(0, 0, self.to_seconds() + seconds)

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    # P1-2
    def between(self, t1, t2):
        """see if a time is inbetween two other times"""
        if self.to_seconds() > t1.to_seconds() and self.to_seconds() <= t2.to_seconds():
            return True
        return False

    # P3
    def __add__(self, other):
        """ add two times together"""
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __gt__(self, other):
        """compare if one time is greater than another"""
        return self.to_seconds() > other.to_seconds()

    def __str__(self):
        """ format the time output"""
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    # for increment test cases
    def __eq__(self, other):
        """ format how equality works for  MyTime objects"""
        return (
            self.hours == other.hours
            and self.minutes == other.minutes
            and self.seconds == other.seconds
        )


def test_suite():
    t1 = MyTime(10, 24, 30)
    t2 = MyTime(11, 22, 30)
    t3 = MyTime(12, 11, 45)

    print("\n Between Method")
    test(t2.between(t1, t3) == True)
    test(t1.between(t2, t3) == False)

    print("\n GT operation overload")
    test(bool(t1 > t2) == False)
    test(bool(t2 > t1) == True)

    print("\n Increment Method")
    test(t1.increment(30) == MyTime(10, 25, 0))
    test(t1.increment(-30) == MyTime(10, 24, 0))


test_suite()