from fastapi import FastAPI
app = FastAPI()

# minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}

# Get --> Read Todo
@app.get("/todo", tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}


# Post --> Create Todo
@app.post("/todo", tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "The todo has been successfully added"}


# Put --> Update Todo
@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id: int, body:dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
        
            return {
                "data": "Todo with id {id} has been updated"
            }
    
    return {"data": "Todo with this id {id} wasn't found"}


# Delete --> Delete Todo
@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todos.remove(todo)
        
            return {
                "data": f"Todo with id {id} has been deleted"
            }
    
    return {"data": f"Todo with this id {id} wasn't found"}


todos = [
    {
        "id": "1", 
        "Activity": "Go to the bank"
    },

    {
        "id": "2", 
        "Activity": "Attend the Webinar about Higher education in the US"
    }
]

