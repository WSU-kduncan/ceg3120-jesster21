## Part 1 - Build a VPC

For each step below, provide a screenshot that shows the network resource has been created according to specification along with a description of what the resource does (what is its role). You may add whatever additional notes you would like. **The screenshot and description of each network component is required**. Any other notes you leave behind may make this project more useful in the future. Getting a good screenshot can be done by clicking on the resource and showing configurations in the details menu.

1. Create a VPC.
   - Tag it with "YOURLASTNAME-VPC"
   - Specify a /24 private IP address range
   - ![Project2-1](Images/Project2-1.png)
   - Went to VPC and created a new VPC with the name "KESTERSON-VPC" and the IPv4 CIDR of 10.0.0.0/24
2. Create a subnet
   - Tag it with "YOURLASTNAME-Subnet"
   - Specify a /28 private IP address range
   - Attach it to your VPC
3. Create an internet gateway
   - Tag it with "YOURLASTNAME-gw"
   - Attach it to your VPC
4. Create a route table
   - Tag it with "YOURLASTNAME-routetable"
   - Attach it to your VPC
   - Associate it with your subnet
   - Add a routing table rule that sends traffic to all destinations to your internet gateway
5. Create a security group
   - Tag it with "YOURLASTNAME-sg"
   - Allow SSH for a set of trusted networks including:
     - Your home / where you usually connect to your instances from
     - Wright State (addresses starting with 130.108)
     - Instances within the VPC
   - Attach it to your VPC
   - Image should include your Inbound rules
6. (If necessary, else skip) Create a key pair

## Part 2 - EC2 instances

1. Create a new instance. Give a write up of the following information:
   - AMI selected
     - default username of the instance type selected
   - Instance type selected
2. Attach the instance to your VPC. As discussed there are different pathways to doing this. Say how you did it.
3. Determine whether a Public IPv4 address will be auto-assigned to the instance. Justify your choice to do so (or not do so)
   - **NOTE** - in the next few steps, you will be required to request an Elastic IP address and associate it to the instance. Factor that in to your discussion here.
4. Attach a volume to your instance. As discussed there are different pathways to doing this. Say how you did it.
5. Tag your instance with a "Name" of "YOURLASTNAME-instance". Say how you did it.
6. Associate your security group, "YOURLASTNAME-sg" to your instance. Say how you did it.
7. Reserve an Elastic IP address. Tag it with "YOURLASTNAME-EIP". Associate the Elastic IP with your instance. Say how you did it.
8. Create a screenshot your instance details and add it to your project write up. Example below:
   ![sample instance details](sample.png)
9. `ssh` in to your instance. Change the hostname to "YOURLASTNAME-AMI" where AMI is some version of the AMI you chose. Say how you did it.
   1. It is wise to copy config files you are about to change to filename.old For `/etc/hostname`, for example, I would first copy the current `hostname` file to `/etc/hostname.old`
   2. You should not change permissions on any files you are modifying. They are system config files. You may need to access them with adminisrative privileges.
   3. Here is a helpful resource: https://www.tecmint.com/set-hostname-permanently-in-linux/ I did not modify `/etc/hosts` on mine - do so or not as you wish.
10. Create a screenshot your ssh connection to your instance and add it to your project write up - make sure it shows your new hostname.
