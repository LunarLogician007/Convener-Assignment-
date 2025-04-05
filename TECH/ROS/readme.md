## Autonomous Navigation on TurtleBot3 using ROS 2 and Docker

We aim to implement **autonomous navigation** on the **TurtleBot3** platform by leveraging the standard ROS 2 packages as outlined in the official [TurtleBot3 documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/). The development environment will utilize the previously configured Docker image used for the **fROSty** project, ensuring consistency and portability across systems.

### System Architecture

The system integrates two core components essential for autonomous mobile robotics:

#### 1. Simultaneous Localization and Mapping (SLAM)
We will use **Cartographer**, a real-time SLAM algorithm developed by Google, to enable the TurtleBot3 to:

- Construct a 2D map of an unknown environment in real-time.
- Localize itself within the map while navigating.

This eliminates the need for a pre-existing map and allows for dynamic exploration.

#### 2. ROS 2 Navigation Stack
For path planning and control, we will employ the **ROS 2 Navigation Stack**, which includes:

- **Global planner**: Generates an optimal path from the current location to a user-defined goal.
- **Local planner**: Generates velocity commands that consider immediate obstacles.
- **Recovery behaviors**: Handles failure scenarios such as being stuck or blocked.

These components work together to ensure smooth and intelligent movement through the environment.

### Configuration and Deployment

All configurations—including robot model selection, sensor calibration, map saving/loading, and parameter tuning—will strictly follow the official guidelines. This ensures:

- **Reliability** across different test environments.
- **Reproducibility** for future use or educational purposes.

The entire implementation will be containerized using Docker. The container will include:

- ROS 2 (Humble/Foxy, depending on compatibility).
- SLAM packages (Cartographer).
- Navigation stack (Nav2).
- Visualization tools like RViz2.
- Simulation tools like Gazebo (optional).

