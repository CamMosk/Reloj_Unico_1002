k = 0

def setup() :
    size(300, 600)

def draw() :
    global k
    background(175)


    ellipse(width/ 2, k, 50, 50)
    fill(232, 5, 24)
    if k > height :
        k = 0
    else:
        k = map(minute(), 0, 60, 0, height)
        
        
        
        
    ellipse(width/ 2, k, 50, 50)
    fill(0, 0, 0)
    if k > height :
        k = 0
    else:
        k = map(second(), 0, 59, 0, height)
        
        
        

    ellipse(width/ 2, k, 50, 50)
    fill(255)
    if k > height :
        k = 0
    else:
        k = map(hour(), 0, 24, 0, height)
        
        
        
        
  

    
