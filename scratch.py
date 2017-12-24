import numpy as np;
import numbers;


my_array = np.array([
[1, 2, 3],
[4, 5, 6],    
[7, 8, 9]    
]);


print(my_array);
print(np.all(np.issubdtype(my_array, np.number)));
print(np.any(my_array == 1));

