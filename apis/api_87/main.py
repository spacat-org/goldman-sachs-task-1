from fastapi import FastAPI

app = FastAPI()

base_url = "/api_87"

# Route for retrieving resources
@app.get(f"{base_url}/resource/{resource_id}")
def read_resource(resource_id: int):
    return {"resource_id": resource_id, "message": f"Retrieving resource {resource_id}"}

# Route for creating a new resource
@app.post(f"{base_url}/resource/")
def create_resource(resource_data: dict):
    # Here, you can add the logic to create a new resource
    return {"message": "Resource created successfully"}

# Route for updating a resource
@app.put(f"{base_url}/resource/{resource_id}")
def update_resource(resource_id: int, resource_data: dict):
    # Here, you can add the logic to update the resource with the provided ID
    return {"message": f"Resource {resource_id} updated successfully"}

# Route for deleting a resource
@app.delete(f"{base_url}/resource/{resource_id}")
def delete_resource(resource_id: int):
    # Here, you can add the logic to delete the resource with the provided ID
    return {"message": f"Resource {resource_id} deleted successfully"}
