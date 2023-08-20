#user.permissions
    # 0 : Normal User
    # 1 : SuperUser

#Created Users
    # file_manager.create_user("alice", 0)
    # file_manager.create_user("bob", 1)
    # file_manager.create_user("anonymous", 0)

#Uploaded Files
    # file_manager.upload_file("secret.txt", "Confidential data", "alice",0)
    # file_manager.upload_file("important.txt", "Top Secret personal data", "alice",1)
    # file_manager.upload_file("CompanySecrets.txt", "Company Data", "bob",0)
    # file_manager.upload_file("HealthDataLeaked.csv", "ID,Health,insurance Cost", "alice",0)



class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

class File:
    def __init__(self, name, content, owner,Filepermissions):
        self.name = name
        self.content = content
        self.owner = owner
        self.Filepermissions = Filepermissions

class FileManager:
    def __init__(self):
        self.users = []
        self.files = []

    def create_user(self, username, permissions):
        user = User(username, permissions)
        self.users.append(user)

    def upload_file(self, name, content, owner,Filepermissions):
        file = File(name, content, owner,Filepermissions)
        self.files.append(file)

    def download_file(self, username, file_name):
        user = next((u for u in self.users if u.username == username), None)
        if not user:
            return ("User not found")


        file = next((f for f in self.files if f.name == file_name), None)
        if not file:
            return ("File not found")        
        
        if user.permissions >= 1 or (user.username == file.owner):
            return (f"Downloading {file.name}: {file.content}")
        else:
            return ("Permission denied")
