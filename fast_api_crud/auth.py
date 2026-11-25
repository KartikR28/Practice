from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = "mysecret123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# verify password
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# decode token
def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
