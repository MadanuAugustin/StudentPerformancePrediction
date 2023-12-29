'''
AWS Elastic Beanstalk is a service for deploying and scaling web applications and services.
Upload your code and Elastic Beanstalk automatically handles the deployment—from capacity provisioning,
load balancing, and auto scaling to application health monitoring.


'''


# two configurations we need to setup when ever we are working with elastic bean stalk--
# elastic bean stalk is like a kind of instance which is provided to us to deploy our application

# And one of the extension is that .ebextensions that we created and it contains python.config file
# python.config file is mainly to tell the elastic bean stalk about what is the entry point of our application


# second-configuration
# WSGIPath : application : application -- we need to make sure that we give our application file name