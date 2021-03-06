#Hyperparameter
growth_k = 24
data_path = 'data/wiki_crop/wiki_db_96.mat'
tfrecord_train = 'tfrecords/train_96.tfrecords'
tfrecord_valid = 'tfrecords/valid_96.tfrecords'
# Number of (dense block + Transition Layer)
nb_blocks = 3
init_learning_rate = 0.1
# AdamOptimizer epsilon
epsilon = 1e-4

dropout_rate = 0.2
class_num_gender = 2
class_num_age = 101
image_size = 96
img_channels = 3
nb_of_train_images = 30510
nb_of_test_images = 7628

# Momentum Optimizer will use
nesterov_momentum = 0.9
weight_decay = 1e-4

# Label & batch_size
batch_size = 64

train_fraction = 0.8
test_fraction = 0.2

test_batch_size = 100
total_epochs = 300
test_epochs  = 1
	
