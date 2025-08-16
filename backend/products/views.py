
from rest_framework.views import APIView
from rest_framework.response import Response
DEMO=[
    {"id":1,"name":"HDFC Regalia Credit Card","category":"Credit Card","bank":"HDFC Bank"},
    {"id":2,"name":"SBI Home Loan","category":"Loan","bank":"SBI"},
    {"id":3,"name":"ICICI Platinum Debit Card","category":"Debit Card","bank":"ICICI Bank"},
]
class ProductList(APIView):
    def get(self, request):
        q=request.GET.get("q","").lower().strip()
        data=[p for p in DEMO if q in p["name"].lower()] if q else DEMO
        return Response(data)
class Health(APIView):
    def get(self, request):
        return Response({"status":"ok"})
