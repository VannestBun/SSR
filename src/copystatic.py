# import os
# import shutil

# def copy_static():
#     dest_path = "public/"
#     source_path = "static/"
#     if os.path.exists(dest_path): # check to clear existing stuff
#         shutil.rmtree(dest_path) #clears all public files and directory
#     os.mkdir(dest_path)
#     # Start the recursive copy from static to public
#     copy_recursive(source_path, dest_path) 
    
# def copy_recursive(src, dst):

#     print(os.listdir(src), "this is listdir(src)")
#     # output: ['images', 'index.css'] this is listdir(src)
#     # ['rivendell.png']


#     for item in os.listdir(src):
#         src_path = os.path.join(src, item)
#         # static/images, static/index.css..
#         print(src_path, "src_path")

#         dst_path = os.path.join(dst, item)
#         print(dst_path, "dst_path")
#         # public/images, public/index.css..
        
#         if os.path.isfile(src_path):
#             shutil.copy(src_path, dst_path)
#         else:
#             os.mkdir(dst_path)
#             # Pass the new source and destination paths
#             copy_recursive(src_path, dst_path) 

import os
import shutil


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
