import os
import random
DATA_DIR='/home/ubuntu/AdienceFaces/DATA/aligned'
original_folds_dir='/home/ubuntu/AdienceFaces/folds/original_txt_files'
out_files_dir='/home/ubuntu/AdienceFaces/folds/train_val_txt_files_per_fold'

age_list=['(0, 2)','(4, 6)','(8, 12)','(15, 20)','(25, 32)','(38, 43)','(48, 53)','(60, 100)']
gender_list=['m','f']
#note that since there's a bug in the txt files - (25 32) == (25 23)


for cur_test_fold_ind in range(5):
    cur_fold_out_foldername='test_fold_is_{0}'.format(cur_test_fold_ind)
    cur_fold_out_foldername=os.path.join(out_files_dir,cur_fold_out_foldername)
    
    if not os.path.exists(cur_fold_out_foldername):
        os.mkdir(cur_fold_out_foldername)
    
    
    #test files
    cur_test_fold_filename='fold_{0}_data.txt'.format(cur_test_fold_ind)
    cur_test_fold_filename=os.path.join(original_folds_dir,cur_test_fold_filename)
    
    with open(cur_test_fold_filename) as f:
        def_lines=f.readlines()
    
    def_lines.pop(0)
    
    full_test_list=[]
    for def_line in def_lines:
        def_dic={}
        
        subject_dir=def_line.split('\t')[0]
        image_subject=def_line.split('\t')[2]
        
        image_name='landmark_aligned_face.{0}.{1}'.format(image_subject,def_line.split('\t')[1])

        image_age=def_line.split('\t')[3] 
        
        
        if image_age=='(25 23)':
            image_age='(25 32)'
        

        image_gender=def_line.split('\t')[4]
        
        
        def_dic['subject_dir']=subject_dir
        def_dic['image_name']=image_name
        def_dic['image_subject']=image_subject
        def_dic['image_age']=image_age
        def_dic['image_gender']=image_gender
        
        full_test_list.append(def_dic)
    
    
    images_num=len(full_test_list)
    indices=random.sample(set(range(0,images_num)), images_num)

    
    #creating text.txt file
    age_test_txt_filename=os.path.join(cur_fold_out_foldername,'age_test.txt')
    gender_test_txt_filename=os.path.join(cur_fold_out_foldername,'gender_test.txt')

    for f in [age_test_txt_filename,gender_test_txt_filename]:
        if os.path.exists(f):
            os.remove(f)
        
    age_test_txt_file=open(age_test_txt_filename,'w+')
    gender_test_txt_file=open(gender_test_txt_filename,'w+')
    
    
    for ind in indices:
        subject_dir=full_test_list[ind]['subject_dir']
        image_name=full_test_list[ind]['image_name']
        image_age=full_test_list[ind]['image_age']
        image_gender=full_test_list[ind]['image_gender']
        image_subject=full_test_list[ind]['image_subject']
        
        if image_age in age_list:
            image_age_index=age_list.index(image_age)  
            s='{0}/{1} {2}\n'.format(subject_dir,image_name,image_age_index)
            age_test_txt_file.write(s)

        if image_gender in gender_list:
            image_gender_index=gender_list.index(image_gender)
            s='{0}/{1} {2}\n'.format(subject_dir,image_name,image_gender_index)
            gender_test_txt_file.write(s)
        

    for f in [age_test_txt_file,gender_test_txt_file]:
        f.close()
        
    
    
    full_train_list=[]
    train_folds_indices=list(set(range(5)) - set([cur_test_fold_ind]))
    
    for train_fold_ind in train_folds_indices:
        
        #test files
        cur_train_fold_filename='fold_{0}_data.txt'.format(train_fold_ind)
        cur_train_fold_filename=os.path.join(original_folds_dir,cur_train_fold_filename)

        with open(cur_train_fold_filename) as f:
            def_lines=f.readlines()

        def_lines.pop(0)

        for def_line in def_lines:
            def_dic={}

            subject_dir=def_line.split('\t')[0]
            image_subject=def_line.split('\t')[2]
            image_name='landmark_aligned_face.{0}.{1}'.format(image_subject,def_line.split('\t')[1])
            
            image_age=def_line.split('\t')[3]

            if image_age=='(25 23)':
                image_age='(25 32)'


            image_gender=def_line.split('\t')[4]
            
    
            def_dic['subject_dir']=subject_dir
            def_dic['image_name']=image_name
            def_dic['image_subject']=image_subject
            def_dic['image_age']=image_age
            def_dic['image_gender']=image_gender

            full_train_list.append(def_dic)
    
        
    
    images_num=len(full_train_list)
    indices=random.sample(set(range(0,images_num)), images_num)
    
    val_indices=indices[:images_num/10]
    train_indices=indices[(images_num/10) + 1:]
    train_subset_indices=indices[(images_num/10) + 1: 2* (images_num/10)]
    #train files
    
    cases=['val','train','train_subset']
    
    for case,indices in zip(cases,[val_indices,train_indices,train_subset_indices]):
       
        age_txt_filename=os.path.join(cur_fold_out_foldername,'age_{0}.txt'.format(case))
        gender_txt_filename=os.path.join(cur_fold_out_foldername,'gender_{0}.txt'.format(case))
   
        for f in [age_txt_filename,gender_txt_filename]:
            if os.path.exists(f):
                os.remove(f)

        age_txt_file=open(age_txt_filename,'w+')
        gender_txt_file=open(gender_txt_filename,'w+')

    
        
        for ind in indices:
            subject_dir=full_train_list[ind]['subject_dir']
            image_name=full_train_list[ind]['image_name']
            image_age=full_train_list[ind]['image_age']
            image_gender=full_train_list[ind]['image_gender']
            image_subject=full_train_list[ind]['image_subject']
            if image_age in age_list:
                image_age_index=age_list.index(image_age)  
                s='{0}/{1} {2}\n'.format(subject_dir,image_name,image_age_index)
                age_txt_file.write(s)

            if image_gender in gender_list:
                image_gender_index=gender_list.index(image_gender)
                s='{0}/{1} {2}\n'.format(subject_dir,image_name,image_gender_index)
                gender_txt_file.write(s)


        for f in [age_txt_file,gender_txt_file]:
            f.close()


