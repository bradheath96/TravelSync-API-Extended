from src.models.google_places_models import fetch_nearby_places, fetch_place_info, fetch_place_detail
from fastapi import APIRouter, HTTPException, Request


router = APIRouter()
@router.post('/info')
async def get_place_info(address):

    # data = await request.json()  # Extract JSON data from the request body
    # address = data.get("address")
    
    if not address:
        raise HTTPException(status_code=422, detail="Address field is required")


    try:
        response = await fetch_place_info(address)
        return {"placeInfo": response}
    except HTTPException as err:
        raise err #This is the errors we expect can happen e.g. 500, 404 
    except Exception as err:
        # this catches unexpected non HTTP errors like ValueError or TypeError (code bugs)
        # it presents this error to the client as an internal server error 500 with the error message
        # this means errors are handled in consistent mannor
        raise HTTPException(status_code=500, detail=str(err))


@router.post('/nearby')
async def get_nearby_places(location: str, radius=2000, type="tourist_attraction"):
    try:
        response = await fetch_nearby_places(location, radius, type)
        return {"locations": response}
    except HTTPException as err:
        print(err)
        raise err
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


@router.post('/detail')
async def get_place_detail(place_id: str):
    try:
        response = await fetch_place_detail(place_id)
        return {"details": response}
    except HTTPException as err:
        raise err
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
