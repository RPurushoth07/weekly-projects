import "./App.css";
import { useState } from "react";

function App() {
  const [featureName, setFeatureName] = useState("");
  const [requirement, setRequirement] = useState("");
  const [testCases, setTestCases] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const [pdfContent, setPdfContent] = useState("");

  const generateTestCases = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/generate-ai-testcases",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            feature_name: featureName,
            requirement: requirement,
          }),
        }
      );

      const data = await response.json();
      setTestCases(data.testcases);

    } catch (error) {
      console.error(error);
      alert("Failed to generate test cases");
    } finally {
      setLoading(false);
    }
  };

  const uploadPdf = async () => {
    try {
      if (!selectedFile) {
        alert("Please select a PDF file");
        return;
      }

      const formData = new FormData();
      formData.append("file", selectedFile);

      const response = await fetch(
        "http://127.0.0.1:8000/upload-pdf",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (data.success) {
        setPdfContent(data.content);
      } else {
        alert(data.error);
      }

    } catch (error) {
      console.error(error);
      alert("Failed to upload PDF");
    }
  };

  const exportToExcel = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/export-excel",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            testcases: testCases,
          }),
        }
      );

      const blob = await response.blob();

      const url = window.URL.createObjectURL(blob);

      const a = document.createElement("a");
      a.href = url;
      a.download = "TestCases.xlsx";
      a.click();

      window.URL.revokeObjectURL(url);

    } catch (error) {
      console.error(error);
      alert("Failed to export Excel");
    }
  };

  return (
    <div className="container">
      <div className="card">

        <h1 className="title">AI Test Case Generator</h1>

        <div className="input-group">
          <label>Feature Name</label>
          <input
            type="text"
            value={featureName}
            onChange={(e) => setFeatureName(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label>Requirement</label>
          <textarea
            rows="5"
            value={requirement}
            onChange={(e) => setRequirement(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label>Upload Requirement Document (PDF)</label>
          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setSelectedFile(e.target.files[0])}
          />
        </div>

        <button
          className="btn"
          onClick={generateTestCases}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Test Cases"}
        </button>

        <button
          className="btn"
          onClick={uploadPdf}
        >
          Read PDF
        </button>

        <button
          className="btn btn-export"
          onClick={exportToExcel}
          disabled={testCases.length === 0}
        >
          Export Excel
        </button>

        {pdfContent && (
          <div className="summary">
            <h3>Extracted PDF Content</h3>

            <textarea
              value={pdfContent}
              readOnly
              rows="15"
              style={{
                width: "100%",
                padding: "10px",
                marginTop: "10px"
              }}
            />
          </div>
        )}

        {testCases.length > 0 && (
          <div className="summary">
            <h3>Test Case Summary</h3>

            <p>Total Test Cases: {testCases.length}</p>

            <p>
              Positive:
              {testCases.filter(
                (tc) => tc.category === "Positive"
              ).length}
            </p>

            <p>
              Negative:
              {testCases.filter(
                (tc) => tc.category === "Negative"
              ).length}
            </p>

            <p>
              Boundary:
              {testCases.filter(
                (tc) => tc.category === "Boundary"
              ).length}
            </p>

            <p>
              Validation:
              {testCases.filter(
                (tc) => tc.category === "Validation"
              ).length}
            </p>
          </div>
        )}

        {testCases.length > 0 && (
          <div className="table-container">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Category</th>
                  <th>Scenario</th>
                  <th>Expected Result</th>
                  <th>Priority</th>
                </tr>
              </thead>

              <tbody>
                {testCases.map((tc) => (
                  <tr key={tc.id}>
                    <td>{tc.id}</td>
                    <td>{tc.category}</td>
                    <td>{tc.scenario}</td>
                    <td>{tc.expected_result}</td>
                    <td>{tc.priority}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

      </div>
    </div>
  );
}

export default App;