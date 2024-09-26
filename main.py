from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/")
def read_user():
    return {"message": "Hello World"}

app.include_router(prefix='/user', router=router)
