"""
Made by Tiago Taquelim, 15/12/2016.
>It is a random ant behavior to food and other things using tkinter<
"""

#Note: do not import with *, however i'm only going to use tkinter for this script
from tkinter import *
import random
import variables as var


class Ants(object):
    def __init__(self):
        #Creating the window
        self.root = Tk()
        self.root.title("Ants movement program")
        self.root.geometry(("500x500"))
        self.frame = Frame(self.root)
        self.canvas = Canvas(self.frame,height=400,width=400)

        self.canvas_box = self.canvas.create_rectangle((1,1),(300,300),
                                                       outline="darkblue",tag="border")

        #creating button
        self.resetButton = Button(self.root, text = "Reset",pady = 5, command = self.spawn)

        ##TODO!!
        self.increaseTimeButton = Button(self.root, text = "+ Time")
        self.decreaseTimeButton = Button(self.root, text = "- Time")

        #self.infectButton = Button(self.root, text = "Infect. mode", command = self.infectState)
                                         
                                        
        #packing
        self.frame.pack()
        self.canvas.pack()
        self.resetButton.pack()
        #self.infectButton.pack()       

        #start 
        self.spawn()
        self.foodSpawn()
        self.update()
        self.root.mainloop()
        
        
    def spawn(self):
        print("Respawned")
        self.canvas.delete(ALL)
        
        for i in range(100):
            dx = random.randint(-195,195)
            dy = random.randint(-195,195)
            
            self.bots = self.canvas.create_oval((200 + dx,200 + dy),(205 + dx,205 + dy),
							    fill="black",outline="white",
                                                            tag="bot%i"%(i))
        if self.bots > 100:
            self.foodSpawn()
    def move(self):
        for i in range(100):
            vx = random.randint(-5,5)
            vy = random.randint(-5,5)

            self.canvas.move("bot%i"%i,vx,vy)

            
    def update(self):
        self.move()
        self.colision()
        self.instinct()

        
        self.root.after(1000,self.update)

        
    def foodSpawn(self):
        print("Food Spawned")
        self.foodCords = []
        for i in range(3):
            #Create random coords to make it more random 
            dx = random.randint(-195,195)
            dy = random.randint(-195,195)

            self.foodCords.append((dx+200,dy+210))
            
            self.food = self.canvas.create_rectangle((200 + dx,200 + dy),(210 + dx,210 + dy),
                                                           fill = "green", outline = "green",tag = "food")

    def instinct(self):
        """
         Food sensus: Ants get red when near a food source
        """
        
        r_detectZone = 50
        r_food = 5
        
        for i in range(len(self.foodCords)):
            x_food = self.foodCords[i][0] - (r_detectZone - r_food)
            y_food = self.foodCords[i][1] - (r_detectZone + r_food)

            #Enable for debugging
            """
            detectZone = self.canvas.create_rectangle((x_food, y_food),(x_food + r_detectZone*2, y_food + r_detectZone*2),
                                            outline="blue")
            """
            #Enclosed creates an imaginary rectangle
            items = self.canvas.find_enclosed(x_food,y_food, x_food + r_detectZone*2, y_food + r_detectZone*2)
            print("Inside rectangle %i: "%i, items)
        
            
            
            
            for i in range(len(items) -1 ):
                #TODO , type is printing ints and not rectangle because of the ID.
                if type(items[i]) != "rectangle":

                    #Enable for debugging
                    #self.canvas.itemconfig(items[i], fill="red", outline="red")
                    
                    #vector PF = F-P
                    vx = (x_food +40) - self.canvas.coords(items[i])[0]
                    vy = (y_food +40) - self.canvas.coords(items[i])[1]

                    self.canvas.move(items[i],vx/4 ,vy/4)
                    
                    #TODO move them to the food and eat
                    #self.canvas.scale("food",-0.5,0.5,1,-1)
                else:
                    self.canvas.itemconfig(items[i], fill="green")

            
                

        print("\n")
        
        
    ######


        
    def colision(self):
        for i in range(100):
            coord = self.canvas.bbox("bot%i"%i)
            #a = self.canvas.coord("bot%i"%i)

            if coord == 1:
                vx = random.randint(-5,5)
                vy = random.randint(-5,5)
                
                #Now they bounce back inverting the vector -(x,y)
                self.canvas.itemconfig("bot%i"%i, fill="red")
            

                

    '''
    def infect(self):
        """
         If you enable this option, when the ants touch one another they becoem infected: DEBUGGING PROPOUSE FOR NOW!!
        """
        var.enableInfect += 1
        
        print(var.enableInfect)
        if var.enableInfect % 2 == 0:
            for i in range(100):
                coord = self.canvas.bbox("bot%i"%i)

                colisions = self.canvas.find_overlapping(*coord)

                if len(colisions) != 1:
                    self.canvas.itemconfig("bot%i"%i, fill="red")

    '''

        
if __name__ == "__main__":
    Ants()


