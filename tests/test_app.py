from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    activities = client.get("/activities").json()
    if email in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].remove(email)

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert unregister_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
