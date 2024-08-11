# cloud-cost-optimization
Building continuous integration/deployment workflows as well as reproducing and replicating bugs in production efficiently require multiple environments be maintained. This, however, can be costly. In order to reduce AWS cloud infrastructure costs, any EC2 instances running 24/7 unnecessarily (e.g., sandbox and staging environments) must be shut down outside of regular business hours.

Figure 1 below shows an automated process for starting and stopping instances according to a time-based schedule in order to reduce expenses. It is a perfect example of using the serverless approach.
![image](https://github.com/user-attachments/assets/a159481a-6891-4a4f-af54-36accd737a86)

In this case, you can configure a scheduled cron job on Amazon CloudWatch Events to trigger Lambda functions. The function’s handler will scan all EC2 instance metadata and identify those with an “ Environment “ tag, while ignoring those without. Once all instances with the target tag have been identified, the Lambda function will use AWS EC2 API to start or stop the target instances at the designated time.

Another use case for reducing infrastructure costs is the employment of Lambda functions to delete unassigned Elastic IPs and unused Amazon Elastic Block Store (EBS) volumes. Because these resources constitute a significant portion of total AWS infrastructure costs, deleting orphaned resources can result in major savings.

![image](https://github.com/user-attachments/assets/c3c30179-cf4c-4ef2-aafc-4e33bfce554d)

Similarly, the EC2 API can be used to delete or release unassigned IPs and unattached EBS volumes as described in the above scenario.


