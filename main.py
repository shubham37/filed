from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Done
@app.post("/audio/{audio_type}/")
def create_audio(audio_type: int, audio: dict, db: Session = Depends(get_db)):
    is_exists = crud.get_file_by_id(db, audio_type=audio_type, audio=audio)
    if is_exists:
        raise HTTPException(status_code=400, detail="Audio File already registered")
    uploaded_file = crud.create_file(db, audio_type=audio_type, audio=audio)
    if not uploaded_file:
        raise HTTPException(status_code=500, detail="Try Again")
    return "Audio Uploaded Successfully"

# Done
@app.get("/audio/{audio_type}")
def read_files(audio_type : int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    files = crud.get_files(db, skip=skip, limit=limit, audio_type=audio_type)
    return files

# Done
@app.get("/audio/{audio_type}/{audio_file_id}")
def read_audio(audio_type: int, audio_file_id: int, db: Session = Depends(get_db)):
    audio_file = crud.get_file(db, audio_type=audio_type, audio_file_id=audio_file_id)
    if audio_file and audio_file is not None:
	    return audio_file
    return "No File For ID {0} in Audio Type {1}".format(audio_file_id, audio_type)

# Done
@app.delete("/audio/{audio_type}/{audio_file_id}")
def delete_audio(audio_type: int, audio_file_id: int, db: Session = Depends(get_db)):
    is_delete = crud.delete_audio(db, audio_type=audio_type, audio_file_id=audio_file_id)
    if is_delete:
        return is_delete
    raise HTTPException(status_code=400, detail="File Does Not Exists.")

# Done
@app.put("/audio/{audio_type}/{audio_file_id}")
def update_audio(audio_type: int, audio_file_id: int, audio: dict, db: Session = Depends(get_db)):
    is_update = crud.update_audio(db=db, audio_type = audio_type, audio_file_id = audio_file_id, audio = audio)
    if not is_update:
        raise HTTPException(status_code=400, detail="Please Check Data")
    return is_update

