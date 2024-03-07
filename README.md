<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Paystack Payment API in Django</title>
</head>
<body>
  <h1>Setting Up Paystack Payment API in Django</h1>
  <p>Integrating Paystack's payment API into your Django project involves several steps:</p>
  <ol>
    <li>**Obtain Paystack API Keys:** Create a Paystack account and obtain your public key and secret key from the dashboard.</li>
    <li>**Install Django Paystack Library:** Simplify the process using a library like django-rest-paystack. Install it using pip install django-rest-paystack.</li>
    <li>**Configure Django Project:** Add 'django-rest-paystack' to your INSTALLED_APPS in settings.py. Set PAYSTACK_PUBLIC_KEY and PAYSTACK_SECRET_KEY with your respective keys.</li>
    <li>**Create API Endpoints:** Use django-rest-paystack to create endpoints for initiating and verifying transactions.</li>
    <li>**Frontend Integration:** Use JavaScript on your frontend to redirect users to the Paystack URL and handle the payment response.</li>
  </ol>
  <p>Remember to test thoroughly in a test environment before deploying to production.</p>
</body>
</html>

