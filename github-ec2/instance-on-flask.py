from flask import Flask, render_template
import boto3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/instanceinfo")
def instanceinfo():
    ec2client = boto3.client('ec2')
    response = ec2client.describe_instances()
    final_dict = {}
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            temp_list = []
            instance_id = instance['InstanceId']
            temp_list.append(instance_id)
            instance_type = instance['InstanceType']
            temp_list.append(instance_type)
            key_name = instance['KeyName']
            temp_list.append(key_name)
            image_id = instance['ImageId']
            temp_list.append(image_id)
            placement = instance['Placement']
            temp_list.append(placement)
            public_dns = instance['PublicDnsName']
            temp_list.append(public_dns)
            final_dict[instance['InstanceId']] = temp_list
    print(final_dict)
    return render_template("instance-details.html", instance=final_dict)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5003")