# Machine Learning tool for the hospital to detect pneumonia #

This is an approach towards building a machine learning tool for the hospital to automate the process of pneumonia detection using Federated Learning techniques and to protect sensitive data using Pysyft and Pygrid libraries in Python.

Cutting edge techniques that will have a huge impact on the future of machine learning in healthcare:
-------------------------------------------------------------------------------------------------------

1. Federated Learning: allows us to train AI models on distributed datasets that you cannot directly access.
2. Differential Privacy: allows us to make formal, mathematical guarantees around privacy preservation when publishing our results (either directly or through AI models).
3. Encrypted Computation: allows machine learning to be done on data while it remains encrypted.

To emphasize: these privacy-preserving developments can allow us to train our model on data from multiple institutions, hospitals, and clinics without sharing the patient data. It allows the use of data to be decoupled from the governance (or control) over data.


Problem Statement:
------------------------------------------------------------------------------------

Build a machine learning tool for the hospital which automates the process of pneumonia detection. The sample X-ray images of the INFECTED and NOT-INFECTED are given. The task is to protect the patient data without sharing the X-ray images with another third party.


Approach:
------------------------------------------------------------------------------------

1. Create an initial model from the available dataset
2. Connect to the hospital's data cluster node
3. Manage access rules and permissions
4. Prepare the tensor data to train and publish
5. Create a training plan procedure
6. Train the model
7. Perform the computations and publish the private datasets on this node
8. As a data owner, manage node's accounts to identify and control who can access the node


Secure Multi-Party Computation:
------------------------------------------------------------------------------------

Secure Multi-party Computation (SMPC) is a different way to encrypt data, sharing it to different devices. The main advantage is, unlike traditional cryptography, SMPC allows us to perform logic and arithmetic operations using encrypted data.

![Alt text](/model_centric_FL_tool/SMPC/multi_party_computation.png?raw=true "multi_party_computation")

In this example, we have Andrew holding his number, in this case he is the owner of the number 5, his personal data. Andrew can anonymize his data decomposing his number into 2 (or more) different numbers. In this case, he decomposes the number 5 into 2 and 3. That way, he can share his anonymized data with his friends Marianne and Bob.

Here, none of them really know the real value of Andrew’s data. They’re holding only a part of it. Any of them can perform any kind of operation without the agreement of all of them. But, while these numbers are encrypted between them, we’ll still be able to perform computations. That way, we can use encrypted values to compute user’s data without showing any kind of sensitive information.

![Alt text](/model_centric_FL_tool/SMPC/encrypted_data_share.png?raw=true "encrypted_data_share")


PySyft Technique:
------------------------------------------------------------------------------------

![Alt text](/model_centric_FL_tool/Libraries/pysyft.png?raw=true "pysyft")

PySyft is a Python library for secure and private Deep Learning. PySyft aims to provide privacy preserving tools within the main Deep Learning frameworks like PyTorch and TensorFlow. That way, the data scientists can use these frameworks to manage any kind of sensitive data applying privacy preserving concepts, without having to be privacy experts and themselves.


PyGrid Platform:
------------------------------------------------------------------------------------

![Alt text](/model_centric_FL_tool/Libraries/pygrid.png?raw=true "pygrid")

PyGrid aims to be a peer-to-peer platform that uses the PySyft framework for Federated Learning and data science.

The architecture is composed of two components: Gateways and Nodes. The Gateway component works like a DNS, routing the nodes that provide the desired datasets.



Authenticating using JWT token:
------------------------------------------------------------------------------------

PyGrid supports authentication via JWT token (HMAC, RSA) or opaque token via remote API to protect the model for different workers.

![Alt text](/model_centric_FL_tool/auth/auth_token.PNG?raw=true "auth_token")

![Alt text](/model_centric_FL_tool/auth/fl_client.PNG?raw=true "fl_client")



Implementation:
------------------------------------------------------------------------------------

1. Create an initial model from the available dataset

![Alt text](/model_centric_FL_tool/code_snippets/import_libraries.png?raw=true "import_libraries")

![Alt text](/model_centric_FL_tool/code_snippets/define_model.PNG?raw=true "define_model")


2. Connect to the hospital's data cluster node

![Alt text](/model_centric_FL_tool/code_snippets/connect_node.png?raw=true "connect_node")


3. Manage access rules and permissions

![Alt text](/model_centric_FL_tool/code_snippets/access_permissions.PNG?raw=true "access_permissions")


4. Prepare the tensor data to train and publish

![Alt text](/model_centric_FL_tool/code_snippets/tensor_data.PNG?raw=true "tensor_data")


5. Create a training plan procedure

![Alt text](/model_centric_FL_tool/code_snippets/training_plan.png?raw=true "training_plan")


6. Train the model

![Alt text](/model_centric_FL_tool/code_snippets/train_model.PNG?raw=true "train_model")

![Alt text](/model_centric_FL_tool/code_snippets/train_model_epoch.PNG?raw=true "train_model_epoch")


7. Perform the computations and publish the private datasets on this node

![Alt text](/model_centric_FL_tool/code_snippets/publish_data.PNG?raw=true "publish_data")


8. As a data owner, manage node's accounts to identify and control who can access the node

PyGrid Interface looks something similar like this for managing the access control for the workers

![Alt text](/model_centric_FL_tool/auth/manage_nodes.png?raw=true "manage_nodes")



Summary:
------------------------------------------------------------------------------------

* In medical imaging, necessary privacy concerns limit us from fully maximizing the benefits of AI in our research.

* Fortunately, with other industries also limited by regulations of private data, three cutting edge techniques have been developed that have huge potential for the future of machine learning in healthcare: federated learning, differential privacy, and encrypted computation.

* These modern privacy techniques would allow us to train our models on encrypted data from multiple institutions, hospitals, and clinics without sharing the patient data.

* Recently, these techniques have become increasingly easier for researchers to implement, thanks to the efforts of scientists from overall AI world.