import datetime
import time
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service

def video_categories():
    video_categories = service.videoCategories().list(part="snippet", regionCode="US").execute()
    df = pd.DataFrame(video_categories.get("items"))
    return pd.concat([df["id"], df["snippet"].apply(pd.Series)[["title"]]], axis=1)

API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube"]
# SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
client_file = "client-secret.json"
service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

print(video_categories())

"""
Step 1. Uplaod Video
"""
upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + ".000Z"
#upload_time = (datetime.datetime.now())
request_body = {
    "snippet": {
        "title": "Funny Dog",
        "description": "Funny Description",
        "categoryId": "1",
        "tags": ["funny","dogs"]
    },
    "status": {
        "privacyStatus": "private",
        "publishdAt": upload_time,
        "selfDeclaredMadeForKids": False
    }

}

video_file = "dog.mp4"
media_file = MediaFileUpload(video_file)
# print(media_file.size() / pow(1024, 2), "mb")
# print(media_file.to_json())
# print(media_file.mimetype())

response_video_upload = service.videos().insert(
    part="snippet,status",
    onBehalfOfContentOwner="O_CN6Qsf1YjNgQzBPEtslQ",
    onBehalfOfContentOwnerChannel="UCurc5sXwzTRMC1qc9htpnZw",
    body=request_body,
    media_body=media_file
).execute()
uploaded_video_id = response_video_upload.get("id")


# """
# Step 2. Update video thumbnail
# """
# response_thumbnail_upload = service.thumbnails().set(
#     videoId=uploaded_video_id,
#     media_body=MediaFileUpload("thumbnail.png")
# ).execute()

# """
# Step 3 (optional). Set video privacy status to "Public"
# """
# video_id = uploaded_video_id

# counter = 0
# response_update_video = service.videos().list(id=video_id, part="status").execute()
# update_video_body = response_update_video["items"][0]

# while 10 > counter:
#     if update_video_body["status"]["uploadStatus"] == "processed":
#         update_video_body["status"]["privacyStatus"] = "public"
#         service.videos().update(
#             part="status",
#             body=update_video_body
#         ).execute()
#         print("Video {0} privacy status is updated to "{1}"".format(update_video_body["id"], update_video_body["status"]["privacyStatus"]))
#         break
#     # adjust the duration based on your video size
#     time.sleep(10)
#     response_update_video = service.videos().list(id=video_id, part="status").execute()
#     update_video_body = response_update_video["items"][0]
#     counter += 1