import jwt

payload={
  "user_id": "9e1da8cc328d487586784cc48b30d009",
  "profile_id": "9ca8769bcd1047dd93091eee76b56e04",
  "profile_type": "Owner",
  "exp": 1735631188
} 
secret="v0cZBrajxUbrJhlWL44nFIN3ObX1vqBtKKNm38IcdjalB7c2mXXEpeJu7S6J_O821TH7_ZjoScoT1SiEcKfjfKf4dv4bMwwrwUxeTxHKBvvRkwmo2c--4fX433SHWgi6dXpsrf9CW3YjfcPCGHJfRnTVxHoHnJrFB4vaELDk2rXwogk_tP1tIpfvCFYGj0CSsujjvNpQyr3k4CnVQL8JpDgThZUNbYbuZXvVhups7BC3TWijaZRMJkwmkCt1W7gNWVRW0RCCOsJ-5-entjrprGqfxuLg45ITXQPBrwZdaWIRcD2BSx6Xx_6-RX1z0dUI7Xs9NU6AgN6h47tAvVrqyQ"
algorithm='HS256'
token = jwt.encode(payload, secret, algorithm=algorithm)
print(token)