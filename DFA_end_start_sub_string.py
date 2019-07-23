def dfa_4_end_and_sub_(s , p , sym , c = 9):
    
    states = list(range( s+1 ))  
    temp = list(range(s+1))
    
    a1 = []
    b1 = []
    
    dfa = { sym[0] : a1 , sym[1] : b1}
    
    for i in range(s):
        
        if p[i] == sym[0]:
            a1.append([i , i+1])           
            
        else:
            b1.append([i,i+1])
           
    for i in range(s+1):
        
        if i > s-1:
            states[i] = " "
            break
        
        states[i] = p[i: ]
        
    
    ## a
    
    counted = list(i[0] for i in dfa[sym[0]])
    miss = ( list(set(temp)  - set(counted)))
    
    pre = ""   
    for i in miss:
        
        for j in range(i):
            pre += states[j][0]
            
        temp_s = pre + sym[0]
        
        string_list  = []
        
        for j in range(s+1):
            string_list.append(temp_s + states[j])
            size_comp = []
            
        for k in string_list:               
                
                
            if check_(p , k, s):
                size_comp.append(k)
                
                
                
        minElementPos = 0
        for index in range(len(size_comp)-1):
            if len(size_comp[index]) > len(size_comp[index+1]):
                minElementPos = index+1
            
        
        
        a1.append([i, minElementPos])
        
    
    
    temp_s = ""
    pre = ""
    
    counted = list(i[0] for i in dfa[sym[1]])
    miss = ( list(set(temp)  - set(counted)))
  
    for i in miss:
        
        for j in range(i):
            pre += states[j][0]
            
        temp_s = pre + sym[1]
        
        string_list  = []
        
        for j in range(s+1):
            string_list.append(temp_s + states[j])
            size_comp = []
            
        for k in string_list:               
                
                
            if check_(p , k, s):
               
                size_comp.append(k)
                    
                
        
        minElementPos = 0
        for index in range(len(size_comp)-1):
            if len(size_comp[index]) > len(size_comp[index+1]):
                minElementPos = index+1
            
        
        b1.append([i, minElementPos])
    
    
        
    dfa[sym[0]] = sort_(dfa[sym[0]])
    dfa[sym[1]] = sort_(dfa[sym[1]])
    
    if c == 3:
        dfa[sym[0]][-1][1] = dfa[sym[0]][-1][0]
        dfa[sym[1]][-1][1] = dfa[sym[1]][-1][0]
               
    return dfa
                


def check_(p , s, size):  
    
    if size > len(s):
        return False
    
    if s[ -size : ] == p:
        return True
    
    return False



def sort_(lis):
    
    lis.sort(key = lambda x : x[0])
    return lis



import copy 

def disp_transition_(dfa , string , sym , choice ):
       
    
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    print("\n\nString Processing : ")
    
    ini = 0
    next = 0
    
    print( "Q" + str(ini).translate(SUB) , end = " ")
    for i in string:
        next = dfa[i][ini][1]
        print("―――" + i + "――→" , "Q" + str(next).translate(SUB) , end = " ")
        
        if next == "D":
            break
        
        ini = copy.deepcopy(next)
       
    if next == len(dfa[sym[0]]) -1:
        print("\n\nString is accepted")
        
    elif choice == 1 and next == len(dfa[sym[0]]) - 2:
        print("\n\nString is accepted")

        
    else:
        print("\n\nString is rejected")
        
        

def disp_table_(dfa , sym , choice):
    
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    
    print("\nTransition Table : ")
    print("\n    Q    |  " , sym[0] , "   |   " ,   sym[1] ,  end = "\n――――――――――――――――――――――――――\n")
    for i in range(len(dfa[sym[0]])):
        
        if i == 0:
            print("  → " , end = "")
        
        elif i == len(dfa[sym[0]]) - 1 and choice != 1:
            print("  **" , end = "")
            
        elif  i == len(dfa[sym[0]]) - 2 and choice == 1:
            print("  **" , end = "")
            
        else:
            print("    " , end = "" )
        
        
        if choice == 1 and i == len(dfa[sym[0]]) -1  :
            print( "QD"  , "Q" + str(dfa[sym[0]][-1][1]).translate(SUB) , "Q" + str(dfa[sym[1]][-1][1]).translate(SUB) , sep = "   |   ")
            break
            
           
        
        print( "Q" + str(i).translate(SUB) , "Q" + str(dfa[sym[0]][i][1]).translate(SUB) , "Q" + str(dfa[sym[1]][i][1]).translate(SUB) , sep = "   |   ")
    
      


