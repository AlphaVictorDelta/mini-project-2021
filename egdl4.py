import matplotlib.pyplot as plt
import numpy as np
import math

def iline(a1,b1,c1,a2,b2,c2):
    return (((b2*c1-b1*c2)/(a2*b1-b2*a1)),((a2*c1-c2*a1)/(b2*a1-a2*b1)))

def icirclelinep(a,b,c):
    d=(b*b)-(4*a*c)
    return (-b+math.sqrt(d))/(2*a)

def icirclelinen(a,b,c):
    d=(b*b)-(4*a*c)
    return (-b-math.sqrt(d))/(2*a)



print('''Problem - A line AB 80 mm long has its end A 20 mm above HP and 30 mm
         in front of VP. It is inclined at 30 degrees to HP and and 45 degrees to
         VP. Draw the projections and find apparent angles and apparent length.''')

x = np.linspace(-100,150,100)
y = 0*x
fig = plt.figure()
ax = fig.add_subplot(111)

#X AXIS
plt.plot(x,y,'-k')

#y axis
plt.plot(y,x,'-k')

hp=float(input('Enter the distance of line from HP - '))

#y=20
plt.plot(x,y+hp,'-k',linestyle='-.',linewidth='0.4')
a1=0
b1=1
c1=-hp

vp=float(input('Distance of line from VP - '))
plt.plot(x,y-vp,'-k', linestyle='-.',linewidth='0.4')
a2=0
b2=1
c2=vp

angle1=float(input('Angle of line w.r.t HP - '))
a3=(math.tan(angle1*math.pi/180))
#i=(10*math.sqrt(3))
plt.plot(x,a3*x+hp,'-k',linewidth='0.3')
b3=1
c3=-hp

angle2=float(input('Angle of line w.r.t VP - '))
a4=math.tan(-angle2*math.pi/180)
plt.plot(x,a4*x-vp,'-k',linewidth='0.3')
b4=1
c4=vp


length=float(input('Enter the lenth of the line - '))
t1=iline(a1,b1,c1,a3,b3,c3)
circle1=plt.Circle(t1,length,fill=False,linewidth='0.1')
a5=t1[0]
b5=t1[1]
r1=length

t2=iline(a2,b2,c2,a4,b4,c4)
circle2=plt.Circle(t2,length,fill=False,linewidth='0.1')
a6=t2[0]
b6=t2[1]

ax.add_patch(circle1)
ax.add_patch(circle2)
#plt.savefig("two_straight_lines_intersection_point_02.png", bbox_inches='tight')

j1=1+(a3*a3)
k1=2*(-a5+(a3*hp)-(a3*b5))
l1=(a5*a5)+(hp*hp)+(b5*b5)-(2*hp*b5)-(length*length)

j2=1+(a4*a4)
k2=2*(-a6+(-a4*vp)-(a4*b6))
l2=(a6*a6)+(vp*vp)+(b6*b6)-(-2*vp*b6)-(length*length)

intersect1x=icirclelinep(j1,k1,l1)
intersect1y=a3*intersect1x+hp
intersect2x=icirclelinep(j2,k2,l2)
intersect2y=a4*intersect2x-vp

#print(intersect1y,intersect2y)
#print(intersect1x,intersect2x)
#print(intersect1x,intersect1y)
#lines joining to X

plt.plot(y+intersect1x,x,'-k',linewidth='0.3')
plt.plot(y+intersect2x,x,'-k',linewidth='0.3')

#horizontal lines
plt.plot(x,y+intersect1y,'-k',linewidth='0.3')
plt.plot(x,y+(intersect2y),'-k',linewidth='0.3')

#plt.scatter(40*math.sqrt(2),20,color='red')
#plt.scatter(40*math.sqrt(3),-30,color='red')

#last circles
circle3=plt.Circle(t1,intersect2x,fill=False,linewidth='0.3')
ax.add_patch(circle3)

#USe a5 and b5 as centre is same
#intersextnx is the apparent length radius
j3=1+(a1*a1)
k3=2*(-a5+(a1*intersect1y)-(a1*b5))
l3=(a5*a5)+(intersect1y*intersect1y)+(b5*b5)-(2*intersect1y*b5)-(intersect2x*intersect2x)

intersectl1x=icirclelinep(j3,k3,l3)
circle4=plt.Circle(t2,intersect1x,fill=False,linewidth='0.3')

ax.add_patch(circle4)

#final points for lines
#plt.scatter(40,60,color='red')
#plt.scatter(40,-30-40*math.sqrt(2),color='red')

#Drawing lines
plt.plot([t1[0] ,intersectl1x],[t1[1],intersect1y])
plt.plot([t2[0],intersectl1x],[t2[1],intersect2y])

#applength1=math.sqrt((t1[0]-intersectl1x)**2+(t1[1]-intersect1y)**2)
#applength2=math.sqrt((t2[0]-intersectl1x)**2+(t2[1]-intersect2y)**2)
print(intersect2x,intersect1x)


plt.xlim(-100,150)
plt.ylim(-100,150)
ax.set_aspect('equal',adjustable='box')

plt.title('Graph of y=0')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.xticks(np.arange(-100, 150, 10))
plt.yticks(np.arange(-100,150, 10))#.set_aspect('equal', adjustable='box')
#plt.grid()
plt.show()
