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

### 3) Image showing two complete frames analysis (frames #196 and #197 executed in VSCode):<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-3_Frames-Analysis.png)<br />

# STEP 4:<br />
## Your task:<br />

- In the Sensor class, implement the function in_fov() that checks if the input state vector x of an object can be seen by this sensor. The function should return True if x lies in the sensor's field of view, otherwise False. Don't forget to transform from vehicle to sensor coordinates first. The sensor's field of view is given in the attribute fov.<br />
- In the Sensor class, implement the function get_hx() with the nonlinear camera measurement function h as follows:<br />
        - transform position estimate from vehicle to camera coordinates,<br />
        - project from camera to image coordinates,<br />
        - make sure to not divide by zero, raise an error if needed,<br />
        - return h(x).<br />
- In the Sensor class, simply remove the restriction to lidar in the function generate_measurement() in order to include camera as well.<br />
- In the Measurement class, initialize camera measurement objects including z, R, and the sensor object sensor.<br />
- After completing these steps, make a movie to showcase your tracking results! You can simply do so by setting exec_visualization = ['show_tracks', 'make_tracking_movie'] in loop_over_dataset.py and re-running the tracking loop.<br />

## What should the result be?<br />

If you have implemented everything correctly, the tracking loop now updates all tracks with lidar measurements, then with camera measurements. The console output shows lidar updates followed by camera updates. The visualization shows that the tracking performs well, again no confirmed ghost tracks or track losses should occur. The RMSE plot should show at least three confirmed tracks. Two of the tracks should be tracked from beginning to end of the sequence (0s - 200s) without track loss. The mean RMSE for these two tracks should be below 0.25.<br />

# Step 4 Results:<br />

### 1) Image showing multitracking objects:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-4_Image.png)<br />

### 2) Image showing the RMSE values per track in comparison to Step 3 you'll see improve RMSE values:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-4_RMSE.png)<br />

### 3) Image showing one complete frame analysis (frames #196 executed in VSCode) in that you'll see camera and lidar measurements:<br />
![alt text](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/blob/main/01_Results/20221102_Step-4_Frames_Processing.png)<br />

# ANSWERED QUESTIONS:<br />
## Writeup Instructions:<br />
You are nearly done! To complete the final project, please answer the following questions in a write-up in pdf or markdown format:<br />

1) Write a short recap of the four tracking steps and what you implemented there (EKF, track management, data association, camera-lidar sensor fusion).<br /> 
**In the first step, an EKF was created with the idea of tracking a single target, it was successfully implemented, although it was noted that the accuracy of the detection was lacking.<br />
In the second step, we implemented a track management with the idea to initialize and delete tracks, set a track state and a track score.<br />
In the third step we implemented a single nearest neighbor data association to associate measurements to tracks with the idea to improve the performance in comparison to the first step in that we only use EKF to track the target.<br />
At the end of the this project we implemented a nonlinear camera measurement model in that we fusioned camera and lidar measurements, as we saw in the graphs above (STEP 4 Results), the precision improved remarkably.**<br />

2) Which results did you achieve? Which part of the project was most difficult for you to complete, and why?<br />
**I managed to understand the different steps to be able to increase the precision in the detection of targets as well as the mathematics that exists behind the applied algorithms. The truth is that the most complicated part was to understand the different matrix calculations behind the different algorithms, for example Mahalanobis. The good part of the development is that there are libraries that facilitate the development and readability of the programs.**<br />

3) Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)?<br />
**Yes, because using both sensors we were able to carry out measurements with lidar to locate objects (cars) in a grid (X;Y) and cameras to detect objects using the different classes present within the CNN pre- trained.**<br />

4) Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?<br />
**One of the points we verified was the one shown in Step 1, which is the difference between the marker box and the detected object (the box looks out of phase with respect to the vehicle), this is corrected at the end of the project in Step 4 with the implementation of the Mahalanobis algorithm.**<br />

5) Can you think of ways to improve your tracking results in the future?<br />
**Is a good idea to include pedestrian detection and other objects detection using the classes included in the trained CNN.**<br />

# VIDEO AND PROGRAM TO CREATE IT:<br />
[Link to download the video!!!](https://github.com/HomeBrain-ARG/SDCE_End_Project_Sensor_Fusion_and_Object_Tracking/tree/main/03_Video)<br />

<video width="320" height="240" controls>
  <source src="03_Video/my_tracking_results.avi" type="video/avi">
</video>

### NOTE: Since I couldn't get the "loop_over_dataset.py" program to create the video by setting the "make_tracking_movie" flag, I created a small program to create the same (code included).
