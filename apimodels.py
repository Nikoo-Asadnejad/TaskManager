class TaskModel(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskResponse(TaskModel):
    id: int
    class Config:
        orm_mode = True