from troposphere import Ref, Template, Parameter, Output, Join, GetAtt
import troposphere.ec2 as ec2
t=Template()
#SecurityGroup
#AMIID and instanceID
#SSH key pair

sg = ec2.securityGroup("Lampsg")
sg.GroupDescription = "Allow access through ports 80 and 22 to the web server"
sg.SecurityGroupIngress = [
	ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort = "22", ToPort = "22", CidrIp = "0.0.0.0/0"),
	ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort = "80", ToPort = "80", CidrIp = "0,0,0,/0"),
]

t.add_resource(sg)

print(t.to_json())
