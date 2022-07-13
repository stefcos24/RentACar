from fastapi import HTTPException, status


def raise_id_does_not_exist(id):
    raise HTTPException(status_code=404, detail=f"id number {id} doesn't exists", headers={'X-Header_Error': 'Nothing to be seen at the id'})


def raise_id_does_not_match(id):
    raise HTTPException(status_code=404, detail=f"id number {id} does not match user_id", headers={'X-Header_Error': 'id does not match user_id'})


def raise_user_does_not_exist():
    raise HTTPException(status_code=404, detail="User does not exist!", headers={'X-Header_Error': 'Nothing to be seen at the user'})


def raise_user_not_registered():
    raise HTTPException(status_code=404, detail="User does not match registered users!", headers={'X-Header_Error': 'User not matching registered users'})


def get_user_exception():
    credentials_exceptions = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return credentials_exceptions


def token_exception():
    token_exception_response = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token_exception_response