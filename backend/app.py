from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from openpyxl import Workbook
from pypdf import PdfReader
from gemini_service import generate_test_cases
import json

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Model
class RequirementRequest(BaseModel):
    feature_name: str
    requirement: str


# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "AI Test Case Generator API Running"
    }


# Generate AI Test Cases
@app.post("/generate-ai-testcases")
def generate_ai(data: RequirementRequest):

    result = generate_test_cases(
        data.requirement
    )

    parsed_result = json.loads(result)

    return {
        "testcases": parsed_result
    }


# Export Excel
@app.post("/export-excel")
def export_excel(data: dict):

    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "Test Cases"

    headers = [
        "ID",
        "Category",
        "Scenario",
        "Expected Result",
        "Priority"
    ]

    sheet.append(headers)

    for tc in data["testcases"]:
        sheet.append([
            tc.get("id", ""),
            tc.get("category", ""),
            tc.get("scenario", ""),
            tc.get("expected_result", ""),
            tc.get("priority", "")
        ])

    file_name = "TestCases.xlsx"

    workbook.save(file_name)

    return FileResponse(
        path=file_name,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=file_name
    )


# Upload PDF
@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    try:

        reader = PdfReader(file.file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return {
            "success": True,
            "filename": file.filename,
            "content": text[:5000]
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }