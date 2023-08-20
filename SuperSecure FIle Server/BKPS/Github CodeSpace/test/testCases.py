# test_cases.py
import sys
from sserver import User, File, FileManager # Import the necessary classes and methods

def execute_test_cases():
    file_manager = FileManager()

    # Create users and upload files for testing
    file_manager.create_user("alice", 0)
    file_manager.create_user("bob", 1)
    file_manager.create_user("anonymous", 0)

    file_manager.upload_file("secret.txt", "Confidential data", "alice",0)
    file_manager.upload_file("important.txt", "Top Secret personal data", "alice",1)
    file_manager.upload_file("CompanySecrets.txt", "Company Data", "alice",1)
    file_manager.upload_file("HealthDataLeaked.csv", "ID,Health,insurance Cost", "anonymous",0)


    flag = True
    #Test Case 1
    output = file_manager.download_file('alice', 'secret.txt')
    result = "FAILED"
    if(output == "Downloading secret.txt: Confidential data"):
        result="PASSED"
    else:
        flag=False
        print(f"Test case 1: {output} : Test Case {result}")# Should work

    #Test Case 2
    output = file_manager.download_file("bob", "secret.txt")
    result = "FAILED"
    if(output == "Downloading secret.txt: Confidential data"):
        result="PASSED"
    else:
        flag=False
        print(f"Test case 2: {output} : Test Case {result}")# Should work

    #Test Case 3
    output = file_manager.download_file("bob", "important.txt")
    result = "FAILED"
    if(output == "Permission denied"):
        result="PASSED"
    else: 
        flag=False
        print(f"Test case 3: {output} : Test Case {result}")# Should fail due to permissions

     #Test Case 4
    output = file_manager.download_file("anonymous", "CompanySecrets.txt")
    result = "FAILED"
    if(output == "Permission denied"):
        result="PASSED"
    else:    
        flag=False
        print(f"Test case 4: {output} : Test Case {result}")# Should fail due to permissions

     #Test Case 5
    output = file_manager.download_file("bob", "CompanySecrets.txt")
    result = "FAILED"
    if(output == "Permission denied"):
        result="PASSED"
    else:    
        flag=False
        print(f"Test case 5: {output} : Test Case {result}")# Should fail due to permissions

    #Test Case 6
    output = file_manager.download_file("bob", "HealthDataLeaked.csv")
    result = "FAILED"
    if(output == "Downloading HealthDataLeaked.csv: ID,Health,insurance Cost"):
        result="PASSED"
    else:    
        flag=False
        print(f"Test case 6: {output} : Test Case {result}")# Should work


    #Test Case 7
    output = file_manager.download_file("alice", "HealthDataLeaked.csv")
    result = "FAILED"
    if(output == "Downloading HealthDataLeaked.csv: ID,Health,insurance Cost"):
        result="PASSED"
    else:    
        flag=False
        print(f"Test case 7: {output} : Test Case {result}")# Should work

    if(flag):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    execute_test_cases()



# if (user.permissions >= 1 and file.Filepermissions==0) or (user.username == file.owner) or (file.owner=="anonymous"):#Corrected Code
#             return (f"Downloading {file.name}: {file.content}")
#         else:
#             return ("Permission denied")


# if user.permissions >= 1 or (user.username == file.owner):#Vuln Code
#             return (f"Downloading {file.name}: {file.content}")
#         else:
#             return ("Permission denied")
