import random

def forwardMultiplyGate(x,y):
	return x * y

x = -2
y = 3

tweak_amount = 0.01
best_out = -float("inf")
best_x = x
best_y = y
for k in range(0,100):
	x_try = x + tweak_amount * (random.random() * 2 - 1)
	y_try = y + tweak_amount * (random.random() * 2 - 1)
	out = forwardMultiplyGate(x_try, y_try)
	if (out > best_out):
		best_out = out
		best_x = x_try
		best_y = y_try

print best_out
print best_x
print best_y