def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "city":item["city"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]