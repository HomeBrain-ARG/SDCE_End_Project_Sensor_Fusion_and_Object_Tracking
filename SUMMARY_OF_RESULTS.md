# STEP 1:
## Your task:<br />
- The single track is already initialized for you, so don't worry about track initialization right now.<br />
- In student/filter.py, implement the predict() function for an EKF. Implement the F() and Q() functions to calculate a system matrix for constant velocity process model in 3D and the corresponding process noise covariance depending on the current timestep dt. Note that in our case, dt is fixed and you should load it from misc/params.py. However, in general, the timestep might vary. At the end of the prediction step, save the resulting x and P by calling the functions set_x() and set_P() that are already implemented in student/trackmanagement.py.<br />
- Implement the update() function as well as the gamma() and S() functions for residual and residual covariance. You should call the functions get_hx and get_H that are already implemented in students/measurements.py to get the measurement function evaluated at the current state, h(x), and the Jacobian H.<br />
- Note that we have a linear measurement model for lidar, so h(x)=H*x for now. You should use h(x) nevertheless for the residual to have an EKF ready for the nonlinear camera measurement model you'll need in Step 4. Again, at the end of the update step, save the resulting x and P by calling the functions set_x() and set_P() that are already implemented in student/trackmanagement.py.<br />
- Use numpy.matrix() for all matrices as learned in the exercises.<br />

## What should the result be?<br />
If you have implemented everything correctly, the RMSE plot should show a mean RMSE of 0.35 or smaller. You can see the computed mean RMSE in the legend on the right. Make sure to successfully complete this step and save the RMSE plot before moving to the next.

## Hints:<br />

- We now want to track 3D objects with a constant velocity model including height estimation, so F and Q will be 6D matrices, in comparison to our 2D tracking in the lesson exercise where we assumed a flat world. Therefore, you need to implement the following matrices: [TODO: include image of Latex formulas].<br />
- Remember from the repository overview on the last page that there is a Track class and a Measurement class. These classes define your input to the predict() and update() functions. So you can get the track data by calling track.x and track.P, the measurement data by calling meas.z and meas.R. Also note that the measurement has an attribute sensor that tells us which sensor generated this measurement, so you can get the measurement matrix by calling meas.sensor.get_H(). Take a closer look at the two classes for clarification.<br />
- Note that you don't have a running track management yet, therefore the track state is fixed at 'confirmed' and the score remains at the initial value zero.<br />
- From misc/params.py, you should load the following parameters: dt, q, dim_state.<br />


