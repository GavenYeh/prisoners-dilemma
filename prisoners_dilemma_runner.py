# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Prisoner's Dilemma")
     
    size = width, height = 600, 500
    padding = 40

    # create a surface on screen that has the size of 240 x 180
    window = pygame.display.set_mode(size)
     
    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
    largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
    moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

    # Draw buttons
    cooperateButton = pygame.Rect((width / 8), (height * 2/3), width / 4, 50)
    cooperate = mediumFont.render("Cooperate", True, black)
    cooperateRect = cooperate.get_rect()
    cooperateRect.center = cooperateButton.center
    pygame.draw.rect(window, white, cooperateButton)
    window.blit(cooperate, cooperateRect)

    defectButton = pygame.Rect(5 * (width / 8), (height * 2/3), width / 4, 50)
    defect = mediumFont.render("Defect", True, black)
    defectRect = defect.get_rect()
    defectRect.center = defectButton.center
    pygame.draw.rect(window, white, defectButton)
    window.blit(defect, defectRect)

    rectangle_width = width-2*padding
    rectangle_height = 100
    pygame.draw.rect(window,(0,0,255),(padding,padding,rectangle_width,rectangle_height))
    pygame.draw.rect(window,(0,0,255),(padding,rectangle_height+padding*2,rectangle_width,rectangle_height))

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        pygame.display.update() 



     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()