def dfa_4_start_(s , p , sym):
    
    temp = list(range(s+1))
    DEAD = 999
    a1 = [[DEAD, DEAD]]
    b1 = [[DEAD, DEAD]]
    
    dfa = { sym[0] : a1 , sym[1] : b1 }
    
    for i in range(s):
        
        if p[i] == sym[0]:
            a1.append([i , i+1])           
            
        else:
            b1.append([i,i+1])
            
    temp_list = a1     
            
    for k in range(0,len(sym)):
        counted = list(i[0] for i in dfa[sym[k]])
        miss = ( list(set(temp)  - set(counted)))
        
        for i in miss[ : -1]:
            temp_list.append([i,DEAD])
        
        temp_list.append([miss[-1] , miss[-1]])
        temp_list = b1
        counted = []
        miss = []
        
        
    dfa[sym[0]] = sort_(dfa[sym[0]])
    dfa[sym[1]] = sort_(dfa[sym[1]])

    
    for i in dfa.values():
        
        for j  in i:
            if j[0] == DEAD:
                j[0] = "D"
            
            if j[1] == DEAD:
                j[1] = "D"
                
    
    return dfa
    




def draw_dfa(dfa):
    #########################################################
    
    import turtle
      
    import tkinter
    
    root = tkinter.Tk()
    root.geometry('500x500-5+40') #added by me
    cv = turtle.ScrolledCanvas(root, width=1500, height=900)
    cv.pack()
    
    screen = turtle.TurtleScreen(cv)
    screen.screensize(3000,1500) #added by me
    t = turtle.RawTurtle(screen)
    #t.hideturtle()
    #t.circle(100)
    
    
    
    
    #t = turtle.Turtle() # currne position (0,0), 
    #above is +ve, below is negatibe
    
    #dfa = {'a': [[0, 1], [1, 1], [2, 1]], 'b': [[0, 0], [1, 2], [2, 0]]}
    
    
    #dfa = {'a': [[0, 1], [1, 'D'], [2, 'D'], [3, 3], ['D', 'D']], 'b': [[0, 'D'], [1, 2], [2, 3], [3, 3], ['D', 'D']]}
    
    flag = 0
    
    for i in range(len(dfa)):
        for j in range(len(dfa[list(dfa.keys())[0]])):
            
            if dfa[list(dfa.keys())[i]][j][0] == "D":
               flag = 1
               dfa[list(dfa.keys())[i]][j][0] =  len(dfa[list(dfa.keys())[i]]) - 1
               
            if dfa[list(dfa.keys())[i]][j][1] == "D":
                dfa[list(dfa.keys())[i]][j][1] =  len(dfa[list(dfa.keys())[i]]) - 1
    
    
    
    colors = ["red" , "green"  ,"purple" , "red" , "green" , "blue" , "red" , "green" , "blue" , "orange"]
        
    space = 15
    
    arrow = {}
    radius = 15*len(dfa[list(dfa.keys())[0]])
    
    
    t.penup()
    t.goto(-radius*2 , radius)
    t.pendown()
    #t.forward(radius)
    t.goto(-radius, radius)
    t.stamp()
    t.penup()
    t.goto(0,0)
    t.pendown()
    
       
     
        
    for i in range(len(dfa[list(dfa.keys())[0]])):
        
        
        if i == len(dfa[list(dfa.keys())[0]]) -1 and flag == 1:
            t.circle(radius)
            t.write("Dead", align = "center", font = ("Arial", 12, "normal"))    
        
        else:
            
            if i == len(dfa[list(dfa.keys())[0]]) -1 or (i == len(dfa[list(dfa.keys())[0]]) -2 and flag == 1)  :            
                t.circle(radius)
                t.penup()
                t.goto((i)*radius*3, 10)
                t.pendown()
                t.circle(radius- 10)
                t.write("Q" + str(i), align = "center", font = ("Arial", 12, "normal"))
                
            else:
                t.circle(radius)
                t.write("Q" + str(i), align = "center", font = ("Arial", 12, "normal"))
                
        t.color(colors[i])
        #t.write("Q")
        #print(t.position())
        
        arrow[i] = (int(t.position()[0]), int(t.position()[1] + radius*2))
        t.penup()
        t.goto((i+1)*radius*3, 0)
        t.pendown()
        
    	
    	
    	   
    
    
    t.color(colors[-1])
    #t.speed(1)
    
    t.right(90)
    for j in range(len(dfa[list(dfa.keys())[0]])):
        for k in range(len(dfa[list(dfa.keys())[0]])):   ## for a
            
            
            if dfa[list(dfa.keys())[0]][k][0] == j:
                t.penup()
                t.goto(arrow[j][0]+ k*space,arrow[j][1])
                t.pendown()
                t.goto(arrow[j][0] + k*space,arrow[j][1] + (j+1)*40)
                t.write(list(dfa.keys())[0], align = "center", font = ("Arial", 12, "normal"))
                t.goto(arrow[dfa[list(dfa.keys())[0]][k][1]][0] + k*space + 8 ,arrow[j][1] + (j+1)*40)        
                t.goto(arrow[dfa[list(dfa.keys())[0]][k][1]][0]   + k*space,arrow[j][1])
                t.stamp()
                
            else:
                continue
     
       
        
    t.color(colors[-2])
    t.right(180)    
    for j in range(len(dfa[list(dfa.keys())[0]])):
        for k in range(len(dfa[list(dfa.keys())[0]])):   ## for a
            
            
            if dfa[list(dfa.keys())[1]][k][0] == j:
                t.penup()
                t.goto(arrow[j][0]+ k*space,arrow[j][1] - 2*radius)
                t.pendown()
                t.goto(arrow[j][0] + k*space, arrow[j][1]- 2*radius + (j+1)*-40)
                
                #t.penup()
                #t.goto(arrow[j][0] + k*space, arrow[j][1]- 2*radius + (j+1)*-55)
                t.write(list(dfa.keys())[1], align = "right", font = ("Arial", 12, "normal"))
                #t.goto(arrow[j][0] + k*space, arrow[j][1]- 2*radius + (j+1)*-40)
                #t.pendown()
                            
                t.goto(arrow[dfa[list(dfa.keys())[1]][k][1]][0] + k*space + 8,arrow[j][1] - 2*radius + (j+1)*-40)        
                t.goto(arrow[dfa[list(dfa.keys())[1]][k][1]][0]   + k*space,arrow[j][1] - 2*radius)
                t.stamp()
            else:
                continue
    
    root.mainloop()	
    #turtle.done()
    #turtle.bye()
    
    
    ########################################





def main_():
    
    while True:
    
        print("\n\nChoose an Option : ", "1. Starting with " , "2. Ending with ", "3. Substring with ", "4. Exit ", sep = "\n"  )
    
        choice = (input("Input Option : "))
         
        if choice == "4":
            break;
            
                         
        symbol = input("Enter symbols: ")
        pattern = input("Enter pattern to find : ")
        string = input("Enter string to process : ")
        size = len(pattern)
  
                
        dfa = {}
    
        if choice == "1":
        
            dfa = dfa_4_start_(size , pattern , symbol)
            
        elif choice == "2":
            
            dfa = dfa_4_end_and_sub_(size, pattern , symbol)
            
            
        elif choice == "3":
            
            dfa = dfa_4_end_and_sub_(size, pattern , symbol , int(choice))
            
                
        disp_table_(dfa , symbol , int(choice)) 
        disp_transition_(dfa , string , symbol , int(choice))
              
        
        #print(dfa)
        draw_dfa(dfa)
    
    

        
        
main_() 
    
  
  