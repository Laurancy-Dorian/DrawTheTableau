"""
Round a number up to the nearest multiple of another
param : Int 	nb 			the number to round up
		Int 	multiple	the multiple to round
"""
def roundToNearestMultiple(nb, multiple):
	return (nb + multiple) - ((nb + multiple) % multiple)
  
