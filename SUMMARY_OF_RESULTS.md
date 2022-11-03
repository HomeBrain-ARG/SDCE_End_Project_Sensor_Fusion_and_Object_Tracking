# STEP 1:<br />

## Your task:<br />

- The single track is already initialized for you, so don't worry about track initialization right now.<br />
- In student/filter.py, implement the predict() function for an EKF. Implement the F() and Q() functions to calculate a system matrix for constant velocity process model in 3D and the corresponding process noise covariance depending on the current timestep dt. Note that in our case, dt is fixed and you should load it from misc/params.py. However, in general, the timestep might vary. At the end of the prediction step, save the resulting x and P by calling the functions set_x() and set_P() that are already implemented in student/trackmanagement.py.<br />
- Implement the update() function as well as the gamma() and S() functions for residual and residual covariance. You should call the functions get_hx and get_H that are already implemented in students/measurements.py to get the measurement function evaluated at the current state, h(x), and the Jacobian H.<br />
- Note that we have a linear measurement model for lidar, so h(x)=H*x for now. You should use h(x) nevertheless for the residual to have an EKF ready for the nonlinear camera measurement model you'll need in Step 4. Again, at the end of the update step, save the resulting x and P by calling the functions set_x() and set_P() that are already implemented in student/trackmanagement.py.<br />
- Use numpy.matrix() for all matrices as learned in the exercises.<br />

## What should the result be?<br />

If you have implemented everything correctly, the RMSE plot should show a mean RMSE of 0.35 or smaller. You can see the computed mean RMSE in the legend on the right. Make sure to successfully complete this step and save the RMSE plot before moving to the next.<br />

## Step 1 Results:<br />

### 1) Image showing one track image:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-1_Image-Tracks.png)<br />

### 2) Image showing RMSE value below 0.35:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-1_RMSE.png)<br />

# STEP 2:<br />

## Your task:<br />

- In the Track class, replace the fixed track initialization values by initialization of track.x and track.P based on the input meas, which is an unassigned lidar measurement object of type Measurement. Transform the unassigned measurement from sensor to vehicle coordinates with the sens_to_veh transformation matrix implemented in the Sensor class. Initialize the track state with 'initialized' and the score with 1./params.window, where window is the window size parameter, as learned in the track management lesson.<br />
- In the Trackmanagement class, implement the manage_tracks() function to complete the following tasks:<br />
        - Decrease the track score for unassigned tracks.<br />
        - Delete tracks if the score is too low or P is too big (check params.py for parameters that might be helpful). Note that you can delete tracks by calling the given function delete_track(), which will remove a track from track_list.<br />
- In the Trackmanagement class, implement the handle_updated_track() function to complete the following tasks:<br />
        - Increase the track score for the input track.<br />
        - Set the track state to 'tentative' or 'confirmed' depending on the track score.<br />
- Use numpy.matrix() for all matrices as learned in the exercises.<br />

## What should the result be?<br />
If you have implemented everything correctly, the visualization shows that a new track is initialized automatically where unassigned measurements occur, the true track is confirmed quickly, and the track is deleted after it has vanished from the visible range. You can see that the track has been deleted if the console output says 'deleting track no. 0'. There is one single track without track losses in between, so the RMSE plot should show a single line. Make sure to successfully complete this step and save the RMSE plot before moving to the next.<br />

## Step 2 Results:<br />

### 1) Image showing one confirmed track:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-2_Image-Box_2.png)<br />

### 2) Image showing the track deleted:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-2_Image-Deleted-Track.png)<br />

### 3) Image showing RMSE value:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-2_RMSE.png)<br />

# STEP 3:<br />
## Your task:<br />

- In the Association class, implement the associate() function to complete the following tasks:<br />
        - Replace association_matrix with the actual association matrix based on Mahalanobis distances for all tracks in the input track_list and all measurements in the input meas_list. Use the MHD()function to implement the Mahalanobis distance between a track and a measurement. Also, use the gating() function to check if a measurement lies inside a track's gate. If not, the function shall return False and the entry in association_matrix shall be set to infinity.<br />
        - Update the list of unassigned measurements unassigned_meas and unassigned tracks unassigned_tracks to include the indices of all measurements and tracks that did not get associated.<br />
- In the Association class, implement the get_closest_track_and_meas() function to complete the following tasks:<br />
        - Find the minimum entry in association_matrix, delete corresponding row and column from the matrix.<br />
        - Remove corresponding track and measurement from unassigned_tracks and unassigned_meas.<br />
        - Return this association pair between track and measurement. If no more association was found, i.e. the minimum matrix entry is infinity, return numpy.nan for the track and measurement.<br />

## What should the result be?<br />

The association works properly if you see in the visualization that multiple tracks are updated with multiple measurements. The console output shows that each measurement is used at most once and each track is updated at most once. The visualization should show that there are no confirmed “ghost tracks” that do not exist in reality. There may be initialized or tentative “ghost tracks” as long as they are deleted after several frames. Make sure to successfully complete this step and save the RMSE plot before moving to the next. If you still saw some initialized or tentative ghost tracks here, let's see if we can deplausibilize them through sensor fusion with camera in the next step!<br />

## Step 3 Results:<br />

### 1) Image showing multitracking objects:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-3_Image-Multi-Tracking.png)<br />

### 2) Image showing the RMSE value per track (in this case 3 tracks):<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-3_RMSE.png)<br />


