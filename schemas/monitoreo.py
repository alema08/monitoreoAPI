def monitoreoEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "lugar": str(item["lugar"]),
        "autor": str(item["autor"]),
        "temperatura": item["temperatura"],
        "humedad": item["humedad"],
        "createdAt": item["createdAt"],
        "updatedAt": item["updatedAt"]
    }

def muchosMonitoreosEntity(entity) -> list:
    return [monitoreoEntity(item) for item in entity]