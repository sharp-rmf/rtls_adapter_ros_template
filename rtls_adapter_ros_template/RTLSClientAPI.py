import time
### Import additional required libraries
# import serial
# import socket

class rtlsAPI:
    # The constructor below accepts parameters typically required 
    # by a device connected via the serial port. 
    # Users should modify the constructor as per the requirements
    # of their device's API

    def __init__(self,
                 "Adapter_Connection_Parameters"):
        ######## Connection Parameters/ Settings #########
        #           IMPLEMENT YOUR CODE HERE             #
        # Examples:                                      #
        #                                                #
        # self.ser = serial.Serial()                     #
        # self.ser.port = <connection parameters>        #
        # or                                             #
        # self.socket = socket.socket(socket.AF_INET,    #
        #                             socket.SOCK_STREAM)#
        # self.address = <connection parameters>         #
        ##################################################
        ### Connection Flag Variable
        self.isconnected = False

    ### Device Connection Function ###
    def connect(self):
        try:
            ### Open Connection Command ###
            #                             #
            #  IMPLEMENT YOUR CODE HERE   #
            #                             #
            ###############################
            self.isconnected = True
        except:
            print("Couldn't establish connection!!! \r\nKindly check your connection parameters")
            return False
        else:
            print("Connection successfully")
            return True
    
    ### Device Disconnect Function
    def disconnect(self):
        self.ser.close()
        self.connected = False
    ### Device Get Position Function
    def get_pos(self):
        if 'something':
            x,y,z=0.0, 0.0, 0.0
            ### Extract Location Information Command ###
            #                                          #
            #         IMPLEMENT YOUR CODE HERE         #
            #                                          #
            ############################################
            self.AdditionalFunction("parameters")
            return (x,y,z)
        else:
            print("get position unsuccesful.")
            return None

    ### Optional Get Device Info Function
    def get_info(self):
        ############################
        #                          # 
        # IMPLEMENT YOUR CODE HERE #
        #                          #
        ############################
        return

    ### Additional Functions to support the main get_pos function
    def AdditionalFunction(self, other_parameters):
        ####### Function info ########
        #                            #
        #  IMPLEMENT YOUR CODE HERE  #
        #                            #
        ##############################
        return 