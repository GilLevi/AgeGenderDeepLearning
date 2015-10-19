TOOLS=/home/ubuntu/repositories/caffe/build/tools
DATA=/home/ubuntu/AdienceFaces/lmdb/Test_fold_is_4/gender_train_lmdb
OUT=/home/ubuntu/AdienceFaces/mean_image/Test_folder_is_4

$TOOLS/compute_image_mean.bin $DATA $OUT/mean.binaryproto

