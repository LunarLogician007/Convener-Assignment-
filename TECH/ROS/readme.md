## Autonomous Navigation on TurtleBot3 using ROS 2 and Docker

Aim :- To implement **autonomous navigation** on the **TurtleBot3** platform by leveraging the standard ROS 2 packages as outlined in the official [TurtleBot3 documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/). The development environment will utilize the previously configured Docker image used for the **fROSty** project, ensuring consistency and portability across systems.

### System Architecture

The system integrates two core components essential for autonomous mobile robotics:

#### 1. Simultaneous Localization and Mapping (SLAM)
We will use **Cartographer**, a real-time SLAM algorithm developed by Google, to enable the TurtleBot3 to:

- Construct a 2D map of the environment in real-time which will be used later.
Follow the Slam subsection under the simulation in the [TurtleBot3 documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/).

#### 2. ROS 2 Navigation Stack
### 2. ROS 2 Navigation Stack
For path planning and control, we will employ the **ROS 2 Navigation Stack (Nav2)**. It enables the robot to autonomously reach a specified goal while avoiding obstacles and reacting to dynamic changes in the environment. The stack integrates motion planning, control, and recovery mechanisms into a modular framework.

Follow the naviagtion subsection under the simulation in the [TurtleBot3 documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/).


The entire implementation will be containerized using Docker. The container will include:

- ROS 2 (Humble).
- SLAM packages (Cartographer).
- Navigation stack (Nav2).
- Visualization tools like RViz2.
- Simulation tools like Gazebo .

## 4. Final Submission

Please submit the following:

- **Complete ZIP file** of the ROS 2 workspace, including all packages, configuration files, and launch files used for the implementation.
-  **Screen recording** demonstrating autonomous navigation of the TurtleBot3, showcasing:
  - SLAM in action (mapping and localization).
  - Goal setting and successful path execution.
  - Obstacle avoidance behavior.

Ensure that the video clearly captures RViz2, Gazebo and the robot's movement during the navigation process.


