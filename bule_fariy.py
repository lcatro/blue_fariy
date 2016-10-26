
import os
import pickle
import rsa
import sys
import time


def get_current_path() :
    last_dir_index=sys.argv[0].rfind('\\')
    
    return sys.argv[0][:last_dir_index+1]
    
def build_new_rsa_keys() :
    keys_file=open(get_current_path()+'keys.pem','w')
    
    if keys_file :
        new_public_key,new_private_key=rsa.newkeys(1024)
        serialization_data=pickle.dumps((new_public_key,new_private_key))
        
        keys_file.write(serialization_data)
        keys_file.close()
       
def get_rsa_public_key() :
    keys_file=open(get_current_path()+'keys.pem')

    if keys_file :
        public_key,private_key=pickle.load(keys_file)
        keys_file.close()
        
        return public_key
    
    return None
           
def get_rsa_private_key() :
    keys_file=open(get_current_path()+'keys.pem')

    if keys_file :
        public_key,private_key=pickle.load(keys_file)
        keys_file.close()
        
        return private_key
    
    return None
    
def rsa_encrypt(public_key,data) :
    encrypy_string=''
    
    while len(data)>100 :  #  RSA Encrypt byte once ..
        encrypy_string+=rsa.encrypt(data[:100],public_key)
        data=data[100:]
    encrypy_string+=rsa.encrypt(data,public_key)
    
    return encrypy_string
    
def rsa_decrypt(private_key,data) :
    try :
        decrypt_string=''
        
        while len(data)>128 :  #  RSA Decrypt byte once ..
            decrypt_string+=rsa.decrypt(data[:128],private_key)
            data=data[128:]
        decrypt_string+=rsa.decrypt(data,private_key)
            
        return decrypt_string
    except :
        return None

def list_dir_file() :
    output_file_list=[]
    
    for dir_path,dir_name,file_name in os.walk(get_current_path()) :
        for file_name_index in file_name :
            output_file_list.append((dir_path+'\\'+file_name_index,file_name_index))

    return output_file_list
    
def get_relative_path(file_path) :
    current_file_path=get_current_path()
    
    return file_path.replace(current_file_path,'')

def read_and_delete_file(file_path) :
    read_file=open(file_path)
    
    if read_file :
        file_data=read_file.read()
        
        read_file.close()
#        os.remove(file_path)
        
        return file_data
    
    return None

def pack_push_file(encrypt_cache) :
    push_file=open(get_current_path()+'packet.pck','w')
    
    if push_file :
        push_file.write(pickle.dumps(rsa_encrypt(get_rsa_public_key(),pickle.dumps(encrypt_cache))))
        push_file.close()

def unpack_push_file() :
    push_file=open(get_current_path()+'packet.pck')
    
    if push_file :
        serialization_data=pickle.loads(push_file.read())
        decrypt_cache=pickle.loads(rsa_decrypt(get_rsa_private_key(),serialization_data))

        push_file.close()
#        os.remove(get_current_path()+'packet.pck')

        return decrypt_cache
    
def print_help() :
    print 'Using :'
    print ''
    print '    bule_fariy.py e|d'
    print ''
    print '    bule_fariy.py e    encrypt current path all file'
    print '    bule_fariy.py d    decrypt current path all file'
    

if __name__=='__main__' :
    if 2==len(sys.argv) :
        if 'e'==sys.argv[1] :
            start_tick=time.time()
            
            build_new_rsa_keys()
            
            current_dir_file_list=list_dir_file()
            current_dir_file_cache=[]

            for file_index in current_dir_file_list :
                file_local_path=file_index[0]
                file_name=file_index[1]
                
                if not -1==file_local_path.find('.git') :
                    continue
                elif 'keys.pem'==file_name :
                    continue
                elif 'bule_fariy.py'==file_name :
                    continue
                
                file_relative_path=get_relative_path(file_local_path)
                file_data=read_and_delete_file(file_local_path)
                
                current_dir_file_cache.append({
                    'file_relative_path':file_relative_path,
                    'file_data':file_data
                })
            
            pack_push_file(current_dir_file_cache)
            
            end_tick=time.time()
            
            print 'Using time :'+str(end_tick-start_tick)
            
            exit()
        elif 'd'==sys.argv[1] :
            start_tick=time.time()
            
            decrypt_cache=unpack_push_file()
            
            for file_index in decrypt_cache :
                new_file=open(get_current_path()+file_index['file_relative_path'],'w')
                
                if new_file :
                    new_file.write(file_index['file_data'])
                    new_file.close()
                    
                print get_current_path()+file_index['file_relative_path']
            
            exit()
        
    print_help()
