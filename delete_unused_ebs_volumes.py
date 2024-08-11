import boto3

client = boto3.client('ec2')
sns_client = boto3.client('sns')

def delete_unused_ebs_volumes():
    volume_ids =[]
    response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': ['available',]
        },
    ],
)
    for volumes in response['Volumes']:
        volume_id = volumes['VolumeId']
        client.delete_volume(VolumeId=volume_id,)
        volume_ids.append(volume_id)
    return volume_ids

def send_notification(volume_id):
    sns_client.publish(
    TopicArn='arn:aws:sns:ca-central-1:363071022789:delete-unused-ebs-volumes',
    Message=f"Deleted unused EBS volume: {volume_id}",
    Subject='Delete Unused EBS Volumes'
)
    


def lambda_handler(event, context):
    volume_ids = delete_unused_ebs_volumes()
    for volume_id in volume_ids:
        send_notification(volume_id)
    
