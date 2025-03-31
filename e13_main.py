import graphics

WINDOW_WIDTH, WINDOW_HEIGHT = 200, 150

def buttons(win):
    # points are ordered ll, ur
    left = graphics.Rectangle(graphics.Point(25, 55), graphics.Point(55, 85)) 
    right = graphics.Rectangle(graphics.Point(145, 55), graphics.Point(175, 85))
    quit = graphics.Rectangle(graphics.Point(85, 116), graphics.Point(115, 146))
    
    left.setFill("red")
    right.setFill("green")
    text = graphics.Text(graphics.Point(100, 133), "Exit")
    text.draw(win)
    
    left.draw(win)
    right.draw(win)
    quit.draw(win)
    
    return left, right, quit

def inside(point, rectangle):
    """ Is point inside rectangle? """
    
    # assume p1 is ll (lower left)
    ll = rectangle.getP1()  
    # assume p2 is ur (upper right)
    ur = rectangle.getP2() 
    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()


def main():
    win = graphics.GraphWin("Simple Breakout", WINDOW_WIDTH, WINDOW_HEIGHT)
    win.setBackground(graphics.color_rgb(240, 240, 240))
    
    left, right, quit = buttons(win)
    
    centerPoint = graphics.Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    text = graphics.Text(centerPoint, "")
    text.draw(win)
    
    while True:
        clickPoint = win.getMouse()
        
        # so we can substitute checkMouse() for getMouse()
        if clickPoint is None:  
            text.setText("")
        elif inside(clickPoint, left): 
            text.setText("left")
        elif inside(clickPoint, right):
            text.setText("right")
        elif inside(clickPoint, quit):
            print("Goodbye")
            break
        else:
            text.setText("")
  
    win.close()

if __name__ == "__main__":
  main()