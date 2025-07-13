import pygame

# Initialize Pygame
pygame.init()

# Load the image
image_path = "track.png"
track_img = pygame.image.load(image_path)

# Set up the display
win = pygame.display.set_mode((track_img.get_width(), track_img.get_height()))
pygame.display.set_caption("Track with Walls")

# Wall class definition
class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def draw(self, win):
        pygame.draw.line(win, (255, 255, 255), (self.x1, self.y1), (self.x2, self.y2), 5)

# Goal class
class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.isactiv = False

    def draw(self, win):
        pygame.draw.line(win, (0, 255, 0), (self.x1, self.y1), (self.x2, self.y2), 2)
        if self.isactiv:
            pygame.draw.line(win, (255, 0, 0), (self.x1, self.y1), (self.x2, self.y2), 2)

# Get goals function
def getGoals():
    goals = []

    goal1 = Goal(0,200,120,200)
    goal2 = Goal(0,100,120,150)
    goal2_5 = Goal(0,0,150,130)
    goal3 = Goal(120,0,170,120)
    goal3_5 = Goal(200,0,200,120)
    goal4 = Goal(270,0,270,110)
    goal4_5 = Goal(350,0,350,110)
    goal5 = Goal(450,0,450,110)
    goal5_5 = Goal(525,0,525,110)
    goal6 = Goal(600,0,550,130)
    goal6_5 = Goal(550,130,700,60)
    goal7 = Goal(550,130,700,130)
    goal7_5 = Goal(550,130,650,200)
    goal8 = Goal(550,130,570,240)
    goal9 = Goal(410,130,430,260)
    goal9_5 = Goal(430,260,300,350)
    goal10 = Goal(430,260,260,260)
    goal10_5 = Goal(430,260,280,180)
    goal11 = Goal(430,260,400,400)
    goal12 = Goal(550,260,570,400)
    goal13 = Goal(750,400,650,200)
    goal14 = Goal(750,400,800,160)
    goal15 = Goal(750,400,950,240)
    goal16 = Goal(750,400,980,440)
    goal17 = Goal(750,400,900,600)
    goal18 = Goal(750,460,750,600)
    goal19 = Goal(670,460,670,600)
    goal19_5 = Goal(590,460,590,600)
    goal20 = Goal(510,460,510,600)
    goal20_5 = Goal(430,460,430,600)
    goal21 = Goal(350,460,350,600)
    goal21_5 = Goal(280,460,278,600)
    goal22 = Goal(210,460,190,600)
    goal22_5 = Goal(80,600,175,440)
    goal23 = Goal(150,420,0,570)
    goal23_5 = Goal(0,450,130,400)
    goal24 = Goal(0,380,130,380)

    goals.append(goal1)
    goals.append(goal2)
    goals.append(goal2_5)
    goals.append(goal3)
    goals.append(goal3_5)
    goals.append(goal4)
    goals.append(goal4_5)
    goals.append(goal5)
    goals.append(goal5_5)
    goals.append(goal6)
    goals.append(goal6_5)
    goals.append(goal7)
    goals.append(goal7_5)
    goals.append(goal8)
    goals.append(goal9)
    goals.append(goal10_5)
    goals.append(goal10)
    goals.append(goal9_5)
    goals.append(goal11)
    goals.append(goal12)
    goals.append(goal13)
    goals.append(goal14)
    goals.append(goal15)
    goals.append(goal16)
    goals.append(goal17)
    goals.append(goal18)
    goals.append(goal19)
    goals.append(goal19_5)
    goals.append(goal20)
    goals.append(goal20_5)
    goals.append(goal21)
    goals.append(goal21_5)
    goals.append(goal22)
    goals.append(goal22_5)
    goals.append(goal23)
    goals.append(goal23_5)
    goals.append(goal24)

    goals[len(goals)-1].isactiv = True

    return(goals)

# Function to get all walls
def getWalls():
    walls = []

    wall1 = Wall(12, 451, 15, 130)
    wall2 = Wall(15, 130, 61, 58)
    wall3 = Wall(61, 58, 149, 14)
    wall4 = Wall(149, 14, 382, 20)
    wall5 = Wall(382, 20, 549, 31)
    wall6 = Wall(549, 31, 636, 58)
    wall7 = Wall(636, 58, 678, 102)
    wall8 = Wall(678, 102, 669, 167)
    wall9 = Wall(669, 167, 600, 206)
    wall10 = Wall(600, 206, 507, 214)
    wall11 = Wall(507, 214, 422, 232)
    wall12 = Wall(422, 232, 375, 263)
    wall13 = Wall(375, 263, 379, 283)
    wall14 = Wall(379, 283, 454, 299)
    wall15 = Wall(454, 299, 613, 286)
    wall16 = Wall(613, 286, 684, 238)
    wall17 = Wall(684, 238, 752, 180)
    wall18 = Wall(752, 180, 862, 185)
    wall19 = Wall(862, 185, 958, 279)
    wall20 = Wall(958, 279, 953, 410)
    wall21 = Wall(953, 410, 925, 505)
    wall22 = Wall(925, 505, 804, 566)
    wall23 = Wall(804, 566, 150, 570)
    wall24 = Wall(150, 570, 46, 529)
    wall25 = Wall(46, 529, 12, 451)
    wall27 = Wall(104, 436, 96, 161)
    wall28 = Wall(96, 161, 122, 122)
    wall29 = Wall(122, 122, 199, 91)
    wall30 = Wall(199, 91, 376, 94)
    wall31 = Wall(376, 94, 469, 100)
    wall32 = Wall(469, 100, 539, 102)
    wall33 = Wall(539, 102, 585, 121)
    wall34 = Wall(585, 121, 585, 139)
    wall35 = Wall(585, 139, 454, 158)
    wall36 = Wall(454, 158, 352, 183)
    wall37 = Wall(352, 183, 293, 239)
    wall38 = Wall(293, 239, 294, 318)
    wall39 = Wall(294, 318, 361, 357)
    wall40 = Wall(361, 357, 490, 373)
    wall41 = Wall(490, 373, 671, 359)
    wall42 = Wall(671, 359, 752, 300)
    wall43 = Wall(752, 300, 812, 310)
    wall44 = Wall(812, 310, 854, 369)
    wall45 = Wall(854, 369, 854, 429)
    wall46 = Wall(854, 429, 754, 483)
    wall47 = Wall(754, 483, 192, 489)
    wall48 = Wall(192, 489, 104, 436)

    walls.extend([wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
                  wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19,
                  wall20, wall21, wall22, wall23, wall24, wall25, wall27, wall28, wall29,
                  wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38,
                  wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47,
                  wall48])

    return walls


# Main visualization
def main():
    pygame.init()
    
    # Set up display
    win_width = 1000
    win_height = 600
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Track Visualization")

    # Load background image
    track_img = pygame.image.load("track.png").convert()

    # Get walls and goals
    walls = getWalls()
    goals = getGoals()

    # Main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Draw background
        win.blit(track_img, (0, 0))

        # Draw walls
        for wall in walls:
            wall.draw(win)

        # Draw goals
        for goal in goals:
            goal.draw(win)

        # Update the display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()