import math

class AdjustedTime:

    def __init__(self, event, realTime, section, invitational):
        self.event = event
        self.realTime = realTime
        self.section = section
        self.invitational = invitational
        
        self.realTimeinSecs = 0
        self.wind = 0
        self.timeAndDay = None
        self.adjTimeinSecs = 0
        self.adjTimeinMins = None

    def __str__(self):
        if invitational:
            return "\nYou ran the " + section + " " + event + " Invitational in " + realTime + ", or " + str(self.realTimeinSecs) + " seconds.\n\nUnfortunately, when you ran on " + self.timeAndDay + ", the gale force winds at Zable Stadium were consistantly pushing against you at " + str(self.wind) + "mph.\n\nIf there had been no wind, your time would have been " + self.adjTimeinMins + ", or " + str(self.adjTimeinSecs) + " seconds."
        
        return "\nYou ran the " + section + " " + event + " in " + realTime + ", or " + str(self.realTimeinSecs) + " seconds.\n\nUnfortunately, when you ran on " + self.timeAndDay + ", the gale force winds at Zable Stadium were consistantly pushing against you at " + str(self.wind) + "mph.\n\nIf there had been no wind, your time would have been " + self.adjTimeinMins + ", or " + str(self.adjTimeinSecs) + " seconds."

    def getRealTimeInSeconds(self):
        timeMins = self.realTime
        mm, ss = timeMins.split(":")

        timeSecs = int(mm) * 60 + int(ss)

        self.realTimeinSecs = timeSecs

    def getAdjTimeInMinutes(self):
        adjTotalSecs = self.adjTimeinSecs

        adjMins = str(math.trunc(adjTotalSecs / 60))
        adjSecs = str(adjTotalSecs - (int(adjMins) * 60))

        self.adjTimeinMins = adjMins + ":" + adjSecs

        print(self.adjTimeinMins)

    def getAdjustmentData(self):
        if self.event == "100m" and self.section == "Men's" and self.invitational is False:
            self.wind = 38
            self.timeAndDay = "Friday, March 31st at 12:30 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 2
        if self.event == "100m" and self.section == "Women's" and self.invitational is False:
            self.wind = 30
            self.timeAndDay = "Friday, March 31st at 12:05 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 2
        if self.event == "100m Hurdles" and self.section == "Women's" and self.invitational is False:
            self.wind = 30
            self.timeAndDay = "Friday, March 31st at 11:30 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 2
        if self.event == "100m Hurdles" and self.section == "Women's" and self.invitational is True:
            self.wind = 44
            self.timeAndDay = "Saturday, April 1st at 11:30 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 3
        if self.event == "110m Hurdles" and self.section == "Men's" and self.invitational is False:
            self.wind = 30
            self.timeAndDay = "Friday, March 31st at 11:55 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 2
        if self.event == "110m Hurdles" and self.section == "Men's" and self.invitational is True:
            self.wind = 44
            self.timeAndDay = "Saturday, April 1st at 11:45 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 3
        if self.event == "200m" and self.section == "Men's" and self.invitational is False:
            self.wind = 31
            self.timeAndDay = "Friday, March 31st at 3:40 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 4
        if self.event == "200m" and self.section == "Women's" and self.invitational is False:
            self.wind = 29
            self.timeAndDay = "Friday, March 31st at 3:10 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 3
        if self.event == "400m" and self.section == "Men's" and self.invitational is False:
            self.wind = 29
            self.timeAndDay = "Friday, March 31st at 2:35 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 7
        if self.event == "400m" and self.section == "Women's" and self.invitational is False:
            self.wind = 36
            self.timeAndDay = "Friday, March 31st at 2:05 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 9
        if self.event == "400m Hurdles" and self.section == "Men's" and self.invitational is False:
            self.wind = 36
            self.timeAndDay = "Friday, March 31st at 1:40 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 9
        if self.event == "400m Hurdles" and self.section == "Women's" and self.invitational is False:
            self.wind = 38
            self.timeAndDay = "Friday, March 31st at 1:05 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 10
        if self.event == "800m" and self.section == "Men's" and self.invitational is False:
            self.wind = 21
            self.timeAndDay = "Friday, March 31st at 11:00 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 11
        if self.event == "800m" and self.section == "Women's" and self.invitational is False:
            self.wind = 9
            self.timeAndDay = "Friday, March 31st at 10:35 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 5
        if self.event == "800m" and self.section == "Men's" and self.invitational is True:
            self.wind = 46
            self.timeAndDay = "Saturday, April 1st at 1:50 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 23
        if self.event == "800m" and self.section == "Women's" and self.invitational is True:
            self.wind = 46
            self.timeAndDay = "Saturday, April 1st at 1:40 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 23
        if self.event == "1500m" and self.section == "Men's" and self.invitational is False:
            self.wind = 8
            self.timeAndDay = "Friday, March 31st at 6:35 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 19
        if self.event == "1500m" and self.section == "Women's" and self.invitational is False:
            self.wind = 24
            self.timeAndDay = "Friday, March 31st at 5:55 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 56
        if self.event == "1500m" and self.section == "Men's" and self.invitational is True:
            self.wind = 8
            self.timeAndDay = "Friday, March 31st at 7:15 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 19
        if self.event == "1500m" and self.section == "Women's" and self.invitational is True:
            self.wind = 8
            self.timeAndDay = "Friday, March 31st at 7:05 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 19
        if self.event == "5000m" and self.section == "Men's" and self.invitational is False:
            self.wind = 22
            self.timeAndDay = "Friday, March 31st at 9:55 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 171
        if self.event == "5000m" and self.section == "Women's" and self.invitational is False:
            self.wind = 14
            self.timeAndDay = "Friday, March 31st at 9:10 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 109
        if self.event == "5000m" and self.section == "Men's" and self.invitational is True:
            self.wind = 14
            self.timeAndDay = "Friday, March 31st at 8:10 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 109
        if self.event == "5000m" and self.section == "Women's" and self.invitational is True:
            self.wind = 8
            self.timeAndDay = "Friday, March 31st at 7:25 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 62
        if self.event == "10000m" and self.section == "Men's" and self.invitational is False:
            self.wind = 37
            self.timeAndDay = "Saturday, April 1st at 10:45 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 574
        if self.event == "10000m" and self.section == "Women's" and self.invitational is False:
            self.wind = 41
            self.timeAndDay = "Saturday, April 1st at 10:00 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 636
        if self.event == "10000m" and self.section == "Men's" and self.invitational is True:
            self.wind = 22
            self.timeAndDay = "Friday, March 31st at 9:30 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 341
        if self.event == "10000m" and self.section == "Women's" and self.invitational is True:
            self.wind = 14
            self.timeAndDay = "Friday, March 31st at 8:45 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 217
        if self.event == "3k Steeplechase" and self.section == "Men's" and self.invitational is False:
            self.wind = 24
            self.timeAndDay = "Friday, March 31st at 5:30 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 112
        if self.event == "3k Steeplechase" and self.section == "Women's" and self.invitational is False:
            self.wind = 29
            self.timeAndDay = "Friday, March 31st at 5:00 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 135
        if self.event == "SMR" and self.section == "Men's" and self.invitational is False:
            self.wind = 38
            self.timeAndDay = "Saturday, April 1st at 12:40 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 15
        if self.event == "SMR" and self.section == "Women's" and self.invitational is False:
            self.wind = 44
            self.timeAndDay = "Saturday, April 1st at 12:15 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 18
        if self.event == "DMR" and self.section == "Men's" and self.invitational is False:
            self.wind = 40
            self.timeAndDay = "Saturday, April 1st at 2:30 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 24
        if self.event == "DMR" and self.section == "Women's" and self.invitational is False:
            self.wind = 46
            self.timeAndDay = "Saturday, April 1st at 2:00 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 28
        if self.event == "4x100m" and self.section == "Men's" and self.invitational is False:
            self.wind = 44
            self.timeAndDay = "Saturday, April 1st at 12:05 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 3
        if self.event == "4x100m" and self.section == "Women's" and self.invitational is False:
            self.wind = 44
            self.timeAndDay = "Saturday, April 1st at 11:55 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 3
        if self.event == "4x200m" and self.section == "Men's" and self.invitational is False:
            self.wind = 38
            self.timeAndDay = "Saturday, April 1st at 1:10 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 5
        if self.event == "4x200m" and self.section == "Women's" and self.invitational is False:
            self.wind = 38
            self.timeAndDay = "Saturday, April 1st at 12:55 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 5
        if self.event == "4x400m" and self.section == "Men's" and self.invitational is False:
            self.wind = 43
            self.timeAndDay = "Saturday, April 1st at 4:25 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 11
        if self.event == "4x400m" and self.section == "Women's" and self.invitational is False:
            self.wind = 43
            self.timeAndDay = "Saturday, April 1st at 4:00 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 11
        if self.event == "4x1500m" and self.section == "Men's" and self.invitational is False:
            self.wind = 40
            self.timeAndDay = "Saturday, April 1st at 3:20 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 93
        if self.event == "4x1500m" and self.section == "Women's" and self.invitational is False:
            self.wind = 40
            self.timeAndDay = "Saturday, April 1st at 2:55 PM"
            self.adjTimeinSecs = self.realTimeinSecs - 93

