from dotenv import dotenv_values

config = dotenv_values()

from werkzeug.security import generate_password_hash, check_password_hash

class PwdBD():
    def __init__(self, pwd):
        self._pwd = pwd
    
    
    def _set_pwd(self, pwd):
        self._pwd = pwd
        
    def _get_pwd(self):
        return self._pwd
    
    def genPwd(self, phrase):
        phrase = self._pwd
        passHash = generate_password_hash(phrase, method=config['METHOD'], salt_length=int(config['SALT_LENGTH']))
        return passHash
       
    
    def checkPwd(self):
        hashed = self.genPwd(self._get_pwd())
        return check_password_hash(hashed, self._get_pwd())   
       
       
       
if __name__ == '__main__':
    f = PwdBD('Isaac') # set value Isaac when instance a PwdDB object
    #print(f._set_pwd('Abimael')) # set value Abimael with set property
    f._set_pwd('Cervantes')
    print(f.genPwd(f._get_pwd()))
    print(f.checkPwd())
    
    
    
    #newPwd = f._get_pwd()
    #print(newPwd)
    #print(f._get_pwd())
    
    #g = generate_password_hash(f._get_pwd(), method=config['METHOD'], salt_length=int(config['SALT_LENGTH']))
    
    #print(generate_password_hash(f._get_pwd(), method='pbkdf2', salt_length=16))
    #print(check_password_hash(g, 'Abimael'))