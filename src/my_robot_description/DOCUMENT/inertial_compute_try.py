import os  
import trimesh 
 
file_name="/home/crta/ros2_ws/src/my_robot_description/DOCUMENT/Inertial_for_urdf_igra.txt"
file = open(file_name,"w")
file.write("INERTIAL PROPERTIES \n \n")
file = open(file_name,"a")


filepath = '/home/crta/ros2_ws/src/my_robot_description/meshes'

# fileName = os.path.isfile(filepath)

# print(fileName)

for i in os.listdir(filepath):
     print(i)


mesh = trimesh.load_mesh('/home/crta/ros2_ws/src/my_robot_description/meshes/'+ str(i))
# Check if the mesh is loaded properlynego
print(f"Is mesh watertight?: {mesh.is_watertight}")
compute_inertial = mesh.moment_inertia
compute_mass = mesh.mass
real_mass = 2
real_inertial = compute_inertial / compute_mass * real_mass
file.write(str(i)+" \n")

center_of_mass = mesh.center_mass
file.write("Centar of mass \n")
file.write(str(center_of_mass)+ "\n")


file.write("Ixx= "+ str(real_inertial[0][0])+ "\n")
file.write("Iyy= "+ str(real_inertial[1][1])+ "\n")
file.write("Izz= "+ str(real_inertial[2][2])+ "\n")
file.write("Ixy= "+ str(real_inertial[0][1])+ "\n")
file.write("Ixz= "+ str(real_inertial[0][2])+ "\n")
file.write("Iyz= "+ str(real_inertial[1][2])+ "\n")
#file.write(str(real_inertial)) #tensore

file.write("\n")



