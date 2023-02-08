import os
from flask import Flask, request
import process


@app.route("/scrap-catalog-data")
def scrap_catalog_data():
    is_success = 1
    error_details = ""
    try:
        catalog_url = request.args.get('catalogUrl')
        catalog_type = request.args.get('catalogType')
        firestore_task_id = request.args.get('firestoreTaskId')
        vendor_name = request.args.get('vendorName')

        if not catalog_url:
            is_success = 0
            error_details += "Insufficient Data Provided. Details: No 'catalogUrl' provided."

        if not catalog_type:
            is_success = 0
            error_details += "Insufficient Data Provided. Details: No 'catalogType' provided."

        if not firestore_task_id:
            is_success = 0
            error_details += "Insufficient Data Provided. Details: No 'firestoreTaskId' provided."

        if not vendor_name:
            is_success = 0
            error_details += "Insufficient Data Provided. Details: No 'vendorName' provided."

        if is_success:
            data = {
                "catalog_url": catalog_url,
                "catalog_type": catalog_type,
                "firestore_task_id": firestore_task_id,
                "vendor_name": vendor_name
            }
            is_success, err_details = process.main(data)
            error_details += err_details

    except Exception as e:
        is_success = 0
        error_details = f"Error occurred while processing. Details: {str(e)}"

    return {
        "is_success": is_success,
        "error_details": error_details
    }


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 4444)))
