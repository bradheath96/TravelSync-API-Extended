from pydantic import BaseModel


class FileBase(BaseModel):
    file_name: str
    itinerary_id: int
    file_path: str 

class FileCreate(FileBase):
    pass  

class FileResponse(FileBase):
    id: int
     

    class Config:
        orm_mode = True