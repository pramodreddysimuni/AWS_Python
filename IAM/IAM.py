import boto3


def Iam_user(User_name):
    user =boto3.client('iam')
    responce=user.create_user(
        UserName=str(User_name)
        )
    return responce

def Iam_group(User_group):
    group=boto3.client('iam')
    responce=group.create_group(
        GroupName=str(User_group)
    )

    return responce

def add_user_togroup(user_name, user_group):
    add_usertogroup=boto3.client('iam')
    responce=add_usertogroup.add_user_to_group(
        GroupName=user_group,
        UserName=user_name
    )

    return responce

if __name__ == "__main__":
    # Example usage
    user_name = "pramod"
    user_group = "use_less"
    
    # Create user and group
    print(Iam_user(user_name))
    print(Iam_group(user_group))
    
    # Add user to group
    print(add_user_togroup(user_name, user_group))