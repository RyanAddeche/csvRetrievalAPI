<<<<<<< HEAD
from django.shortcuts import render
import os
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


# Defines the paths to the responses csv file and the excel file that is being read from
RESPONSES_PATH = os.path.join(settings.BASE_DIR, 'responses', 'responses.csv')
EXCEL_PATH = os.path.join(settings.BASE_DIR, 'data', 'testExcelFile.xlsx')

# API view to handle requests for a specific row in an Excel file
class GetRowView(APIView):
    def post(self, request):
        row_number = request.data.get('row_number')
        requester = request.data.get('requester', 'unknown')

        # Validate the row_number input
        if row_number is None:
            return Response({"error": "Row number is required"}, status=400)
        
        # Ensure row_number is an integer
        try:
            row_number = int(row_number)
        except ValueError:
            return Response({"error": "Row number must be an integer"}, status=400)
        
        # Check if the Excel file exists
        try:
            df = pd.read_excel(EXCEL_PATH)
        except Exception as e:
            return Response({"error": f"Failed to read Excel file: {str(e)}"}, status=500)
        
        # Check if the row_number is within the valid range
        if row_number < 0 or row_number >= len(df):
            return Response({"error": f"Row {row_number} out of range (0 - {len(df)-1})"}, status=400)
        
        # Retrieve the specified row and convert it to a dictionary to match each header with it's value
        row_data = df.iloc[row_number].to_dict()

        # Record the response in a CSV file
        record_response_df = pd.DataFrame([{
            'requester': requester,
            'row_number': row_number,
            'data_returned': str(row_data)
        }])

        # Ensure the directory exists. If it exists append the csv file if it doesn't create the CSV file
        os.makedirs(os.path.dirname(RESPONSES_PATH), exist_ok=True)
        if not os.path.isfile(RESPONSES_PATH):
            record_response_df.to_csv(RESPONSES_PATH, index=False)
        else:
            record_response_df.to_csv(RESPONSES_PATH, mode='a', header=False, index=False)

        # Return the row data as a JSON response
        return Response(row_data, status=200)

        
        

=======
from django.shortcuts import render
import os
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


# Defines the paths to the responses csv file and the excel file that is being read from
RESPONSES_PATH = os.path.join(settings.BASE_DIR, 'responses', 'responses.csv')
EXCEL_PATH = os.path.join(settings.BASE_DIR, 'data', 'testExcelFile.xlsx')

# API view to handle requests for a specific row in an Excel file
class GetRowView(APIView):
    def post(self, request):
        row_number = request.data.get('row_number')
        requester = request.data.get('requester', 'unknown')

        # Validate the row_number input
        if row_number is None:
            return Response({"error": "Row number is required"}, status=400)
        
        # Ensure row_number is an integer
        try:
            row_number = int(row_number)
        except ValueError:
            return Response({"error": "Row number must be an integer"}, status=400)
        
        # Check if the Excel file exists
        try:
            df = pd.read_excel(EXCEL_PATH)
        except Exception as e:
            return Response({"error": f"Failed to read Excel file: {str(e)}"}, status=500)
        
        # Check if the row_number is within the valid range
        if row_number < 0 or row_number >= len(df):
            return Response({"error": f"Row {row_number} out of range (0 - {len(df)-1})"}, status=400)
        
        # Retrieve the specified row and convert it to a dictionary to match each header with it's value
        row_data = df.iloc[row_number].to_dict()

        # Record the response in a CSV file
        record_response_df = pd.DataFrame([{
            'requester': requester,
            'row_number': row_number,
            'data_returned': str(row_data)
        }])

        # Ensure the directory exists. If it exists append the csv file if it doesn't create the CSV file
        os.makedirs(os.path.dirname(RESPONSES_PATH), exist_ok=True)
        if not os.path.isfile(RESPONSES_PATH):
            record_response_df.to_csv(RESPONSES_PATH, index=False)
        else:
            record_response_df.to_csv(RESPONSES_PATH, mode='a', header=False, index=False)

        # Return the row data as a JSON response
        return Response(row_data, status=200)

        
        

>>>>>>> 6e1a9bff5ec84b0dd686fff8e270c43ea54a893d
