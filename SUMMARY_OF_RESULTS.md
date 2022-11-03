# STEP 1:
## Your task:<br />
- The single track is already initialized for you, so don't worry about track initialization right now.<br />
- In student/filter.py, implement the predict() function for an EKF. Implement the F() and Q() functions to calculate a system matrix for constant velocity process model in 3D and the corresponding process noise covariance depending on the current timestep dt. Note that in our case, dt is fixed and you should load it from misc/params.py. However, in general, the timestep might vary. At the end of the prediction step, save the resulting x and P by calling the functions set_x() and set_P() that are already implemented in student/trackmanagement.py.<br />
- Implement the update() function as well as the gamma() and S() functions for residual and residual covariance. You should call the functions get_hx and get_H that are already implemented in students/measurements.py to get the measurement function evaluated at the current state, h(x), and the Jacobian H.<br />
- Note that we have a linear measurement model for lidar, so h(x)=H*x for now. You should use h(x) nevertheless for the residual to have an EKF ready for the nonlinear camera measurement model you'll need in Step 4. Again, at the end of the update step, save the resulting x and P by calling the functions set_x() and set_P() that are already implemented in student/trackmanagement.py.<br />
- Use numpy.matrix() for all matrices as learned in the exercises.<br />

## What should the result be?<br />
If you have implemented everything correctly, the RMSE plot should show a mean RMSE of 0.35 or smaller. You can see the computed mean RMSE in the legend on the right. Make sure to successfully complete this step and save the RMSE plot before moving to the next.<br />

### 1) Image showing one track image:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-1_Image-Tracks.png)<br />

### 2) Image showing RSME value below 0.35:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-1_RMSE.png)<br />




