#-------------------------------------------------#
# Title: Working with Class
# Dev:   Rockey Aye
# Date:  Sep 3, 2018
# Change Log: New
# Change Description:  Rockey Aye, 9/3/2018, Create code to complete assignment 8
# 1.    Create one or more classes to store and process Product data using the code
#       provided by Assignment 8.
#-------------------------------------------------#

#--- DATA ---#
objFile = None #File Handle
strUserInput = None #A string which holds user input

#--- PROCESSING ---#
# Setting up multiple classes for processing and storing data

# Class for Product Name
class Product(object):
    # Fields
    strProduct = ""

    # Constructor
    def __init__(self, Name):  # Add Product Name
        #Attributes
        self.__Name = Name

    # Properties
    @property #getter(accessor)
    def Name (self):
        return self.__Name

    @Name.setter #mutator
    def Name(self, Value):
        self.__Name = Value

    # Methods
    def ToString(self):
        return str(self.Name)

    def __str__(self):
        return self.ToString()
# End of class

# Class for Info / ID
class Info(Product):
    # Fields
    strInfo = ""

    # Constructor
    def __init__(self, ID, Name):  # Add Product ID
        #Attributes
        super(Info, self).__init__(Name)
        self.__ID = ID

    # Properties
    @property #getter(accessor)
    def ID (self):
        return self.__ID

    @ID.setter #mutator
    def ID(self, Value):
        self.__ID = Value

    # Methods
    def ToString(self):
        return str(self.ID) + "," + str(self.Name)

    def __str__(self):
        return self.ToString()
# End of class

# Class for Item Value
class ValueProd (Info):
    # Fields
    strValueProd = ""

    # Constructor
    def __init__(self, ID, Name, Price): # Add Product Value
        # Attributes
        super(ValueProd, self).__init__(ID, Name)
        self.__Price = Price

    # Properties
    @property #getter(accessor)
    def Price (self):
        return self.__Price

    @Price.setter #mutator
    def Price(self, Value):
        self.__Price = Value

    # Methods
    def ToString(self):
        return str(self.ID) + "," + str(self.Name) + "," + str(self.Price)

    def __str__(self):
        return self.ToString()
# End of class

# Class for Processing Data
class ProdProcessor():
    strMessage = '''Type Your Desired Product Id, Name, and Price.  Enter 'Exit' to quit!'''

    def WriteProductUserInput(File):
      try:
        print(ProdProcessor.strMessage)
        while(True):
          strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
          lstInput = strUserInput.split(',')
          objP = ValueProd(lstInput[0], lstInput[1], lstInput[2])
          if(strUserInput.lower() == "exit"): break
          else: File.write(objP.ToString() + "\n")
      except Exception as e:
        print("Error: " + str(e))

    def ReadAllFileData(File, Message="Contents of File"):
      try:
        print(Message)
        File.seek(0)
        print(File.read())
      except Exception as e:
        print("Error: " + str(e))

#--- PRESENTATION ---#
try:
  objFile = open("C:\_PythonClass\Products.txt", "r+")
  ProdProcessor.ReadAllFileData(objFile, "Here is the current data:")
  ProdProcessor.WriteProductUserInput(objFile)
  ProdProcessor.ReadAllFileData(objFile, "Here is this data was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()
