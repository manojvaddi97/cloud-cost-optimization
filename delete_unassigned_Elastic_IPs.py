import boto3

client = boto3.client('ec2')
sns_client = boto3.client('sns')

def release_elastic_IP():
    response = client.describe_addresses()
    released_ips= []
    for address in response['Addresses']:
        allocation_id =address['AllocationId']
        public_ip = address['PublicIp']
        if 'AssociationId' not in address:
            response = client.release_address(
            AllocationId=allocation_id
)
            released_ips.append(public_ip)
    return released_ips

    
def send_notification(public_ip):
    sns_client.publish(
    TopicArn='arn:aws:sns:ca-central-1:363071022789:release_unused_elastic_IPs',
    Message=f"Releasing unassigned Elastic IP: {public_ip}",
    Subject='Release Unassigned Elastic IP'
)
 
def lambda_handler(event, context):
    released_ips = release_elastic_IP()
    for public_ip in released_ips:
        send_notification(public_ip)
    