if __name__ == '__main__':
    print("Welcome to the Colonial Relays Wind Adjuster!")
    print("Please enter your event:")

    validEvent = False
    while validEvent is False:
        try:
            event = input()
            if event == "100m" or event == "100m Hurdles" or event == "110m Hurdles" or event == "200m" or event == "400m" or event == "400m Hurdles" or event == "800m" or event == "1500m" or event == "5000m" or event == "10000m" or event == "3k Steeplechase" or event == "SMR" or event == "DMR" or event == "4x100m" or event == "4x200m" or event == "2x400m" or event == "4x1500m":
                validEvent = True
            else:
                raise ValueError
        except:
            print("Invalid event. Please try again, and make sure your input is one of the following: 100m, 100m Hurdles, 110m Hurdles, 200m, 400m, 400m Hurdles, 800m, 1500m, 5000m, 10000m, 3k Steeplechase, SMR, DMR, 4x100m, 4x200m, 2x400m, or 4x1500m.")

    print("Please enter your section, Men's or Women's:")

    validSection = False
    while validSection is False:
        try:
            section = input()
            if section == "Men's" or section == "Women's":
                validSection = True
            else:
                raise ValueError
        except:
            print("Invalid section. Please try again, and enter either Men's or Women's.")


    invitational = False
    if event == "100m Hurdles" or event == "110m Hurdles" or event == "800m" or event == "1500m" or event == "5000m" or event == "10000m":
        print("Did you run in the invitational section? (Yes/No):")
        validInvitationalAsk = False
        while validInvitationalAsk is False:
            try:
                invitationalAsk = input()
                if invitationalAsk == "Yes" or invitationalAsk == "No":
                    validInvitationalAsk = True
                else:
                    raise ValueError
            except:
                print("Invalid input. Please try again and enter either Yes or No")

        if invitationalAsk == "Yes":
            invitational = True


    print("Please enter your time in format Minutes:Seconds :")
    realTime = input()

    data = AdjustedTime(event, realTime, section, invitational)

    data.getRealTimeInSeconds()
    data.getAdjustmentData()
    data.getAdjTimeInMinutes()

    print(data)
    