# views.py
import logging
import time
from datetime import datetime
from django.http import JsonResponse
from .models import donation_table
import json
from django.views.decorators.csrf import csrf_exempt

# Configure logging
logger = logging.getLogger('file_log')

@csrf_exempt
def make_donation(request):
    start_time = time.time()
    logger.info("\nRequest to make a donation")
    logger.info(f"Time: {datetime.now()}")

    try:
        if request.method != 'POST':
            return JsonResponse(data={"message": "Invalid request method"}, status=405)

        data = json.loads(request.body.decode('utf-8'))

        email_address = str(data.get('email_address'))
        phone_number = str(data.get('phone_number'))
        address = str(data.get('address'))
        donation_amount = data.get('donation_amount')
        message = str(data.get('message', ''))
        receive_updates = data.get('receive_updates')

        logger.info(email_address,phone_number,address)
        # Email validation
        if not email_address or '@' not in email_address:
            return JsonResponse(data={"message": "Invalid email address"}, status=400)

        # Phone number validation
        if not phone_number.isdigit() or len(phone_number) < 10 or len(phone_number) > 15:
            return JsonResponse(data={"message": "Phone number must be between 10 and 15 digits and contain only numbers"}, status=400)

        # Donation amount validation
        try:
            donation_amount = float(donation_amount)
            if donation_amount <= 0:
                return JsonResponse(data={"message": "Donation amount must be a positive number"}, status=400)
        except (ValueError, TypeError):
            return JsonResponse(data={"message": "Donation amount must be a valid number"}, status=400)

        donation = donation_table(
            email_address=email_address,
            phone_number=phone_number,
            address=address,
            donation_amount=donation_amount,
            message=message,
            receive_updates=receive_updates
        )
        donation.save()
        logger.info("Donation record created successfully")

        logger.info(f"Time taken: {time.time() - start_time} seconds")
        return JsonResponse(data={"message": "Donation recorded successfully"}, status=200)

    except Exception as e:
        logger.error(f"Error while processing donation: {e}")
        return JsonResponse(data={"message": "An error occurred while processing your donation"}, status=500)


def test(request):
    return JsonResponse(data={"message": "Test response"}, status=200)