# Session 4 Assignment

In this assignment we will be writing a self defined Qualean class. The qualean accepts a real number from the user. This real number can take only 3 values $$[1,0,-1]$$. It also accepts $$1.0$$ and $$-1.0 $$. It signifies True,False and Maybe states, however it takes a imaginary number which is randomly generated from code random.uniform(-1,1) i.e. a number randomly generated between -1 and 1 is multiplied by the real number passed by the user. 

Then this number is rounded off to the 10th decimal place using Banker's rounding and then finally we store this particular number . Banker's rounding is implemented in python so don't require to write any new round function.

Following are the functions which are defined inside the Qualean class. 



## \_\_init\_\_ : 

The \_\_init\_\_  function first checks the if the real number passed by the user is either -1, 1 or 1.This real number is multiplied by a random number generated between - 1 and 1 and then this is result is rounded up using bankers rounding to 10th Decimal place and stored in self.num variable.

## \_\_eq\_\_ : 

The equal function find equality between two Qualean numbers. Accept two arguments. The self.num ,which is stored while \_\_init\_\_ function, is equated with a another Qulaean number generated by passing the real number as an argumnet to the \_\_eq\_\_ function . We the same method we use in the \_\_init\_\_ to created a new Qualean is the \_\_eq\_\_ function .

## \_\_float\_\_: 

\_\_float\_\_ Returns the float of the Qualean number created.

## \_\_add\_\_: 

Function accepts 2 arguments. HAs to be passed two real number one is store in self.num as a Qualean number , the other converted to Qualean within the \_\_add\_\_ function. the addition of both the qualeans are returned as a result.

## \_\_ge\_\_: 

\_\_ge\_\_ Function check if the qualean number passed is greater than or equal to self.num qualean number.

## \_\_gt\_\_: 

\_\_gt\_\_ Function check with the self.num qualean numbe is greater than the number passed.

## \_\_invertsign\_\_ : 

\_\_invertsign\_\_ Function inverts the sign of the number passed and generated . Returns a positive number if the Qualean number generated is negative an vis-a-vis.

## \_\_le\_\_: 

\_\_le\_\_  Function check if the qualean number passed is less than or equal to self.num qualean number.

## \_\_lt\_\_: 

\_\_lt\_\_ Function check with the self.num qualean numbe is less than the number passed.

## \_\_mul\_\_: 

\_\_mul\_\_ function multiplies two qualeans numbers.

## \_\_bool\_\_: 

The bool function return 0 if the qualean number passed to the \_\_bool\_\_ is zero else it return true.

## \_\_sqrt\_\_: 

Return the square root of a number. For a positive number passed it return a positive number . For a negative number passed it return a complex numbers.

## __\_str\_\_: 

The \_\_str\_\_Function convert the self.num value to str. 

## \_\_repr\_\_: 

__\_repr\_\_ function is used to compute the “official” string representation of an object. 

\_repr\_\_  is used to compute the “official” string representation of an object. 

The built-in function uses to display the object.

 returns a printable representation of the object, one of the ways possible to create this object.  



## \_\_or\_\_:

\_\_or\_\_ function is carzy cool 

## \_\_and\_\_:

\_\_and\_\_ function is also a crazy cool function 