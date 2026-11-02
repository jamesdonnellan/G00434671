from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def user_payload(eq_id=1, b_name="Bob", id=1):
    return {"equipment_id": eq_id, "borrower_name": b_name}

# Test to get all loans
def test_get_loans(client):
    response = client.get("/loans")

    assert response.status_code == 200
    assert response.json()["equipment_id"] == 1
    assert response.json()["borrower_name"] == "James"

# Test to create a loan
def test_create_loan(client):
    response = client.post("/loans", json=user_payload(id=1))
    
    assert response.status_code == 201
    assert response.json()["equipment_id"] == 1
    assert response.json()["borrower_name"] == "James"
    assert response.json()["loan_days"] == 2
    assert response.json()["purpose"] == "College Fees"
    assert response.json()["status"] == "PENDING"

    saved = client.get("/loans/1")
    assert saved.status_code == 200

# Test to delete a loan by id
def test_delete_loan(client):
    response = client.delete("/loans/1")
    assert response.status_code == 204