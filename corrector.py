#corector program, for Crawler motors, 12/11/2021
import math

class CORRECTOR:
    #constructor
    def __init__(self):
        self.speed= True 
        

    #Use of equation determinated by Marc and Dan: pwm2= 3.17 + 0.844pwm1 + 0.0262pwm1^2 + -2.95E-04pwm1^3 --> y = -0,0003x3 + 0,0262x2 + 0,8437x + 3,1708
    def corrector1(self, speed1):
        if speed1==0:
            speed2 = 0
        else :
            speed2 = - 0.000295*pow(int(speed1),3) + 0.0262*pow(int(speed1),2) + 0.844*int(speed1) + 3.17
        return speed2
    
    def corrector2(self, speed1):
        if speed1==0:
            speed2 = 0
        else :
            speed2 =  -0.0022*pow(int(speed1),2) + 1.7222*int(speed1) -2.5556
        print("BACKWARD : %d" %speed2)
        return speed2
    
    # Before this method, correct Scaling Error Es, using a meter and correct 
    #Measurement and Correction of Systematic Odometry Errors in Mobile Robots, by Johann  Borenstein, Member, IEEE, and Liqiang Feng 
    def corrector3(self):
        print("odometry")
           
        #Dr = 1 #actual right wheel diameter
        #Dl = 1 #actual left wheel diameters
        #Dn = 100 #Dn nominal wheel diameter
        #ba = 1 #actual wheelbase  of  the  vehicle
        bn = 210 #nominal wheelbase  of  the  vehicle, mm
        L = 4000 # L is the square side, mm
        #Nl = 100 # pulse increment encoder left
        #Nr = 1001 # pulse increment encoder right
        #Ce = 180 #Ce encoder resolution (in  pulses  per  revolution)
        #n = 1200 #gear  ratio  of the  reduction  gear  between  the  motor (where the  encoder is  attached)  and  the  drive  wheel
        #conversion  factor  that  translates  encoder  pulses  into linear  wheel  displacement
        
        xabs = 0.0 #START POINT
        yabs = 0.0 #START POINT
        tabs = 0.0 #START POINT
        #------------------CCW----------------------------
        
        xcalcCCW = [1.0, 1.0, 1.0, 1.0, 1.0] # end point without calibration, 5 run
        ycalcCCW = [1.0, 1.0, 1.0, 1.0, 1.0] # end point without calibration, 5 run
        tcalcCCW = [0.0, 0.0, 0.0, 0.0, 0.0] # end point without calibration, 5 run
        
        # compute position error
        epsxCCW = [xabs-xcalcCCW[0], xabs-xcalcCCW[1], xabs-xcalcCCW[2], xabs-xcalcCCW[3], xabs-xcalcCCW[4]]
        epsyCCW = [yabs-ycalcCCW[0], yabs-ycalcCCW[1], yabs-ycalcCCW[2], yabs-ycalcCCW[3], yabs-ycalcCCW[4]]
        epstCCW = [tabs-tcalcCCW[0], tabs-tcalcCCW[1], tabs-tcalcCCW[2], tabs-tcalcCCW[3], tabs-tcalcCCW[4]]
        
        
        #compute centers of gravity
        xCCW = sum(epsxCCW)/5
        yCCW = sum(epsyCCW)/5
        
        #-----------------CW-------------------------
        
        xcalcCW = [0.0, 0.0, 0.0, 0.0, 0.0] # end point without calibration, 5 run
        ycalcCW = [0.0, 0.0, 0.0, 0.0, 0.0] # end point without calibration, 5 run
        tcalcCW = [0.0, 0.0, 0.0, 0.0, 0.0] # end point without calibration, 5 run
        
        # compute position error
        epsxCW = [xabs-xcalcCW[0], xabs-xcalcCW[1], xabs-xcalcCW[2], xabs-xcalcCW[3], xabs-xcalcCW[4]]
        epsyCW = [yabs-ycalcCW[0], yabs-ycalcCW[1], yabs-ycalcCW[2], yabs-ycalcCW[3], yabs-ycalcCW[4]]
        epstCW = [tabs-tcalcCW[0], tabs-tcalcCW[1], tabs-tcalcCW[2], tabs-tcalcCW[3], tabs-tcalcCW[4]]
        
        #compute centers of gravity
        xCW = sum(epsxCW)/5
        yCW = sum(epsyCW)/5
        
        #----------------------------------------------
        
        # COMPUTE Ed
        betha_x = ((xCW - xCCW)/(-4*L))*(180/math.pi)
        betha_y= ((yCW + yCCW)/(-4*L))*(180/math.pi)
        
        #R = (L/2)/(math.sin(betha_x/2))
        R = (L/2)/(math.sin(betha_y/2))
        
        Ed = (R + bn/2)/(R - bn/2)
        
        #COMPUTE Eb
        alpha_x = ((xCW + xCCW)/(-4*L))*(180/math.pi)
        alpha_y = ((yCW - yCCW)/(-4*L))*(180/math.pi)
        
        #bnew = (90/(90 - alpha_x))*bn
        bnew = (90/(90 - alpha_y))*bn
        #correction factors wheel left cl and wheel right cr
        cl = 2 / (Ed + 1)
        cr = 2 / ((1/Ed)+1)
        
        return cl, cr, bnew
        

if __name__=="__main__":
   print("correct test")
   correct=CORRECTOR()
   print("CORRECTOR initialized")
   x=correct.corrector1(20)
   print("result x: ", x)
   
   y=correct.corrector1(50)
   print("result y: ", y)
   
   
   z=correct.corrector1(65)
   print("result z: ", z)
   
   print("CORRECTOR initialized")
   x_=correct.corrector2(20)
   print("result -x: ", x_)
   
   y_=correct.corrector2(35)
   print("result -y: ", y_)
   
   
   z_=correct.corrector2(60)
   print("result -z: ", z_)

   correct2=CORRECTOR()
   a=correct2.corrector3()
   print("result a: ", a)

