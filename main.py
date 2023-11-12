def CubicEquiation(a,b,c,d): #create a function,beacuse we just need a b c d to solve the equiation ,so we just put a b c d in this function
    q=((((-b**3/27*a**3)+(b*c/6*a**2)-(d/2*a))+(((-b**3/27*a**3)+(b*c/6*a**2)-(d/2*a))**2+(((c/3*a)-(b**2/9*a**2))**3))**(1/2))**(1/3)) #formula
    w=((((-b**3/27*a**3)+(b*c/6*a**2)-(d/2*a))-(((-b**3/27*a**3)+(b*c/6*a**2)-(d/2*a))**2+(((c/3*a)-(b**2/9*a**2))**3))**(1/2))**(1/3)) #formula
    e=(b/3*a) #formula
    r=q+w-e #formula
    return str(r.real)#we need to add .real after the anwser beacuse we need a interger anwser
print("Hello world")
name=input("What is your name")
print("Nice to meet you",name,"I will solve ax**3-bx**2+cx-d=0")#give user a greeting,and write what kind of equiation we can solve in this programer.
a=int(input("Tell me a"))#ask user what is a
b=int(input("tell me b"))#ask user what is b
c=int(input("tell me c"))#ask user what is c
d=int(input("tell me d"))#ask user what is d
line="Hellow,"+name.capitalize()+" I will solve"+str(a)+"x^3-"+str(b)+"x^^2+"+str(c)+"x-"+str(d)+"=0"#This is to create a sentence for user
line=line.replace("--","-")#to refine the sentence
print(line)#print the sentence
print(CubicEquiation(a,b,c,d))#print the anwser

