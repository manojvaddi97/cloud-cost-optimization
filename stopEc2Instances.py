import boto3
import time

client = boto3.client('ec2')
sns_client = boto3.client('sns')

# Function to get instance details with tag, key name as 'Environment and value as 'Sandbox'
def instance_details():
    response = client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Sandbox',],
        },
    ],
)
    instance_details = response["Reservations"]
    instance_id = instance_details[0]["Instances"][0]["InstanceId"]
    instance_status = response['Reservations'][0]['Instances'][0]['State']['Name']
    return instance_id , instance_status

#Function to stop Ec2 instances

def stopec2instances(instance_id):
    response = client.stop_instances(
        InstanceIds=[instance_id,],
)


#Function to send Notifications
def send_notification(instance_id, instance_status):
    instance_id , instance_status = instance_details()
    sns_client.publish(
    TopicArn='arn:aws:sns:ca-central-1:363071022789:EC2OperationsNotification',
    Subject='EC2 Instance Stop Notification',
    Message=f"The instance {instance_id} has been  {instance_status}."
)
    

def lambda_handler(event, context):
    instance_id , instance_status = instance_details()
    if instance_status == 'running':
        stopec2instances(instance_id)
        time.sleep(60)
        send_notification(instance_id, instance_status)
    else:
        print(f"{instance_id} is now {instance_status}")
        

