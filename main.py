pi = 3.14159

class Unit:
  def __init__(self, value, usym):
    self.value = value
    self.unit_symbol=usym
  
  def __add__(self,other):
    return self.value+other
  
  def __sub__(self,other):
    return self.value-other
    
  def __mul__(self,other):
    return self.value*other
    
  def __div__(self,other):
    return self.value/other
  
  def __radd__(self,other):
    return other+self.value
  
  def __rsub__(self,other):
    return other-self.value
    
  def __rmul__(self,other):
    return other*self.value
    
  def __rdiv__(self,other):
    return other/self.value
    
  def __repr__(self):
    return '{0} {1}'.format(self.value, self.unit_symbol)

class Newton(Unit):
  def __init__(self, value):
    Unit.__init__(self,value,'N')

class Horsepower(Unit):
  def __init__(self, value):
    Unit.__init__(self,value,'Hp')

class Meter(Unit):
  def __init__(self, value):
    Unit.__init__(self,value,'m')

class Newton_Meter(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'Nm')

class Watt(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'W')

class Second(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 's')

class Velocity(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'mps')

class Joule(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'J')

class Volt(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'V')

class Gram(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'g')

class Amp(Unit):
  def __init__(self, value):
    Unit.__init__(self,value, 'A')

class AngularVelocity(Unit):
  def __init__(self,value):
    Unit.__init__(self,value, 'ω')

class SquareMeter(Unit):
  def __init__(self,value):
    Unit.__init__(self,value, 'm\xb2')

class CubicMeter(Unit):
  def __init__(self,value):
    Unit.__init__(self,value, 'm\xb3')

def superscript(n):
  nums = list(str(n))
  ssl = []
  for num in nums:
    ssl.append()
  
  return ''.join(ssl)


def l_mechanical_work(newtons_force, distance):
  return Horsepower(newtons_force*distance)

def l_mechanical_power(work, time):
  return Watt(work/time)
  
def r_mechanical_power(torque, rot_velo):
  return Watt(torque*rot_velo)

def pot_energy(weight, height):
  return Joule(weight*height)

def kinetic_energy(mass, velocity):
  return Joule(0.5*mass*velocity)
  
def voltage(current, resistence):
  return Volt(current*resistence)

def e_power(i,v):
  return Watt(i*v)
  
def spring_stiffness(f,x):
  return f/x
  
def spring_energy(k,x):
  return 0.5*k*(x^2)
  
def rect_area(w,l):
  return w*l
  
def rect_prism_volume(w,l,h):
  return w*l*h
  
def density(m,v):
  return m/v
  
def circle_area(r):
  return pi*r^2





