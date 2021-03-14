from sqlalchemy.orm import Session

import models

# Done
def get_file(db: Session, audio_type: int, audio_file_id: int):
	if audio_type==1:
	    return db.query(models.Song).filter(models.Song.id == audio_file_id).first()
	elif audio_type==2:
	    return db.query(models.Podcast).filter(models.Podcast.id == audio_file_id).first()
	else:
	    return db.query(models.Audiobook).filter(models.Audiobook.id == audio_file_id).first()

# Done
def delete_audio(db: Session, audio_type: int, audio_file_id:int):
	file= None
	if audio_type==1:
	    file = db.query(models.Song).filter(models.Song.id == audio_file_id)
	elif audio_type==2:
	    file = db.query(models.Podcast).filter(models.Podcast.id == audio_file_id)
	else:
	    file = db.query(models.Audiobook).filter(models.Audiobook.id == audio_file_id)

	if file and file  is not None:
		file.delete()
		db.commit()
		return "Audio File Deleted Successfully"
	return False


def get_file_by_id(db: Session, audio_type: int,  audio:dict):
	file = None
	if audio_type==1:
	    file = db.query(models.Song).filter(models.Song.name == audio.get('name')).first()
	elif audio_type==2:
	    file = db.query(models.Podcast).filter(models.Podcast.name == audio.get('name')).first()
	else:
	    file = db.query(models.Audiobook).filter(models.Audiobook.title == audio.get('title')).first()

	if file and file  is not None:
		return True
	return False

# Done
def update_audio(db: Session, audio_type: int, audio_file_id:int, audio: dict):
	file = None
	if audio_type==1:
	    file = db.query(models.Song).filter(models.Song.id == audio_file_id)
	elif audio_type==2:
	    file = db.query(models.Podcast).filter(models.Podcast.id == audio_file_id)
	else:
	    file = db.query(models.Audiobook).filter(models.Audiobook.id == audio_file_id)
	if file and file  is not None:
		try:
			file.update(values=audio)
			db.commit()
			return "Audio File Updated Successfully"
		except Exception as e:
			return False
	return "File Does Not Exists"

# Done
def create_file(db: Session, audio_type: int, audio: dict):
	if audio_type==1:
	    db_user = models.Song(**audio)
	elif audio_type==2:
	    db_user = models.Podcast(**audio)
	else:
	    db_user = models.Audiobook(**audio)
	try:
	    db.add(db_user)
	    db.commit()
	    db.refresh(db_user)
	    return True
	except Exception as e:
		return False

# Done
def get_files(db: Session, skip: int = 0, limit: int = 100,  audio_type: int = 1):
	if audio_type==1:
	    return db.query(models.Song).offset(skip).limit(limit).all()
	elif audio_type==2:
	    return db.query(models.Podcast).offset(skip).limit(limit).all()
	else:
	    return db.query(models.Audiobook).offset(skip).limit(limit).all()

