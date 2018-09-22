def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   weightMars = weight * .38
   weightJupiter = weight * 2.34
   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(weightMars, weightJupiter))
   
   
if __name__ == '__main__':
   weight_on_planets()