import trimesh
import os

#sudo apt install python3-pip
#\pip install trimesh

file_name="/home/crta/ros2_ws/src/my_robot_description/DOCUMENT/Inertial_for_urdf.txt"
file = open(file_name,"w")
file.write("Inertial properties   in kgm^2 \n")
file = open(file_name,"a")




#MASS OF LINKS FROM 1 TO 7
robot_link_mass=[5.85, 4.929, 3.368, 3.309, 3.517, 1.510, 1.004]

for i in range(len(robot_link_mass)):
    mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/robot_link_'+ str(i+1)+'.stl')
    # Check if the mesh is loaded properlynego
    print(f"Is mesh watertight?: {mesh.is_watertight}")
    compute_inertial = mesh.moment_inertia
    compute_mass = mesh.mass
    real_mass = robot_link_mass[i]
    real_inertial = compute_inertial / compute_mass * real_mass
    file.write("Robot_link_" + str(i+1) + "\n")

    center_of_mass = mesh.center_mass
    file.write("Centar of mass \n")
    file.write(str(center_of_mass)+ "\n")


    file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
    file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
    file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
    file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
    file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
    file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
    #file.write(str(real_inertial)) #tensore

    file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/robot_base.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 8
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Robot_base  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/platform.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 365
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Platform  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/service_cover.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 5
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Service cover  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/ommni_suport_wheel.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 0.5
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Ommni_suport_wheel  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")


mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/drive_wheel.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 2
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Drive_wheel  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/guide_tool.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 1.5
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Guide tool  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/adapter.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 0.5
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Adapter  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")

mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/camera_tool_rev0.stl')
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 3
real_inertial = compute_inertial / compute_mass * real_mass
file.write("Camera_tool_rev0  \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0]/10e5)+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1]/10e5)+ "\n")
file.write("Izz= "+ str(real_inertial[2][2]/10e5)+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1]/10e5)+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2]/10e5)+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2]/10e5)+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")
