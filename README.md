## Inspiration

My friends are all runners for the W&M team, and this weekend, I was straddling being at Zable Stadium to watch the meet and Swem Library to participate in Cypher. The big story of the meet was how much wind there was on the track, and how that might impact the runner's times. I was thinking about lower-scale projects that I could accomplish as a solo, freshman hacker, and one of my friends suggested that I create some running software. Using that idea, and knowing the problem that runners were having at Zable, I came up with the idea to make a "final time adjuster" that essentially erases the winds at Zable stadium, and calculates the times that individuals should have run.

## What it does

This program takes in three main variables, mathematically finds the adjusted final time based on those variables and using NOAA's historical weather database and a professional runner's guidelines to running in the wind, and spits out a statement on how the runner would have done had there been no wind.

## How I built it

The project is completely built in Python, but I also heavily relied on Excel to find a lot of the data. I started by writing down every single event (of which there were 42) as well as the time that each event took place at. Then, I used NOAA's historical weather database to map the gale force winds for every hour in the last 48 hours to each event, depending on the hour that that event took place in. After that, I found a guide from a professional runner that detailed exactly how much a specific amount of wind would slow someone down per hour. Using those numbers, as well as the distance ran in each event, I calculated the total amount of time that runners were slowed for each event. After I had all my data laid out in Excel, I went to Python to put all of the variables together to make a script that works on PowerShell. This took a lot of trial and error, as I've only coded in Python for one semester of CSCI 241, but using the outlines of previous projects, many Google searches, and a lot of if statements, I finally got it all working.

## Challenges I ran into

I've never made a project from scratch before! Like I said, I've only taken CSCI 241, where I did make four in-depth projects, but all of those came with skeleton files to start with. This is the first thing I've made from a blank file, so I had to figure out how exactly classes, functions, and "main" work with each other.

On the running side of things, my main challenge is that a lot of these adjusted numbers do not seem realistically accurate. I promise you, they are mathematically what they should be, but there are way too many factors in a race to account for here. Principally, I am assuming that the highest gale force winds of the hour were constantly pushing against each runner for the entirety of their (sometime 30+ minute race). This is not realistic on its own, not to mention the fact that tracks are ovular and for each minute that the wind is against you on one side, it would be with you on the other. This program makes a lot of assumptions and overcorrects in its adjustments, but it does make our W&M runners look good - and that's all that matters.

## Accomplishments that I'm proud of

I am most proud that I did this project by myself. Coming in to Cypher, I thought that I would have to work with a group of more experience people to get anything done, and after missing the opening ceremony and initial team-building, I thought I would be unable to make anything impressive on my own. However, I'm very happy with how well this turned out and I'm proud that this code is 100% my own. I certainly worked harder than I was thinking I would, but I'm glad that I got so much accomplished and I'm proud of the product I made.

## What I learned

Like I said, I think I learned the most from creating a Python file 100% on my own. It's something that I had never done before, and it's also something I wasn't planning on doing this weekend. So, the process of connecting classes with functions and controlling it all through main without a skeleton file to kick-start me was what I learned most from.

## What's next for Colonial Relays Wind Adjuster

I'd love to talk to more runners to make it more accurate - both what they think their time should have been and also how much they feel the wind had impacted them. I also think it would be interesting to ask what percentage of their race they felt the were against the wind. It would also be amazing in the future to get wind data from the track itself - the program currently uses data from the Williamsburg Airport. Finally, the most that this program could improve in the short-term would be with a UI. I personally have no experience with coding UI, but I would be open to learn or team up with someone who could help to make this project feel much more complete.
