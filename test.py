# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"
  
  
def godown():
    if head.direction != "up":
        head.direction = "down"
  
  
def goleft():
    if head.direction != "right":
        head.direction = "left"
  
  
def goright():
    if head.direction != "left":
        head.direction = "right"
  
  
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
  
  
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
           
