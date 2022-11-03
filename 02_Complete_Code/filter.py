# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        #pass
        self.dim_state = params.dim_state # Model dimension.
        self.dim = int(params.dim_state / 2)
        self.dt = params.dt # Time increment.
        self.q = params.q # Kalman filter Q variable.

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############
        #return 0
        F = np.eye(self.dim_state)
        F[0:self.dim, self.dim:] = np.eye(self.dim) * self.dt
        return np.matrix(F)            
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        #return 0
        x = self.dim_state
        n = self.dim
        mat_q = np.eye(n) * self.q
        Q = np.eye(self.dim_state)
        Q[0:n, 0:n] = mat_q * self.dt ** 3 * (1/3)
        Q[0:n, n:x] = mat_q * self.dt ** 2 * (1/2)
        Q[n:x, 0:n] = mat_q * self.dt ** 2 * (1/2)
        Q[n:x, n:x] = mat_q * self.dt
        return np.matrix(Q)                
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############
        #pass
        F = self.F()
        Q = self.Q()
        x_predict = F * track.x # State prediction.
        P_predict = F * track.P * np.transpose(F) + Q # Covariance prediction.
        track.set_x(x_predict)
        track.set_P(P_predict)        
        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############
        H = meas.sensor.get_H(track.x) # Calculate Jacobian H.
        gamma = self.gamma(track, meas) # Residual.
        S = self.S(track, meas, H) # Covariance of residual.
        K = track.P * np.transpose(H) * np.linalg.inv(S) # Kalman Gain.
        x = track.x + K * gamma # state update
        P = (np.eye(self.dim_state) - K * H) * track.P # Covariance update.        
        # Saving x and P:
        track.set_x(x)
        track.set_P(P)        
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############
        #return 0
        gamma = meas.z - meas.sensor.get_hx(track.x)
        return np.matrix(gamma)         
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############
        #return 0
        S = H * track.P * np.transpose(H) + meas.R
        return np.matrix(S)                
        ############
        # END student code
        ############ 